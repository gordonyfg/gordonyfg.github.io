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


<!--more-->

## Why Build LMQuickBench?

While tools like [LM Studio](https://lmstudio.ai/) make it easy to run LLMs locally, I wanted to measure and compare model performance. I wanted a tool that could:

- Quickly measure **response latency**
- Track **token usage**
- Calculate **tokens per second** output speed
- Test both short prompts and complex coding tasks

With these goals in mind, I created **LMQuickBench**, now available on [PyPI](https://pypi.org/project/lmquickbench/). You can install it with:

```bash
pip install lmquickbench
```

---

## How I Built LMQuickBench

Building LMQuickBench was a rewarding experience. Here’s how I approached it:

1. **Python CLI Tool**: I used Python and the `requests` library to interact with LM Studio’s local server API.
2. **Flexible CLI Arguments**: I added options like `--prompt`, `--promptfile`, `--max_tokens`, and `--server_url` for flexibility.
3. **Clean Project Structure**: I structured the project with `setup.py` and `pyproject.toml` for easy packaging.
4. **PyPI Publishing**: I packaged the tool and published it to PyPI for public use.
5. **GitHub Actions**: I set up CI/CD workflows to automatically test the tool on every push and pull request.

One key decision was to allow a dynamic server URL (`--server_url`) to make LMQuickBench future-proof for different deployment scenarios.

---

## Key Features

LMQuickBench is designed to be simple yet powerful. Here are its key features:

| Feature                     | Description                                      |
|-----------------------------|--------------------------------------------------|
| Single or batch benchmarking| Test individual prompts or batches of prompts.  |
| Dynamic server URL           | Connect to any compatible LLM server.           |
| Lightweight                 | Only depends on `requests`.                     |
| Expandable                  | CSV output and dashboard visualization planned. |

---

## Quick Demo

Here’s how you can use LMQuickBench to benchmark your local LLMs:

### Benchmark a Single Prompt

```bash
lmquickbench --prompt "Explain recursion in computer science." --max_tokens 512
```

### Batch Test Prompts from a File

```bash
lmquickbench --promptfile prompts/prompts_coding.txt --max_tokens 512
```

**Example Output:**

```
Testing prompt: Explain recursion.
Model: qwen2.5-coder-14b-instruct, Latency: 4.56 sec, Tokens: 133, Tokens/sec: 29.14
Output: Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem...
```

---

## Performance Comparison

To demonstrate LMQuickBench’s capabilities, I tested several models with different prompts. Below is a summary of the results:

| **Prompt**                                                                 | **Model**                      | **Latency (sec)** | **Tokens** | **Tokens/sec** | **Output Summary**                                                                                     |
|----------------------------------------------------------------------------|--------------------------------|-------------------|------------|----------------|-------------------------------------------------------------------------------------------------------|
| Write a Python function that checks whether a given string is a palindrome. | qwen2.5-coder-14b-instruct     | 2.95              | 58         | 19.68          | Provided a Python function to check if a string is a palindrome.                                    |
| Write a Python class called Stack that implements push, pop, and peek operations. | qwen2.5-coder-14b-instruct     | 7.53              | 300        | 39.87          | Provided a Python class `Stack` with `push`, `pop`, and `peek` methods.                              |
| Write a Python function to calculate the factorial of a number recursively. | qwen2.5-coder-14b-instruct     | 7.52              | 297        | 39.51          | Provided a recursive Python function to calculate the factorial of a number.                         |
| Write a Python function that reverses a given string.                      | qwen2.5-coder-14b-instruct     | 4.46              | 148        | 33.21          | Provided a Python function to reverse a string using slicing.                                        |
| Write a Python function that sums all elements in a list.                  | qwen2.5-coder-14b-instruct     | 5.83              | 215        | 36.86          | Provided a Python function to sum all elements in a list using `sum()`.                              |

### Summary:

- **Average Latency**: 6.57 sec
- **Average Tokens/sec**: 36.91

This table highlights how LMQuickBench can provide clear, actionable insights into model performance.

---

## Publishing to PyPI

Publishing LMQuickBench to [PyPI](https://pypi.org/project/lmquickbench/) was a major milestone for me. It’s my first pip-installable open-source project, and it’s now publicly available for anyone to use.

To install LMQuickBench, simply run:

```bash
pip install lmquickbench
```

---

## Future Plans

I’m excited about the future of LMQuickBench. Here are some features I’m planning to add:

- **CSV/JSON Export**: Save benchmarking results for further analysis.
- **Streamlit Dashboard**: Visualize results in an interactive dashboard.
- **System Monitoring**: Track CPU and RAM usage during benchmarking.
- **Stress Testing**: Auto-scale prompt generation to test model limits.

---

## Conclusion

Building LMQuickBench taught me a lot about structuring Python projects, publishing to PyPI, and setting up CI/CD workflows. It’s been a rewarding journey, and I’m thrilled to share this tool with the community.

If you’re running LLMs locally, give LMQuickBench a try! Feedback and contributions are always welcome.

👉 **GitHub Repo**: [https://github.com/gordonyfg/LMQuickBench](https://github.com/gordonyfg/LMQuickBench)  
👉 **PyPI Install**:

```bash
pip install lmquickbench
```

---

Let’s keep pushing the boundaries of local LLM capabilities together 🚀.