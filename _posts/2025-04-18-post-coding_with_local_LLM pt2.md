---
title: "LMQuickBench: Building, Testing, and Publishing a Local LLM Benchmarking Tool"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - LLM
  - Benchmarking
  - Python
  - Open Source
  - Productivity Tools
  - LM Studio
---

# LMQuickBench: Building, Testing, and Publishing a Local LLM Benchmarking Tool

[![PyPI version](https://badge.fury.io/py/lmquickbench.svg)](https://badge.fury.io/py/lmquickbench)

---

## 🧠 Introduction

When I started experimenting with running Large Language Models (LLMs) locally through [LM Studio](https://lmstudio.ai/), I realized there was a missing piece:  
**An easy, lightweight way to benchmark model performance.**

I wanted a tool that could quickly measure:
- Response **latency**
- **Token usage**
- **Tokens per second** output speed

So I decided to build it myself — **LMQuickBench**.

Today, I'm excited to share that LMQuickBench is live on [PyPI](https://pypi.org/project/lmquickbench/), and anyone can install it with:

```bash
pip install lmquickbench
```

---

## 💬 Why Build LMQuickBench?

While LM Studio offers local LLM hosting with a nice UI,  
there was **no simple way to batch test prompts and measure generation speed directly**.

Pain points I wanted to solve:
- See how different models perform (e.g., Qwen, DeepSeek)
- Test on both short prompts and complex coding tasks
- Get standardized, easy-to-compare metrics

---

## 🛠️ How I Built It

- Developed a Python CLI tool using `requests` to connect to LM Studio’s local server API
- Designed CLI arguments: `--prompt`, `--promptfile`, `--max_tokens`, `--server_url`
- Packaged it into a clean project structure (`setup.py`, `pyproject.toml`)
- Made it pip-installable
- Set up GitHub Actions for automatic testing on every push and PR

**Key decision:**  
Allow flexible server URL input (`--server_url`) so LMQuickBench is **future-proof** for different deployment scenarios.

---

## ✨ Key Features

| Feature | Description |
|:---|:---|
| Single prompt or batch benchmarking | Flexible testing |
| Dynamic server URL | Connect to any compatible LLM server |
| Lightweight | Only depends on `requests` |
| Expandable | CSV output and dashboard planned |

---

## 📦 Publishing to PyPI

After local testing was successful,  
I built distribution packages and uploaded LMQuickBench to [PyPI](https://pypi.org/project/lmquickbench/).

It was an exciting milestone:
- ✅ My first pip-installable open-source project
- ✅ Publicly available for anyone to use worldwide

Now, installing LMQuickBench is as easy as:

```bash
pip install lmquickbench
```

---

## 🚀 Quick Demo

Benchmark a simple prompt:

```bash
lmquickbench --prompt "Explain recursion in computer science." --max_tokens 512
```

Batch test a file of coding prompts:

```bash
lmquickbench --promptfile prompts/prompts_coding.txt --max_tokens 512
```

**Example output:**

```
Testing prompt: Explain recursion.
Model: qwen2.5-coder-14b-instruct, Latency: 4.56 sec, Tokens: 133, Tokens/sec: 29.14
Output: Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem...
```

---

## 🔥 Future Plans

- CSV/JSON export of benchmarking results
- Streamlit dashboard visualization
- System resource (CPU, RAM) monitoring
- Auto-scaling prompt generation for stress testing

---

## 🎯 Conclusion

Building LMQuickBench taught me a lot:
- Structuring a real Python CLI project
- Pip packaging and PyPI publishing
- Setting up GitHub CI/CD workflows
- Turning ideas into production-ready tools

This is just the beginning.  
Feel free to try LMQuickBench — feedback and contributions are welcome!

👉 GitHub Repo: [https://github.com/gordonyfg/LMQuickBench](https://github.com/gordonyfg/LMQuickBench)

👉 PyPI Install:

```bash
pip install lmquickbench
```

---

**Let's keep pushing the boundaries of local LLM capabilities together 🚀.**