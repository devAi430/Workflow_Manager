<!-- Canopus Work Manager README -->

<h1 align="center">⚙️ Canopus Work Manager</h1>

<p align="center">
  <b>Fast & Flexible Multi-Agent Automation Framework</b><br>
  <i>Python | Crews & Flows | High-Performance Automation</i>
</p>

<p align="center">
  <a href="https://pypi.org/project/canopus-work-manager/"><img src="https://img.shields.io/pypi/v/canopus-work-manager.svg?color=blue" alt="PyPI Version"></a>
  <a href="https://github.com/canopusai/work-manager/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-yellow.svg" alt="Python Version"></a>
  <a href="https://github.com/canopusai/work-manager/stargazers"><img src="https://img.shields.io/github/stars/canopusai/work-manager?style=social" alt="GitHub Stars"></a>
</p>

---

<p align="center">
  <img src="https://raw.githubusercontent.com/canopusai/work-manager/main/assets/banner.png" alt="Canopus Work Manager Banner" width="90%">
</p>

---

## 📘 Overview
**Canopus Work Manager** is a **lightweight, high-performance Python framework** engineered from the ground up — completely independent of LangChain or other agent frameworks.

It enables developers and enterprises to build **autonomous AI agents** and **collaborative automation systems** that can think, decide, and execute complex workflows with both **speed and precision**.

**Core Paradigms:**
- 🤖 **Crews** → Teams of AI agents collaborating autonomously toward shared goals.
- 🔄 **Flows** → Event-driven, deterministic process controllers ensuring reliable, rule-based execution.

Together, they empower organizations to create **scalable, intelligent automation systems** blending autonomy with control.

---

## 🚀 Key Features
- 🤖 **Autonomous AI Crews** — Multi-agent systems capable of collaborative reasoning.
- ⚡ **Lightning-Fast Execution** — Built purely in Python for optimal performance.
- 🔄 **Flows for Precision Control** — Event-driven workflows with condition handling.
- 🧠 **Full Customization** — Tailor workflows, prompts, and logic from high to low levels.
- 🔒 **Enterprise-Ready Security** — Integrated observability and compliance.
- 🌐 **Seamless Integration** — Connect easily with APIs, databases, or enterprise systems.
- 👥 **Developer Ecosystem** — 100K+ certified developers and growing community.

---

<details>
<summary><b>🏗️ Project Architecture</b></summary>

**Workflow Lifecycle:**  
Developer → Define Agents & Tasks → Configure YAML → Build Crew → Execute Flow → Monitor & Scale  

**Core Components:**
```bash
my_project/
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── main.py           → Entry point for your crew or flow
        ├── crew.py           → Crew and task orchestration logic
        ├── config/
        │   ├── agents.yaml   → Define agent roles, goals, and behaviors
        │   └── tasks.yaml    → Define task descriptions and outcomes
        └── tools/            → Custom tool definitions for agent use
```
</details>

---

## ⚙️ Installation & Setup

### 1️⃣ Install Canopus Work Manager
```bash
pip install canopus-work-manager
```

Include optional tools and embeddings:
```bash
pip install 'canopus-work-manager[tools]'
```

### 2️⃣ Verify Dependencies
Requires **Python ≥ 3.10 and < 3.14**.
If `tiktoken` or related dependencies fail:
```bash
pip install 'canopus-work-manager[embeddings]'
```

### 3️⃣ Create a New Project
```bash
canopus create crew my_project
cd my_project
```

### 4️⃣ Configure Agents & Tasks
Edit:
- `config/agents.yaml` — Define agent roles, goals, and personalities.
- `config/tasks.yaml` — Define task logic, inputs, and outputs.

### 5️⃣ Run Your Crew or Flow
```bash
canopus run
```
Or via Python:
```bash
python src/my_project/main.py
```

**Environment Variables:**
```
OPENAI_API_KEY=sk-xxxx
SERPER_API_KEY=your_serper_key
```

---

## 🧱 Canopus AMP Suite
The **Canopus AMP Suite** extends the framework into an enterprise-grade automation platform, combining **security**, **observability**, and **scalability**.

### 💼 Key Modules
- 📊 **Tracing & Observability** — Real-time monitoring with logs and traces.
- 🧭 **Unified Control Plane** — Manage workflows from a central dashboard.
- 🔐 **Advanced Security** — Encryption, auditing, and compliance.
- ☁️ **Flexible Deployment** — Cloud or on-premise options.
- 📈 **Analytics Dashboard** — Visualize performance and collaboration.
- 🛠️ **Integrations** — Connect with APIs, tools, and enterprise systems.
- 💬 **24/7 Enterprise Support** — Dedicated expert assistance.

**Try the Canopus Control Plane for free** — experience live observability and tracing.

---

## 🧠 Use Cases
- Multi-Agent AI Automation
- Intelligent Workflow Orchestration
- Research & Data Analysis Systems
- Document Processing & Summarization
- Business Process Automation
- AI-Driven Planning & Reporting Tools

---

## 🧪 Example Projects
Explore real-world examples built using **Canopus Work Manager**:
- 🏝️ **Trip Planner** — Autonomous multi-agent travel coordination.
- 📈 **Stock Analysis** — Automated market intelligence and reporting.
- 🧱 **Landing Page Generator** — Collaborative content creation.
- 🤝 **Human-in-the-Loop Agents** — Hybrid AI + human decision pipelines.

---

## 🤝 Contributing
We welcome community contributions!
1. Fork the repository.
2. Create a branch (`git checkout -b feature-name`).
3. Commit and submit a pull request.

Ensure all contributions are **documented and tested**.

---

## 📜 License
**Canopus Work Manager** is released under the **MIT License** — freely usable, modifiable, and distributable with attribution.

---

## 💡 Summary
**Canopus Work Manager** bridges the gap between **autonomous AI collaboration** and **precise workflow management**, giving developers a **powerful, modular, and production-ready automation toolkit**.

From **simple orchestrations** to **enterprise-scale intelligent systems**, it provides the **speed, flexibility, and control** required to build the future of AI-driven workflows.

<p align="center"><b>✨ Build smarter workflows — faster — with Canopus Work Manager ✨</b></p>
