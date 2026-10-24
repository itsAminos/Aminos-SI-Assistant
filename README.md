# 🤖 Aminos-SI-Assistant

> **A lean, asynchronous Telegram AI assistant built with Python and FastAPI, featuring agentic tool calling and a $0-cost LLM stack.**

## 🎯 Project Overview

**Aminos-SI-Assistant** is a production-grade personal Telegram AI agent. Built from scratch to master advanced Python engineering, it serves as a portfolio backend project demonstrating:
- Asynchronous Python (FastAPI & Aiogram 3.x)
- Event-driven webhook architecture
- Relational database memory (async SQLAlchemy 2.0 & Alembic)
- Autonomous Agentic AI workflows (Tool Calling via OpenRouter/Groq)

## 🛣️ Development Roadmap

This project is being built progressively using a feature-driven approach:
- [x] **Phase 1:** Python Fundamentals, Git, & Environment (uv/ruff)
- [ ] **Phase 2:** Object-Oriented Python & Pydantic Data Validation
- [ ] **Phase 3:** Asynchronous Programming & Bot Basics (Aiogram)
- [ ] **Phase 4:** Web APIs & Event-Driven Architecture (FastAPI)
- [ ] **Phase 5:** Relational Databases & Async ORMs
- [ ] **Phase 6:** Concurrency Control & Security 
- [ ] **Phase 7:** AI Integration & Telemetry
- [ ] **Phase 8:** Advanced AI Engineering (Agent Tool Calling)
- [ ] **Phase 9:** Automated Testing & Docker Containerization

## 🚀 Getting Started (Phase 1)

### Prerequisites
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (Extremely fast Python package installer and resolver)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Aminos-SI-Assistant.git
   cd Aminos-SI-Assistant
   ```

2. **Initialize the virtual environment & install dependencies:**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install ruff
   ```

3. **Format code:**
   ```bash
   ruff format .
   ```
