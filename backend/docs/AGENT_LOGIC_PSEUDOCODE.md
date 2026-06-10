# DeerFlow Backend Agent Logic Analysis

This document provides a pseudo-code representation of the core logic of the DeerFlow backend agent, designed for learning agent development patterns.

## 1. Agent Factory (Lead Agent)
The agent is constructed using a factory pattern that assembles the LLM, tools, and a middleware chain into a LangGraph.

```python
def make_lead_agent(config):
    # Model Selection
    model = create_chat_model(config.model_name)

    # Tool Registry
    tools = [bash_tool, read_file_tool, web_search, task_tool]

    # System Prompt Construction (Dynamic Injection)
    system_prompt = apply_prompt_template(
        agent_name="DeerFlow",
        soul=load_soul(),
        skills=load_skills(),
        workspace="/mnt/user-data/workspace"
    )

    # Middleware Chain (Execution Pipeline)
    middlewares = [
        ThreadDataMiddleware(),    # Sets up isolated directories
        UploadsMiddleware(),       # Injects uploaded files
        SandboxMiddleware(),       # Prepares execution environment
        SummarizationMiddleware(), # Manages context window
        MemoryMiddleware(),        # Queues learning tasks
        ClarificationMiddleware()  # Intercepts questions to user
    ]

    return create_langgraph_agent(model, tools, system_prompt, middlewares)
```

## 2. Middleware System
Middlewares intercept the agent's lifecycle (before/after model, around tool calls).

```python
class AgentMiddleware:
    def before_agent(self, state, runtime):
        # Setup logic before LLM turn
        pass

    def wrap_tool_call(self, request, handler):
        # Intercept tool calls (e.g., for security/translation)
        # 1. Translate virtual paths to host paths
        # 2. Execute tool
        # 3. Mask host paths in output
        return handler(request)

    def after_agent(self, state, runtime):
        # Cleanup or async triggers
        pass
```

## 3. Sandbox & Tool Interaction
Tools operate in an isolated environment using virtual path mapping.

```python
def sandbox_tool(path, runtime):
    # Resolve thread-specific sandbox
    sandbox = get_sandbox(runtime)

    # Translate /mnt/user-data/... to actual host path
    actual_path = resolve_path(path, runtime.thread_data)

    # Execute operation in isolated environment (Docker/Local)
    result = sandbox.read_or_execute(actual_path)

    # Return sanitized result to LLM
    return mask_paths(result)
```

## 4. Persistent Memory Flow
Memory is updated asynchronously to avoid blocking the user.

```python
async def memory_update_flow(messages):
    # 1. Extract context (Facts, Preferences) via specialized LLM call
    new_memory_data = await extraction_model.invoke(messages)

    # 2. Merge with existing JSON storage
    # 3. Filter facts by confidence and relevance
    # 4. Persist to disk/DB
    save_memory(new_memory_data)
```

## Key Architectual Patterns
- **Isolation**: Every thread has its own workspace.
- **Interception**: All LLM-Tool interactions are mediated by middlewares.
- **Asynchronicity**: Long-term memory and sub-agents run in background workers.
- **Statelessness**: The agent graph is reconstructed per-turn from the persisted thread state.
