# -*- coding: utf-8 -*-
"""
Builds deerflow-core-architecture-flowchart.html
A standalone, interactive, styled HTML flowchart with core logic code.
"""

import os
import sys
import html
import json

output_file = "/home/user/deer-flow/deerflow-core-architecture-flowchart.html"

def get_code_snippet(rel_path, start_line, end_line):
    full_path = os.path.join("/home/user/deer-flow", rel_path)
    if not os.path.exists(full_path):
        return f"# File {rel_path} not found"
    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        snippet = "".join(lines[start_line-1:end_line])
        return snippet

print("Extracting code snippets from repository...")

code_make_lead_agent = get_code_snippet(
    "backend/packages/harness/deerflow/agents/lead_agent/agent.py",
    730, 860
)

code_build_middlewares = get_code_snippet(
    "backend/packages/harness/deerflow/agents/lead_agent/agent.py",
    453, 580
)

code_clarification_part1 = get_code_snippet(
    "backend/packages/harness/deerflow/agents/middlewares/clarification_middleware.py",
    98, 135
)
code_clarification_part2 = get_code_snippet(
    "backend/packages/harness/deerflow/agents/middlewares/clarification_middleware.py",
    430, 570
)
code_clarification = code_clarification_part1 + "\n    # ... [表单标准化与字段解析] ...\n\n" + code_clarification_part2

code_loop_detection = get_code_snippet(
    "backend/packages/harness/deerflow/agents/middlewares/loop_detection_middleware.py",
    187, 310
)

code_dangling_tool = get_code_snippet(
    "backend/packages/harness/deerflow/agents/middlewares/dangling_tool_call_middleware.py",
    161, 280
)

code_run_agent = get_code_snippet(
    "backend/packages/harness/deerflow/runtime/runs/worker.py",
    980, 1060
)

code_task_tool = get_code_snippet(
    "backend/packages/harness/deerflow/tools/builtins/task_tool.py",
    215, 330
)

code_subagent_executor = get_code_snippet(
    "backend/packages/harness/deerflow/subagents/executor.py",
    438, 560
)

code_local_sandbox = get_code_snippet(
    "backend/packages/harness/deerflow/sandbox/local/local_sandbox.py",
    82, 210
)

code_deer_mem = get_code_snippet(
    "backend/packages/harness/deerflow/agents/memory/backends/deermem/deer_mem.py",
    94, 210
)

code_run_manager = get_code_snippet(
    "backend/packages/harness/deerflow/runtime/runs/manager.py",
    219, 320
)

def escape_code(text):
    return html.escape(text.strip())

print("Generating HTML content...")

html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🦌 DeerFlow 2.0 核心代码逻辑流程图与架构全景解析</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- FontAwesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Prism.js for Syntax Highlighting -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" id="prism-theme" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css" rel="stylesheet" />

  <!-- Mermaid.js for Flowcharts -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>

  <style>
    :root {{
      --bg-primary: #0b0f19;
      --bg-secondary: #111827;
      --bg-tertiary: #1f2937;
      --bg-card: rgba(17, 24, 39, 0.85);
      --border-color: #374151;
      --border-accent: #3b82f6;
      --text-primary: #f3f4f6;
      --text-secondary: #9ca3af;
      --text-muted: #6b7280;
      --accent-blue: #3b82f6;
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-purple: #8b5cf6;
      --accent-rose: #f43f5e;
      --code-bg: #090d16;
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
      --shadow-glow: 0 0 25px rgba(59, 130, 246, 0.25);
    }}

    [data-theme="light"] {{
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-tertiary: #f1f5f9;
      --bg-card: rgba(255, 255, 255, 0.9);
      --border-color: #e2e8f0;
      --border-accent: #2563eb;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      --accent-blue: #2563eb;
      --accent-cyan: #0891b2;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-purple: #7c3aed;
      --accent-rose: #e11d48;
      --code-bg: #1e293b;
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --shadow-glow: 0 0 25px rgba(37, 99, 235, 0.15);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      transition: background-color 0.3s ease, color 0.3s ease;
      overflow-x: hidden;
    }}

    code, pre {{
      font-family: 'Fira Code', Consolas, Monaco, 'Courier New', Courier, monospace;
    }}

    /* Top Sticky Header */
    header.top-header {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(11, 15, 25, 0.9);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color);
      padding: 0.75rem 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
    }}

    [data-theme="light"] header.top-header {{
      background: rgba(255, 255, 255, 0.9);
    }}

    .header-logo {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--text-primary);
    }}

    .header-logo .icon {{
      font-size: 1.8rem;
    }}

    .header-logo h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .header-controls {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .search-box {{
      position: relative;
      width: 280px;
    }}

    .search-box input {{
      width: 100%;
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 9999px;
      padding: 0.45rem 1rem 0.45rem 2.25rem;
      color: var(--text-primary);
      font-size: 0.875rem;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}

    .search-box input:focus {{
      border-color: var(--accent-blue);
      box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
    }}

    .search-box i {{
      position: absolute;
      left: 0.85rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.85rem;
    }}

    .theme-toggle-btn {{
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      padding: 0.45rem 0.85rem;
      border-radius: 0.5rem;
      cursor: pointer;
      font-size: 0.875rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: background 0.2s;
    }}

    .theme-toggle-btn:hover {{
      background: var(--border-color);
    }}

    /* Main Container & Layout */
    .app-layout {{
      display: flex;
      min-height: calc(100vh - 60px);
    }}

    /* Sidebar Navigation */
    aside.sidebar {{
      width: 280px;
      flex-shrink: 0;
      background: var(--bg-secondary);
      border-right: 1px solid var(--border-color);
      position: sticky;
      top: 61px;
      height: calc(100vh - 61px);
      overflow-y: auto;
      padding: 1.5rem 1rem;
    }}

    .sidebar-nav-title {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
      padding-left: 0.75rem;
      font-weight: 700;
    }}

    .nav-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }}

    .nav-item a {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.6rem 0.85rem;
      color: var(--text-secondary);
      text-decoration: none;
      border-radius: 0.5rem;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s ease;
    }}

    .nav-item a:hover {{
      color: var(--text-primary);
      background: var(--bg-tertiary);
    }}

    .nav-item.active a {{
      color: #ffffff;
      background: linear-gradient(135deg, #2563eb, #3b82f6);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }}

    .nav-item .badge {{
      margin-left: auto;
      font-size: 0.7rem;
      padding: 0.15rem 0.45rem;
      border-radius: 9999px;
      background: var(--bg-tertiary);
      color: var(--text-muted);
    }}

    .nav-item.active .badge {{
      background: rgba(255, 255, 255, 0.2);
      color: #ffffff;
    }}

    /* Main Content Area */
    main.main-content {{
      flex: 1;
      padding: 2rem 3rem 5rem;
      max-width: 1300px;
      overflow-x: hidden;
    }}

    /* Hero Banner */
    .hero-banner {{
      background: linear-gradient(135deg, rgba(30, 58, 138, 0.4) 0%, rgba(88, 28, 135, 0.4) 100%);
      border: 1px solid rgba(59, 130, 246, 0.3);
      border-radius: 1rem;
      padding: 2rem 2.5rem;
      margin-bottom: 3rem;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-glow);
    }}

    .hero-title {{
      font-size: 2rem;
      font-weight: 800;
      margin-bottom: 0.75rem;
      letter-spacing: -0.025em;
      line-height: 1.25;
    }}

    .hero-subtitle {{
      color: var(--text-secondary);
      font-size: 1.05rem;
      max-width: 900px;
      margin-bottom: 1.5rem;
    }}

    .hero-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
    }}

    .pill-tag {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
    }}

    /* Section Styles */
    section.doc-section {{
      margin-bottom: 4.5rem;
      scroll-margin-top: 80px;
    }}

    .section-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 1rem;
      margin-bottom: 1.75rem;
    }}

    .section-title-wrapper {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}

    .section-icon {{
      font-size: 1.5rem;
      width: 42px;
      height: 42px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 0.75rem;
      background: var(--bg-tertiary);
      color: var(--accent-blue);
      border: 1px solid var(--border-color);
    }}

    .section-title {{
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.015em;
    }}

    .section-desc {{
      color: var(--text-secondary);
      font-size: 0.95rem;
      margin-bottom: 1.5rem;
      line-height: 1.7;
    }}

    /* Card Containers */
    .card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 0.875rem;
      padding: 1.5rem;
      margin-bottom: 1.75rem;
      box-shadow: var(--shadow-md);
      backdrop-filter: blur(12px);
      transition: border-color 0.2s, box-shadow 0.2s;
    }}

    .card:hover {{
      border-color: rgba(59, 130, 246, 0.5);
    }}

    .card-title {{
      font-size: 1.15rem;
      font-weight: 600;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-primary);
    }}

    /* Mermaid Flowchart Card & Controls */
    .diagram-container {{
      position: relative;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 0.875rem;
      padding: 2rem 1.5rem 1.5rem;
      margin-bottom: 2rem;
      overflow: hidden;
      box-shadow: var(--shadow-md);
    }}

    .diagram-toolbar {{
      position: absolute;
      top: 0.75rem;
      right: 0.75rem;
      display: flex;
      gap: 0.35rem;
      z-index: 10;
      background: rgba(17, 24, 39, 0.8);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-color);
      padding: 0.25rem;
      border-radius: 0.5rem;
    }}

    .diagram-toolbar button {{
      background: transparent;
      border: none;
      color: var(--text-secondary);
      width: 28px;
      height: 28px;
      border-radius: 0.35rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      transition: background 0.15s, color 0.15s;
    }}

    .diagram-toolbar button:hover {{
      background: var(--bg-tertiary);
      color: var(--text-primary);
    }}

    .mermaid-wrapper {{
      width: 100%;
      overflow-x: auto;
      display: flex;
      justify-content: center;
      min-height: 200px;
      transition: transform 0.2s ease;
      transform-origin: center top;
    }}

    .mermaid {{
      width: 100%;
      text-align: center;
    }}

    /* Step Grid & Flow Elements */
    .step-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-bottom: 1.75rem;
    }}

    .step-card {{
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 0.75rem;
      padding: 1.25rem;
      position: relative;
      transition: transform 0.2s, border-color 0.2s;
    }}

    .step-card:hover {{
      transform: translateY(-2px);
      border-color: var(--accent-blue);
    }}

    .step-number {{
      position: absolute;
      top: 0.75rem;
      right: 0.75rem;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      background: var(--bg-secondary);
      border-radius: 9999px;
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--border-color);
    }}

    .step-icon {{
      font-size: 1.25rem;
      color: var(--accent-cyan);
      margin-bottom: 0.5rem;
    }}

    .step-title {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 0.4rem;
    }}

    .step-desc {{
      font-size: 0.85rem;
      color: var(--text-secondary);
      line-height: 1.5;
    }}

    /* Code Box and Details */
    .code-box {{
      background: var(--code-bg);
      border: 1px solid var(--border-color);
      border-radius: 0.75rem;
      margin-top: 1rem;
      overflow: hidden;
    }}

    .code-header {{
      background: rgba(0, 0, 0, 0.3);
      border-bottom: 1px solid var(--border-color);
      padding: 0.6rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .code-path {{
      font-size: 0.8rem;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-family: 'Fira Code', monospace;
    }}

    .code-actions {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .copy-btn {{
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      padding: 0.25rem 0.6rem;
      border-radius: 0.375rem;
      font-size: 0.75rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s;
    }}

    .copy-btn:hover {{
      background: var(--border-color);
      color: var(--text-primary);
    }}

    .code-content {{
      max-height: 480px;
      overflow-y: auto;
      padding: 0;
      margin: 0;
    }}

    .code-content pre {{
      margin: 0 !important;
      padding: 1.25rem !important;
      background: transparent !important;
      font-size: 0.85rem !important;
    }}

    /* Collapsible Details */
    details.code-details {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 0.75rem;
      margin-top: 1rem;
      overflow: hidden;
    }}

    details.code-details summary {{
      padding: 0.85rem 1.25rem;
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      background: var(--bg-tertiary);
      transition: background 0.2s;
    }}

    details.code-details summary:hover {{
      background: var(--border-color);
    }}

    details.code-details summary::after {{
      content: '展开代码 ▼';
      font-size: 0.75rem;
      color: var(--accent-blue);
      font-weight: 500;
    }}

    details.code-details[open] summary::after {{
      content: '收起代码 ▲';
    }}

    /* Table Styles */
    .data-table-container {{
      overflow-x: auto;
      border: 1px solid var(--border-color);
      border-radius: 0.75rem;
      margin-bottom: 1.5rem;
    }}

    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.875rem;
      text-align: left;
    }}

    table.data-table th {{
      background: var(--bg-tertiary);
      color: var(--text-primary);
      padding: 0.85rem 1rem;
      font-weight: 600;
      border-bottom: 1px solid var(--border-color);
      white-space: nowrap;
    }}

    table.data-table td {{
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-secondary);
    }}

    table.data-table tr:last-child td {{
      border-bottom: none;
    }}

    table.data-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
      color: var(--text-primary);
    }}

    .hook-badge {{
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 600;
      padding: 0.2rem 0.5rem;
      border-radius: 0.375rem;
      margin-right: 0.3rem;
      margin-bottom: 0.2rem;
    }}

    .hook-before-agent {{ background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.4); }}
    .hook-before-model {{ background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .hook-wrap-model   {{ background: rgba(139, 92, 246, 0.2); color: #a78bfa; border: 1px solid rgba(139, 92, 246, 0.4); }}
    .hook-after-model  {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }}
    .hook-after-agent  {{ background: rgba(244, 63, 94, 0.2); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); }}
    .hook-wrap-tool    {{ background: rgba(6, 182, 212, 0.2); color: #22d3ee; border: 1px solid rgba(6, 182, 212, 0.4); }}

    /* Key Invariants / Callouts */
    .callout {{
      border-left: 4px solid var(--accent-blue);
      background: rgba(59, 130, 246, 0.08);
      padding: 1rem 1.25rem;
      border-radius: 0 0.5rem 0.5rem 0;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
      color: var(--text-secondary);
    }}

    .callout strong {{
      color: var(--text-primary);
    }}

    /* Footer */
    footer.page-footer {{
      border-top: 1px solid var(--border-color);
      padding: 2.5rem 2rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.875rem;
      background: var(--bg-secondary);
    }}

    @media (max-width: 1024px) {{
      aside.sidebar {{
        display: none;
      }}
      main.main-content {{
        padding: 1.5rem 1.5rem 4rem;
      }}
    }}
  </style>
</head>
<body data-theme="dark">

  <!-- Top Sticky Header -->
  <header class="top-header">
    <a href="#" class="header-logo">
      <span class="icon">🦌</span>
      <div>
        <h1>DeerFlow 2.0 架构与核心代码全景流程图</h1>
      </div>
    </a>

    <div class="header-controls">
      <div class="search-box">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" id="searchInput" placeholder="搜索组件/中间件/函数/代码..." oninput="handleSearch(this.value)">
      </div>
      <button class="theme-toggle-btn" onclick="toggleTheme()">
        <i class="fa-solid fa-moon" id="themeIcon"></i>
        <span id="themeText">明亮模式</span>
      </button>
    </div>
  </header>

  <div class="app-layout">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <div class="sidebar-nav-title">架构与流程目录</div>
      <ul class="nav-list" id="sidebarNav">
        <li class="nav-item active">
          <a href="#overview">
            <i class="fa-solid fa-network-wired"></i>
            <span>1. 全局架构与请求流</span>
            <span class="badge">Nginx/Gateway</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#lead-agent">
            <i class="fa-solid fa-sitemap"></i>
            <span>2. 主代理装配流程</span>
            <span class="badge">make_lead_agent</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#middleware-pipeline">
            <i class="fa-solid fa-layer-group"></i>
            <span>3. 14+ 中间件管道</span>
            <span class="badge">Pipeline</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#runtime-worker">
            <i class="fa-solid fa-bolt"></i>
            <span>4. 运行时主循环与 SSE</span>
            <span class="badge">run_agent</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#subagent-system">
            <i class="fa-solid fa-robot"></i>
            <span>5. Sub-agent 任务委派</span>
            <span class="badge">task_tool</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#core-subsystems">
            <i class="fa-solid fa-cubes"></i>
            <span>6. 沙箱/记忆/MCP子系统</span>
            <span class="badge">Core</span>
          </a>
        </li>
      </ul>

      <div style="margin-top: 2rem; padding: 1rem; background: var(--bg-tertiary); border-radius: 0.5rem; border: 1px solid var(--border-color); font-size: 0.8rem; color: var(--text-secondary);">
        <div style="font-weight: 600; margin-bottom: 0.4rem; color: var(--text-primary);"><i class="fa-solid fa-circle-info" style="color: var(--accent-blue);"></i> 交互说明</div>
        <p>1. 点击流程图右上角可缩放/重置<br>2. 展开各折叠卡片查看仓库真实源码<br>3. 点击代码右上角按钮可一键复制代码</p>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      
      <!-- Hero Banner -->
      <div class="hero-banner">
        <h2 class="hero-title">DeerFlow 2.0 Super Agent Harness 核心代码全景</h2>
        <p class="hero-subtitle">
          DeerFlow 2.0 是一套基于 LangGraph 的超级 Agent 框架，通过单主代理（Lead Agent）统一编排多子代理（Sub-agents）、持久化长期记忆（DeerMem）、容器化安全沙箱（Sandbox）及动态可扩展技能（Skills/MCP）。
        </p>
        <div class="hero-tags">
          <span class="pill-tag"><i class="fa-solid fa-microchip"></i> LangGraph 引擎</span>
          <span class="pill-tag"><i class="fa-solid fa-shield-halved"></i> 14+ 阶段 Middleware</span>
          <span class="pill-tag"><i class="fa-solid fa-box-open"></i> Docker / 本地沙箱隔离</span>
          <span class="pill-tag"><i class="fa-solid fa-brain"></i> DeerMem 记忆提取</span>
          <span class="pill-tag"><i class="fa-solid fa-bolt"></i> SSE 实时流式响应</span>
        </div>
      </div>

      <!-- SECTION 1: 全局服务拓扑与请求生命周期 -->
      <section id="overview" class="doc-section">
        <div class="section-header">
          <div class="section-title-wrapper">
            <div class="section-icon"><i class="fa-solid fa-network-wired"></i></div>
            <h2 class="section-title">1. 全局服务拓扑与 HTTP/SSE 请求生命周期</h2>
          </div>
        </div>

        <p class="section-desc">
          DeerFlow 2.0 采用微服务与网关嵌入式 Agent 运行时架构。Nginx（端口 2026）作为唯一的公共入口，根据 URL 将客户端请求无缝分发给 Next.js 前端（端口 3000）或 FastAPI Gateway（端口 8001），并通过 URL Rewrite 实现了与标准 LangGraph SDK 客户端的完全兼容。
        </p>

        <!-- Diagram 1 -->
        <div class="diagram-container">
          <div class="diagram-toolbar">
            <button onclick="zoomDiagram(this, 1.15)" title="放大"><i class="fa-solid fa-plus"></i></button>
            <button onclick="zoomDiagram(this, 0.85)" title="缩小"><i class="fa-solid fa-minus"></i></button>
            <button onclick="resetDiagram(this)" title="重置"><i class="fa-solid fa-rotate-left"></i></button>
          </div>
          <div class="mermaid-wrapper">
            <div class="mermaid">
graph TB
    subgraph ClientLayer ["🖥️ 客户端层 (Client Layer)"]
        Browser["Web 浏览器 (Next.js 聊天界面)"]
        IM["IM 接入渠道 (飞书/Slack/钉钉/Telegram/GitHub Webhook)"]
        SDK["LangGraph SDK / Python 嵌入式客户端"]
    end

    subgraph IngressLayer ["🌐 入口反向代理 (Ingress)"]
        Nginx["Nginx Reverse Proxy (Port 2026)<br/>• 默认 Loopback 绑定 (127.0.0.1)<br/>• URL Rewrite: /api/langgraph/* ➔ /api/*"]
    end

    subgraph AppLayer ["⚡ 服务层 (Application Services)"]
        Frontend["Next.js 前端 (Port 3000)<br/>React 19 / TanStack Query / SSE 订阅"]
        Gateway["FastAPI Gateway (Port 8001)<br/>• REST Routers (threads/models/uploads/mcp/skills)<br/>• 嵌入式 LangGraph 运行时"]
    end

    subgraph CoreRuntime ["⚙️ 核心 Agent 执行引擎 (Harness Runtime)"]
        RunMgr["RunManager<br/>• 租约控制 (Lease)<br/>• 孤儿恢复 (Orphan Recovery)<br/>• 幂等启动 (Idempotency)"]
        Worker["Run Worker (asyncio.Task)<br/>• 线程级 Checkpoint 锁<br/>• 目标验证与继续循环<br/>• 工作区变更比对"]
        Bridge["StreamBridge<br/>• SSE 流分发 (messages/values/custom)<br/>• Redis / 内存广播后端"]
        LeadAgent["Lead Agent Graph<br/>• 14+ 阶段 Middleware 管道<br/>• 动态提示词与工具组装"]
    end

    subgraph ResourceLayer ["📦 资源与子系统 (Subsystems & Storage)"]
        Checkpointer["Checkpointer 存储<br/>SQLite / PostgreSQL / Redis"]
        Sandbox["Sandbox Provider<br/>LocalSandbox (直接执行) / AioSandbox (Docker)"]
        DeerMem["DeerMem 长期记忆<br/>Markdown 事实库 / 向量检索 / 防抖提取"]
        SubagentPool["Subagent Executor<br/>后台并行任务池 / 步骤事件流"]
        MCP["MCP Servers<br/>stdio / SSE / HTTP 协议工具"]
    end

    Browser -->|HTTP / SSE 请求| Nginx
    IM -->|Webhook / API| Nginx
    SDK -->|/api/langgraph/*| Nginx

    Nginx -->|/* (前端静态资源/路由)| Frontend
    Nginx -->|/api/* (重写后的 Agent 路由)| Gateway

    Gateway -->|创建/管理 Run| RunMgr
    RunMgr -->|后台异步拉起| Worker
    Worker -->|astream 驱动执行| LeadAgent
    Worker -->|发布 SSE 事件| Bridge
    Bridge -->|流式推送到 HTTP 响应| Gateway
    Gateway -->|实时 Token 流| Nginx
    Nginx -->|SSE 数据帧| Browser

    LeadAgent --> Checkpointer
    LeadAgent --> Sandbox
    LeadAgent --> DeerMem
    LeadAgent --> SubagentPool
    LeadAgent --> MCP
            </div>
          </div>
        </div>

        <div class="step-grid">
          <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-icon"><i class="fa-solid fa-arrow-right-to-bracket"></i></div>
            <div class="step-title">统一反向代理</div>
            <div class="step-desc">Nginx 监听 2026 端口。将 <code>/api/langgraph/*</code> 抹除前缀重写至 Gateway <code>/api/*</code>，保持对 LangGraph 原生协议的无感兼容。</div>
          </div>
          <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-icon"><i class="fa-solid fa-key"></i></div>
            <div class="step-title">RunManager 租约与幂等</div>
            <div class="step-desc">Gateway 接收到 Run 创建请求后，通过 RunManager 申领租约、注册幂等性校验，防止重复触发与死锁。</div>
          </div>
          <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-icon"><i class="fa-solid fa-tower-broadcast"></i></div>
            <div class="step-title">异步 Task 与 SSE 桥接</div>
            <div class="step-desc">启动独立 <code>asyncio.Task</code> 执行 <code>run_agent</code>，通过 <code>StreamBridge</code> 发送 <code>messages</code>、<code>values</code> 及 <code>task_*</code> 事件。</div>
          </div>
        </div>

        <!-- Code Block 1: RunManager & Gateway Entry -->
        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：RunManager 租约控制与幂等创建 (packages/harness/deerflow/runtime/runs/manager.py)</div>
          <p style="font-size: 0.875rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
            <code>RunManager.create_run</code> 负责在多进程/多 Worker 场景下通过 SQLite / PostgreSQL 唯一约束及过期租约检查实现并发安全与孤儿恢复。
          </p>
          <details class="code-details" open>
            <summary>查看核心源码 (RunManager.create_run)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/runtime/runs/manager.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_run_manager)}</code></pre>
              </div>
            </div>
          </details>
        </div>
      </section>

      <!-- SECTION 2: 主代理装配流程 -->
      <section id="lead-agent" class="doc-section">
        <div class="section-header">
          <div class="section-title-wrapper">
            <div class="section-icon"><i class="fa-solid fa-sitemap"></i></div>
            <h2 class="section-title">2. 主代理装配与初始化流程 (<code>make_lead_agent</code>)</h2>
          </div>
        </div>

        <p class="section-desc">
          Lead Agent 的装配是 DeerFlow 运行的核心起点。通过 <code>make_lead_agent</code> 工厂函数，系统根据运行配置动态解析模型、RBAC 授权规则、多源工具集、延迟 MCP 工具编排、14+ 阶段 Middleware 栈，最终编译为 LangGraph 可执行图。
        </p>

        <!-- Diagram 2 -->
        <div class="diagram-container">
          <div class="diagram-toolbar">
            <button onclick="zoomDiagram(this, 1.15)" title="放大"><i class="fa-solid fa-plus"></i></button>
            <button onclick="zoomDiagram(this, 0.85)" title="缩小"><i class="fa-solid fa-minus"></i></button>
            <button onclick="resetDiagram(this)" title="重置"><i class="fa-solid fa-rotate-left"></i></button>
          </div>
          <div class="mermaid-wrapper">
            <div class="mermaid">
graph TD
    Start(["🚀 调用 make_lead_agent(config)"]) --> ParseCfg["1. 解析运行时配置 & 上下文<br/>• user_id / agent_name<br/>• is_plan_mode / subagent_enabled<br/>• channel_name (Webhook安全隔离)"]

    ParseCfg --> ResolveModel["2. 模型解析与授权校验<br/>• _resolve_model_name(requested)<br/>• _authorize_model_name(RBAC enforce)<br/>• 确定 thinking_enabled & supports_vision"]

    ResolveModel --> GatherTools["3. 多源工具池收集 (Tool Gathering)<br/>• 内置工具: present_files, ask_clarification, task<br/>• 沙箱工具: bash, read_file, write_file, ls, grep<br/>• 外部工具: web_search, fetch, MCP servers<br/>• 自定义代理工具: update_agent (Webhook通道自动禁用)"]

    GatherTools --> AuthzFilter["4. 授权过滤与延迟工具封装<br/>• apply_tool_authorization (RBAC 策略校验)<br/>• assemble_deferred_tools (超大 MCP 延迟加载)<br/>• 构建 mcp_routing_middleware & 路由提示词"]

    AuthzFilter --> BuildMW["5. 构建 Middleware 执行链<br/>• build_lead_runtime_middlewares (基础沙箱/安全)<br/>• 挂载 14 个 Lead 专属 Middleware<br/>• 注册扩展贡献插件 Middleware"]

    BuildMW --> BuildPrompt["6. 生成静态系统提示词 (Prompt Assembly)<br/>• apply_prompt_template<br/>• 注入工具说明、可用技能索引、Subagent 配额规则<br/>• 剥离易变时间/记忆 (保持前缀缓存命中)"]

    BuildPrompt --> CompileGraph["7. 编译 LangGraph 可执行图<br/>• create_agent(model, tools, middleware, prompt)<br/>• 规范化 ThreadState 状态契约 (Mode 适配)"]

    CompileGraph --> OutputAssembly(["📦 返回 LeadAgentAssembly(graph, descriptor)"])
            </div>
          </div>
        </div>

        <div class="callout">
          <strong>🔥 重要设计不变量 (Tracing Invariant)：</strong>
          在 <code>make_lead_agent</code> 内部创建的所有 <code>ChatModel</code> 实例，必须显式传递 <code>attach_tracing=False</code>。Langfuse / LangSmith 的 Tracing Callback 已在图调用的根节点统一挂载，若在内部重复挂载会导致 Span 重复且丢失 <code>session_id</code> 与 <code>user_id</code> 上下文。
        </div>

        <!-- Code Block 2: make_lead_agent -->
        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：主代理装配工厂 (backend/packages/harness/deerflow/agents/lead_agent/agent.py)</div>
          <details class="code-details" open>
            <summary>查看核心源码 (make_lead_agent & build_middlewares)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/agents/lead_agent/agent.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_make_lead_agent)}</code></pre>
              </div>
            </div>
          </details>
        </div>
      </section>

      <!-- SECTION 3: 14+ 阶段 Middleware 管道 -->
      <section id="middleware-pipeline" class="doc-section">
        <div class="section-header">
          <div class="section-title-wrapper">
            <div class="section-icon"><i class="fa-solid fa-layer-group"></i></div>
            <h2 class="section-title">3. 14+ 阶段 Middleware 管道与生命周期深度剖析</h2>
          </div>
        </div>

        <p class="section-desc">
          DeerFlow 的中间件模型并非传统的对称洋葱圈，而是针对多轮 Tool-Call 对话高度优化的<strong>单向管道拦截体系</strong>。
          LangGraph <code>create_agent</code> 遵循：<strong><code>before_*</code> 按照列表正序 (0 ➔ N) 执行，<code>after_*</code> 按照列表反序 (N ➔ 0) 执行</strong>。
        </p>

        <!-- Diagram 3: Middleware Pipeline Flow -->
        <div class="diagram-container">
          <div class="diagram-toolbar">
            <button onclick="zoomDiagram(this, 1.15)" title="放大"><i class="fa-solid fa-plus"></i></button>
            <button onclick="zoomDiagram(this, 0.85)" title="缩小"><i class="fa-solid fa-minus"></i></button>
            <button onclick="resetDiagram(this)" title="重置"><i class="fa-solid fa-rotate-left"></i></button>
          </div>
          <div class="mermaid-wrapper">
            <div class="mermaid">
graph TB
    Start(["用户请求进入 invoke / astream"]) --> TD

    subgraph BA ["<b>[阶段 1] before_agent</b> (正序执行 0 ➔ N)"]
        direction TB
        TD["[0] ThreadDataMiddleware<br/>创建隔离目录 (workspace/uploads/outputs)"]
        UL["[1] UploadsMiddleware<br/>扫描上传文件并注入上下文提示"]
        SB["[2] SandboxMiddleware<br/>向 Provider 申领/初始化沙箱实例"]
        LD_BA["[12] LoopDetectionMiddleware<br/>清理同 thread 旧 run 的残留 warnings"]
        TD --> UL --> SB --> LD_BA
    end

    subgraph BM ["<b>[阶段 2] before_model</b> (每轮循环 正序 0 ➔ N)"]
        direction TB
        SM["[6] SummarizationMiddleware<br/>超限历史消息自动总结与压缩"]
        TODO_BM["[7] TodoMiddleware (Plan Mode)<br/>加载当前待办列表状态"]
        VI["[10] ViewImageMiddleware<br/>解析并注入视觉模型的图片 Base64"]
        SM --> TODO_BM --> VI
    end

    subgraph WM ["<b>[阶段 3] wrap_model_call</b> (模型调用包装 外层 ➔ 内层)"]
        direction TB
        IS["InputSanitization<br/>清理 Prompt 注入攻击标签"]
        TOB["ToolOutputBudget<br/>截断超大工具返回字符"]
        TRS["ToolResultSanitization<br/>对 Web 检索结果做二次清洗"]
        DTC["[3] DanglingToolCall<br/>补齐悬空 ToolMessage 避免模型报错"]
        DC["DynamicContext<br/>注入动态时间 & 记忆提醒 (前缀缓存优化)"]
        DUR["DurableContext<br/>注入委托账本 (Delegation Ledger)"]
        DTF["DeferredToolFilter<br/>隐藏未激活的超大 MCP 工具模式"]
        SMC["SystemMessageCoalescing<br/>合并多个系统消息为首部单条 (兼容严格后端)"]
        LD_WM["[12] LoopDetection<br/>安全注入排队 warning 到末尾 HumanMessage"]

        IS --> TOB --> TRS --> DTC --> DC --> DUR --> DTF --> SMC --> LD_WM
    end

    LD_BA --> SM
    VI --> IS
    LD_WM --> LLM["<b>🧠 LLM MODEL 推理生成</b>"]

    subgraph AM ["<b>[阶段 4] after_model</b> (反序拦截 N ➔ 0)"]
        direction TB
        CM_AM["[13] ClarificationMiddleware<br/>检测 ask_clarification 并剔除兄弟工具调用"]
        SFR["SafetyFinishReason<br/>模型触发安全审查时清空 tool_calls"]
        MLF["ModelLengthFinishReason<br/>标记输出达到最大 Token 截断"]
        TRM["TerminalResponse<br/>空回复兜底重试与错误占位"]
        LD_AM["[12] LoopDetection<br/>哈希检测循环调用，超限入队 warning / 硬拦截"]
        SL["[11] SubagentLimit<br/>截断超出配额的并发 subagent task"]
        TI["[8] TitleMiddleware<br/>首轮对话异步触发自动生成标题"]
        TODO_AM["[7] TodoMiddleware<br/>同步模型产生的待办状态更新"]

        CM_AM --> SFR --> MLF --> TRM --> LD_AM --> SL --> TI --> TODO_AM
    end

    LLM --> CM_AM

    subgraph TC ["<b>[工具调用分支] wrap_tool_call</b>"]
        direction TB
        CM_TC["[13] Clarification<br/>拦截 ask_clarification ➔ Command(goto=END)"]
        AUTHZ["[4] Authorization/Guardrails<br/>RBAC 权限策略与黑白名单校验"]
        SA["SandboxAudit<br/>沙箱命令高危模式审计"]
        RBW["ReadBeforeWrite<br/>写文件前必须先读校验"]
        TP["ToolProgress<br/>工具实时进度事件广播"]
        TEH["[5] ToolErrorHandling<br/>异常捕获与 deerflow_tool_meta 标记"]
        TR["ToolReceipt<br/>生成工具调用数字凭证账本"]

        CM_TC --> AUTHZ --> SA --> RBW --> TP --> TEH --> TR
    end

    subgraph AA ["<b>[阶段 5] after_agent</b> (结束阶段 反序 N ➔ 0)"]
        direction TB
        LD_CLEAN["[12] LoopDetection<br/>清理当前 run 未消费的 pending warnings"]
        MEM["[9] MemoryMiddleware<br/>异步触发长期事实提取并入队 DeerMem"]
        SBR["[2] SandboxMiddleware<br/>释放沙箱资源与临时挂载点"]

        LD_CLEAN --> MEM --> SBR
    end

    TODO_AM -->|有 tool_calls 且非 Clarification| CM_TC
    CM_TC -->|工具执行完成| BM
    TODO_AM -->|无 tool_calls 或已完成| LD_CLEAN
    CM_AM -.->|命中 ask_clarification| END_NODE(["中断退出，等待用户回复表单"])
    SBR --> FinalEnd(["🏁 Run 成功结束，返回结果"])
            </div>
          </div>
        </div>

        <!-- Middleware Table -->
        <div class="card">
          <div class="card-title"><i class="fa-solid fa-list-check" style="color: var(--accent-blue);"></i> 14 个核心 Middleware 职责与执行钩子对照表</div>
          <div class="data-table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Middleware 名称</th>
                  <th>执行阶段 (Hooks)</th>
                  <th>核心职责与执行逻辑</th>
                  <th>硬依赖/位置约束</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>0</strong></td>
                  <td><strong>ThreadDataMiddleware</strong></td>
                  <td><span class="hook-badge hook-before-agent">before_agent</span></td>
                  <td>初始化线程独立物理与虚拟目录 (<code>workspace</code>, <code>uploads</code>, <code>outputs</code>)。</td>
                  <td>必须在 Sandbox 之前</td>
                </tr>
                <tr>
                  <td><strong>1</strong></td>
                  <td><strong>UploadsMiddleware</strong></td>
                  <td><span class="hook-badge hook-before-agent">before_agent</span></td>
                  <td>扫描线程 <code>uploads/</code> 目录，将文件列表与虚拟路径注入消息前缀。</td>
                  <td>位于 ThreadData 之后</td>
                </tr>
                <tr>
                  <td><strong>2</strong></td>
                  <td><strong>SandboxMiddleware</strong></td>
                  <td><span class="hook-badge hook-before-agent">before_agent</span> <span class="hook-badge hook-after-agent">after_agent</span></td>
                  <td><code>before_agent</code> 向 Provider 申领沙箱，<code>after_agent</code> 释放容器资源，形成洋葱对称。</td>
                  <td>成对执行</td>
                </tr>
                <tr>
                  <td><strong>3</strong></td>
                  <td><strong>DanglingToolCallMiddleware</strong></td>
                  <td><span class="hook-badge hook-wrap-model">wrap_model_call</span></td>
                  <td>修复悬空的 tool_call（补充 synthetic error ToolMessage），剔除孤儿 ToolMessage，防止严格模型 400 报错。</td>
                  <td>必须位于 wrap_model 外层</td>
                </tr>
                <tr>
                  <td><strong>4</strong></td>
                  <td><strong>Guardrail / Authorization</strong></td>
                  <td><span class="hook-badge hook-wrap-tool">wrap_tool_call</span></td>
                  <td>RBAC 权限决策器：校验当前用户是否有权调用特定工具；阻止未授权命令。</td>
                  <td>包裹在工具执行外层</td>
                </tr>
                <tr>
                  <td><strong>5</strong></td>
                  <td><strong>ToolErrorHandlingMiddleware</strong></td>
                  <td><span class="hook-badge hook-wrap-tool">wrap_tool_call</span></td>
                  <td>捕获工具执行异常并标准化为 ToolMessage，并在 meta 中标记 <code>deerflow_tool_meta</code>。</td>
                  <td>内层兜底</td>
                </tr>
                <tr>
                  <td><strong>6</strong></td>
                  <td><strong>SummarizationMiddleware</strong></td>
                  <td><span class="hook-badge hook-before-model">before_model</span></td>
                  <td>历史消息到达 Token 阈值时触发自动摘要压缩，保留近期轮次。</td>
                  <td>模型调用前</td>
                </tr>
                <tr>
                  <td><strong>7</strong></td>
                  <td><strong>TodoMiddleware</strong></td>
                  <td><span class="hook-badge hook-before-model">before_model</span> <span class="hook-badge hook-after-model">after_model</span></td>
                  <td>Plan Mode 下维护任务清单，追踪多步骤任务执行进度与状态更新。</td>
                  <td>配置开启生效</td>
                </tr>
                <tr>
                  <td><strong>8</strong></td>
                  <td><strong>TitleMiddleware</strong></td>
                  <td><span class="hook-badge hook-after-model">after_model</span></td>
                  <td>在首次对话后，后台轻量模型异步生成符合会话主题的标题。</td>
                  <td>仅在首轮触发</td>
                </tr>
                <tr>
                  <td><strong>9</strong></td>
                  <td><strong>MemoryMiddleware</strong></td>
                  <td><span class="hook-badge hook-after-agent">after_agent</span></td>
                  <td>检测会话中的偏好、决策、事实，异步防抖入队 DeerMem 长期记忆库。</td>
                  <td>Run 结束后触发</td>
                </tr>
                <tr>
                  <td><strong>10</strong></td>
                  <td><strong>ViewImageMiddleware</strong></td>
                  <td><span class="hook-badge hook-before-model">before_model</span></td>
                  <td>将 <code>view_image</code> 查看的文件读取为 Base64 并组装为 Vision 消息载荷。</td>
                  <td>仅视觉模型加载</td>
                </tr>
                <tr>
                  <td><strong>11</strong></td>
                  <td><strong>SubagentLimitMiddleware</strong></td>
                  <td><span class="hook-badge hook-after-model">after_model</span></td>
                  <td>检查当前轮次派生的 <code>task</code> 工具调用，对超出并发与总量上限的任务执行拦截截断。</td>
                  <td>位于 Model 之后</td>
                </tr>
                <tr>
                  <td><strong>12</strong></td>
                  <td><strong>LoopDetectionMiddleware</strong></td>
                  <td><span class="hook-badge hook-before-agent">before_agent</span> <span class="hook-badge hook-wrap-model">wrap_model</span> <span class="hook-badge hook-after-model">after_model</span> <span class="hook-badge hook-after-agent">after_agent</span></td>
                  <td>滑动窗口哈希比对工具调用。达到 warning 阈值入队提醒；达到 hard_limit 强制剥离 tool_calls 终止死循环。</td>
                  <td>跨多个生命周期钩子</td>
                </tr>
                <tr>
                  <td><strong>13</strong></td>
                  <td><strong>ClarificationMiddleware</strong></td>
                  <td><span class="hook-badge hook-after-model">after_model</span> <span class="hook-badge hook-wrap-tool">wrap_tool_call</span></td>
                  <td>拦截 <code>ask_clarification</code>，丢弃同批次兄弟工具，返回 <code>Command(goto=END)</code> 中断当前执行并展示用户表单。</td>
                  <td><strong>必须位于列表最末尾</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Code Block 3: Clarification & LoopDetection -->
        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：ClarificationMiddleware 中断与表单标准化</div>
          <details class="code-details" open>
            <summary>查看核心源码 (ClarificationMiddleware)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/agents/middlewares/clarification_middleware.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_clarification)}</code></pre>
              </div>
            </div>
          </details>
        </div>

        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：LoopDetectionMiddleware 循环检测与排队注入</div>
          <details class="code-details">
            <summary>查看核心源码 (LoopDetectionMiddleware)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/agents/middlewares/loop_detection_middleware.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_loop_detection)}</code></pre>
              </div>
            </div>
          </details>
        </div>

        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：DanglingToolCallMiddleware 悬空与孤儿修复</div>
          <details class="code-details">
            <summary>查看核心源码 (DanglingToolCallMiddleware)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/agents/middlewares/dangling_tool_call_middleware.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_dangling_tool)}</code></pre>
              </div>
            </div>
          </details>
        </div>
      </section>

      <!-- SECTION 4: 运行时主循环与 SSE 流式推送 -->
      <section id="runtime-worker" class="doc-section">
        <div class="section-header">
          <div class="section-title-wrapper">
            <div class="section-icon"><i class="fa-solid fa-bolt"></i></div>
            <h2 class="section-title">4. 运行时主循环与 SSE 流式推送 (<code>worker.py</code>)</h2>
          </div>
        </div>

        <p class="section-desc">
          <code>worker.py:run_agent</code> 是 Agent 真正的物理执行核心。它运行在独立的后台异步任务中，控制 Checkpoint 线程锁、消息流式迭代、Goal 自动延续、工作区变更比对以及数字交付凭证的持久化。
        </p>

        <!-- Diagram 4 -->
        <div class="diagram-container">
          <div class="diagram-toolbar">
            <button onclick="zoomDiagram(this, 1.15)" title="放大"><i class="fa-solid fa-plus"></i></button>
            <button onclick="zoomDiagram(this, 0.85)" title="缩小"><i class="fa-solid fa-minus"></i></button>
            <button onclick="resetDiagram(this)" title="重置"><i class="fa-solid fa-rotate-left"></i></button>
          </div>
          <div class="mermaid-wrapper">
            <div class="mermaid">
sequenceDiagram
    autonumber
    participant UI as 前端 Web / Client
    participant GW as FastAPI Gateway
    participant WK as Worker (run_agent)
    participant LK as Checkpoint Lock
    participant LG as LangGraph Lead Graph
    participant SB as StreamBridge
    participant FS as 线程工作区 (Workspace)

    UI ->> GW: POST /api/threads/{id}/runs (创建 Run)
    GW ->> WK: 启动 asyncio.Task(run_agent)
    activate WK
    WK ->> LK: 获取线程独占锁 _checkpoint_thread_lock(thread_id)
    activate LK
    WK ->> FS: capture_workspace_snapshot (拍摄初始文件状态)

    loop 图流式迭代 (agent.astream)
        WK ->> LG: agent.astream(stream_mode=["messages", "updates", "values"])
        activate LG
        LG -->> WK: yield chunk (Token / ToolCall / StateUpdate)
        deactivate LG
        WK ->> SB: bridge.publish(run_id, event, serialize(chunk))
        SB -->> GW: SSE 数据帧
        GW -->> UI: 实时推送 (messages / task_* / values)
    end

    opt 存在会话目标 (Session Goal)
        WK ->> WK: evaluate_goal_completion (评估任务是否达成)
        alt 目标未完成且有进展
            WK ->> LG: 构造 Goal Continuation 消息继续迭代执行
        end
    end

    WK ->> FS: diff_workspace (计算生成文件与变更输出)
    WK ->> WK: _persist_delivery_receipt (持久化交付凭据)
    WK ->> LK: 释放锁
    deactivate LK
    WK ->> SB: publish terminal event (完成信号)
    deactivate WK
    GW -->> UI: SSE 流结束
            </div>
          </div>
        </div>

        <!-- Code Block 4: run_agent -->
        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：运行时核心流式主循环 (backend/packages/harness/deerflow/runtime/runs/worker.py)</div>
          <details class="code-details" open>
            <summary>查看核心源码 (worker.py 中的 _stream_once 循环)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/runtime/runs/worker.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_run_agent)}</code></pre>
              </div>
            </div>
          </details>
        </div>
      </section>

      <!-- SECTION 5: Sub-agent 子代理任务委派系统 -->
      <section id="subagent-system" class="doc-section">
        <div class="section-header">
          <div class="section-title-wrapper">
            <div class="section-icon"><i class="fa-solid fa-robot"></i></div>
            <h2 class="section-title">5. Sub-agent 子代理任务委派系统 (<code>task_tool</code> & <code>executor</code>)</h2>
          </div>
        </div>

        <p class="section-desc">
          DeerFlow 支持主代理将复杂、高耗时的研究、编码或分析任务分派给专门的子代理（如 <code>bash_agent</code>, <code>general_purpose</code>）。
          子代理拥有独立的执行上下文、4 个轻量级专属 Middleware 以及专属的步骤事件流通道（<code>task_step</code>）。
        </p>

        <!-- Diagram 5 -->
        <div class="diagram-container">
          <div class="diagram-toolbar">
            <button onclick="zoomDiagram(this, 1.15)" title="放大"><i class="fa-solid fa-plus"></i></button>
            <button onclick="zoomDiagram(this, 0.85)" title="缩小"><i class="fa-solid fa-minus"></i></button>
            <button onclick="resetDiagram(this)" title="重置"><i class="fa-solid fa-rotate-left"></i></button>
          </div>
          <div class="mermaid-wrapper">
            <div class="mermaid">
graph LR
    Lead["Lead Agent<br/>(LLM 生成 task 工具调用)"] -->|调用 task_tool| TaskTool["task_tool.py<br/>• 配额校验 (Max Concurrent/Total)<br/>• 生成 execution_id 与 Trace ID"]

    TaskTool -->|异步派发| Exec["SubagentExecutor.execute<br/>• 调度到独立 ThreadPool / EventLoop<br/>• 隔离运行环境"]

    subgraph SubagentRuntime ["🤖 Subagent 隔离执行图 (Subagent Graph)"]
        direction TB
        SubMW["Subagent 4大轻量 Middleware<br/>1. ThreadDataMiddleware<br/>2. SandboxMiddleware<br/>3. GuardrailMiddleware<br/>4. ToolErrorHandlingMiddleware"]
        SubModel["Subagent Model (独立模型/提示词)"]
        SubTools["专用工具集 (受限权限)"]
        
        SubMW --> SubModel --> SubTools
    end

    Exec --> SubagentRuntime

    SubagentRuntime -->|步骤消息捕获| StepEmitter["capture_new_step_messages<br/>实时发射 aemit_custom_event('task_step')"]
    StepEmitter -->|SSE 实时流| SSEOut["前端子任务进度面板 (Task Cards)"]

    SubagentRuntime -->|收集 Token 消耗| Collector["SubagentTokenCollector<br/>统计子任务 Token 花费"]

    SubagentRuntime -->|执行结束| FormatResult["format_subagent_result_message<br/>• 状态: completed / failed / loop_capped<br/>• 产出结果摘要与数字凭证"]

    FormatResult -->|封装为 ToolMessage| LeadResume["返回 Lead Agent<br/>继续主会话推理"]
            </div>
          </div>
        </div>

        <!-- Code Block 5: task_tool & SubagentExecutor -->
        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：task_tool 工具定义 (backend/packages/harness/deerflow/tools/builtins/task_tool.py)</div>
          <details class="code-details" open>
            <summary>查看核心源码 (task_tool.py)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/tools/builtins/task_tool.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_task_tool)}</code></pre>
              </div>
            </div>
          </details>
        </div>

        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：SubagentExecutor 执行引擎 (backend/packages/harness/deerflow/subagents/executor.py)</div>
          <details class="code-details">
            <summary>查看核心源码 (SubagentExecutor)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/subagents/executor.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_subagent_executor)}</code></pre>
              </div>
            </div>
          </details>
        </div>
      </section>

      <!-- SECTION 6: 沙箱/记忆/MCP核心子系统 -->
      <section id="core-subsystems" class="doc-section">
        <div class="section-header">
          <div class="section-title-wrapper">
            <div class="section-icon"><i class="fa-solid fa-cubes"></i></div>
            <h2 class="section-title">6. 核心子系统：沙箱隔离、DeerMem 记忆与 MCP/Skills</h2>
          </div>
        </div>

        <p class="section-desc">
          DeerFlow 的生产就绪能力建立在三大基础设施子系统之上：虚拟路径安全沙箱、跨会话长期记忆提取（DeerMem）、以及支持动态 Slash 激活的 Skills 与 MCP 协议。
        </p>

        <!-- Subsystem Cards Grid -->
        <div class="step-grid">
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-box-open" style="color: var(--accent-emerald);"></i></div>
            <div class="step-title">安全沙箱体系 (Sandbox)</div>
            <div class="step-desc">
              抽象 <code>SandboxProvider</code>，开发环境使用 <code>LocalSandbox</code>，生产环境使用 Docker 隔离的 <code>AioSandbox</code>。
              强制虚拟路径映射 (<code>/mnt/user-data/workspace</code>) 与有界管道输出截断。
            </div>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-brain" style="color: var(--accent-purple);"></i></div>
            <div class="step-title">DeerMem 长期记忆</div>
            <div class="step-desc">
              无损提取用户偏好、身份、决策、修正等信号。通过异步防抖队列驱动后台 LLM 完成事实合并与时效性审查，持久化为 Markdown 并在会话首部安全注入。
            </div>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-wand-magic-sparkles" style="color: var(--accent-amber);"></i></div>
            <div class="step-title">Skills & MCP 扩展</div>
            <div class="step-desc">
              <code>SKILL.md</code> 渐进式披露：仅暴露元数据，用户通过 <code>/skill-name</code> 显式激活时完整加载。支持 Stdio/SSE 协议 MCP 服务器与延迟工具动态 Promoted。
            </div>
          </div>
        </div>

        <!-- Code Block 6: LocalSandbox & DeerMem -->
        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：LocalSandbox 安全路径转换与命令执行 (backend/packages/harness/deerflow/sandbox/local/local_sandbox.py)</div>
          <details class="code-details" open>
            <summary>查看核心源码 (LocalSandbox.execute_command)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/sandbox/local/local_sandbox.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_local_sandbox)}</code></pre>
              </div>
            </div>
          </details>
        </div>

        <div class="card">
          <div class="card-title"><i class="fa-solid fa-code" style="color: var(--accent-cyan);"></i> 核心代码实现：DeerMem 记忆事实提取与防抖队列 (backend/packages/harness/deerflow/agents/memory/backends/deermem/deer_mem.py)</div>
          <details class="code-details">
            <summary>查看核心源码 (DeerMem)</summary>
            <div class="code-box">
              <div class="code-header">
                <span class="code-path"><i class="fa-brands fa-python"></i> backend/packages/harness/deerflow/agents/memory/backends/deermem/deer_mem.py</span>
                <div class="code-actions">
                  <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> 复制代码</button>
                </div>
              </div>
              <div class="code-content">
                <pre class="line-numbers"><code class="language-python">{escape_code(code_deer_mem)}</code></pre>
              </div>
            </div>
          </details>
        </div>
      </section>

    </main>
  </div>

  <!-- Page Footer -->
  <footer class="page-footer">
    <div>🦌 DeerFlow 2.0 Super Agent Harness &bull; 核心代码架构全景与执行流程图</div>
    <div style="margin-top: 0.5rem; font-size: 0.75rem; color: var(--text-muted);">
      基于真实仓库代码构建 &bull; 涵盖 Lead Agent, 14+ Middlewares, Subagents, Sandbox, DeerMem & MCP Engine
    </div>
  </footer>

  <!-- Scripts -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>

  <script>
    // Initialize Mermaid
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'dark',
      themeVariables: {{
        primaryColor: '#1e3a8a',
        primaryTextColor: '#f3f4f6',
        primaryBorderColor: '#3b82f6',
        lineColor: '#60a5fa',
        secondaryColor: '#312e81',
        tertiaryColor: '#111827',
        fontFamily: 'Inter, sans-serif'
      }},
      flowchart: {{
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis'
      }}
    }});

    // Theme Toggle
    function toggleTheme() {{
      const body = document.body;
      const currentTheme = body.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      body.setAttribute('data-theme', newTheme);
      
      const themeIcon = document.getElementById('themeIcon');
      const themeText = document.getElementById('themeText');
      const prismTheme = document.getElementById('prism-theme');

      if (newTheme === 'light') {{
        themeIcon.className = 'fa-solid fa-sun';
        themeText.innerText = '暗黑模式';
        prismTheme.href = 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css';
      }} else {{
        themeIcon.className = 'fa-solid fa-moon';
        themeText.innerText = '明亮模式';
        prismTheme.href = 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css';
      }}
    }}

    // Diagram Zoom & Pan
    const diagramScales = new WeakMap();

    function zoomDiagram(btn, factor) {{
      const container = btn.closest('.diagram-container');
      const wrapper = container.querySelector('.mermaid-wrapper');
      let currentScale = diagramScales.get(wrapper) || 1.0;
      currentScale = Math.min(Math.max(currentScale * factor, 0.4), 2.5);
      diagramScales.set(wrapper, currentScale);
      wrapper.style.transform = `scale(${{currentScale}})`;
    }}

    function resetDiagram(btn) {{
      const container = btn.closest('.diagram-container');
      const wrapper = container.querySelector('.mermaid-wrapper');
      diagramScales.set(wrapper, 1.0);
      wrapper.style.transform = 'scale(1)';
    }}

    // Copy Code Handler
    function copyCode(btn) {{
      const codeBlock = btn.closest('.code-box').querySelector('code');
      const text = codeBlock.innerText;
      navigator.clipboard.writeText(text).then(() => {{
        const original = btn.innerHTML;
        btn.innerHTML = '<i class="fa-solid fa-check" style="color: #10b981;"></i> 已复制!';
        btn.style.borderColor = '#10b981';
        setTimeout(() => {{
          btn.innerHTML = original;
          btn.style.borderColor = '';
        }}, 2000);
      }}).catch(err => {{
        console.error('复制失败:', err);
      }});
    }}

    // Sidebar Active State on Scroll
    window.addEventListener('scroll', () => {{
      const sections = document.querySelectorAll('section.doc-section');
      const scrollPos = window.scrollY + 120;
      
      sections.forEach(section => {{
        const top = section.offsetTop;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');
        
        if (scrollPos >= top && scrollPos < top + height) {{
          document.querySelectorAll('.sidebar .nav-item').forEach(item => {{
            item.classList.remove('active');
            const link = item.querySelector('a');
            if (link && link.getAttribute('href') === '#' + id) {{
              item.classList.add('active');
            }}
          }});
        }}
      }});
    }});

    // Search Filter
    function handleSearch(query) {{
      const term = query.toLowerCase().trim();
      const cards = document.querySelectorAll('.card, .step-card, section.doc-section');
      
      if (!term) {{
        cards.forEach(c => c.style.display = '');
        return;
      }}
      
      cards.forEach(card => {{
        const text = card.innerText.toLowerCase();
        if (text.includes(term)) {{
          card.style.display = '';
        }} else {{
          if (card.tagName === 'SECTION') {{
            const hasMatchInside = card.querySelectorAll('.card, .step-card');
            let anyMatch = false;
            hasMatchInside.forEach(inner => {{
              if (inner.innerText.toLowerCase().includes(term)) anyMatch = true;
            }});
            card.style.display = anyMatch ? '' : 'none';
          }} else {{
            card.style.display = 'none';
          }}
        }}
      }});
    }}
  </script>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {output_file} ({os.path.getsize(output_file)} bytes)")
