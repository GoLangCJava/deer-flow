# DeerFlow 后端 Agent 逻辑分析

本文档提供了 DeerFlow 后端 Agent 核心逻辑的伪代码表示，旨在帮助开发者学习 Agent 开发模式。

## 1. Agent 工厂 (Lead Agent)
Agent 使用工厂模式构建，将 LLM、工具和中间件链组装成 LangGraph 图。

```python
def make_lead_agent(config):
    # 模型选择
    model = create_chat_model(config.model_name)

    # 工具注册
    tools = [bash_tool, read_file_tool, web_search, task_tool]

    # 系统提示词构建 (动态注入)
    system_prompt = apply_prompt_template(
        agent_name="DeerFlow",
        soul=load_soul(),
        skills=load_skills(),
        workspace="/mnt/user-data/workspace"
    )

    # 中间件链 (执行流水线)
    middlewares = [
        ThreadDataMiddleware(),    # 设置隔离目录
        UploadsMiddleware(),       # 注入上传文件
        SandboxMiddleware(),       # 准备执行环境
        SummarizationMiddleware(), # 管理上下文窗口
        MemoryMiddleware(),        # 排队记忆任务
        ClarificationMiddleware()  # 拦截用户提问
    ]

    return create_langgraph_agent(model, tools, system_prompt, middlewares)
```

## 2. 中间件系统
中间件拦截 Agent 的生命周期（模型运行前后、工具调用前后）。

```python
class AgentMiddleware:
    def before_agent(self, state, runtime):
        # LLM 轮次前的设置逻辑
        pass

    def wrap_tool_call(self, request, handler):
        # 拦截工具调用（例如：为了安全或路径转换）
        # 1. 将虚拟路径转换为宿主机路径
        # 2. 执行工具
        # 3. 在输出中掩码宿主机路径
        return handler(request)

    def after_agent(self, state, runtime):
        # 清理或异步触发逻辑
        pass
```

## 3. 沙箱与工具交互
工具通过虚拟路径映射在隔离环境中运行。

```python
def sandbox_tool(path, runtime):
    # 获取当前线程特定的沙箱
    sandbox = get_sandbox(runtime)

    # 将 /mnt/user-data/... 转换为实际的宿主机路径
    actual_path = resolve_path(path, runtime.thread_data)

    # 在隔离环境（Docker/Local）中执行操作
    result = sandbox.read_or_execute(actual_path)

    # 将脱敏后的结果返回给 LLM
    return mask_paths(result)
```

## 4. 持久化记忆流
记忆异步更新，避免阻塞用户。

```python
async def memory_update_flow(messages):
    # 1. 通过专门的 LLM 调用提取上下文（事实、偏好）
    new_memory_data = await extraction_model.invoke(messages)

    # 2. 与现有 JSON 存储合并
    # 3. 根据置信度和相关性过滤事实
    # 4. 持久化到磁盘/数据库
    save_memory(new_memory_data)
```

## 核心架构模式
- **隔离性 (Isolation)**：每个线程都有独立的工作空间。
- **拦截机制 (Interception)**：所有 LLM 与工具的交互都由中间件调节。
- **异步性 (Asynchronicity)**：长期记忆和子 Agent 在后台工作进程中运行。
- **无状态性 (Statelessness)**：Agent 图每一轮都根据持久化的线程状态重新构建。
