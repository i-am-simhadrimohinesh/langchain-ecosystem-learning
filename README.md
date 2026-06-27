# 🚀 LangChain Ecosystem Learning

A focused repository for learning **LangChain** with hands-on examples, experiments, and Jupyter notebooks.

---

## 📚 Official Documentation

### LangChain Core Documentation

* [LangChain Overview](https://docs.langchain.com/oss/python/langchain/overview) – Introduction to LangChain concepts, architecture, and core features.
* [LangChain Python Reference](https://reference.langchain.com/python/langchain) – Official API reference for LangChain in Python.

### LangChain Integrations

* [Google Generative AI Integration](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai) – Using Google Gemini models with LangChain.

### LangChain Models

* [Supported Models in LangChain](https://docs.langchain.com/oss/python/langchain/models) – List of available LLM integrations and model configurations.

### Google Gemini Models

* [Gemini Model Documentation](https://ai.google.dev/gemini-api/docs/models) – Official list of Google Gemini models and capabilities.

### Python Official Documentation

* [Python Documentation](https://docs.python.org/3/) – Official Python language reference, standard library, and tutorials.

---

## 🛠️ Project Setup

### ⚠️ Before You Start

Always use a **virtual environment** for this project before installing dependencies, running code, or starting Jupyter.

---

### Create Virtual Environment

```bash
python -m venv .venv
```

---

### Activate Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

---

## 📦 Install Dependencies

After activating the virtual environment:

```bash
pip install -r requirements.txt
```

---

## 📓 Jupyter with Virtual Environment

### Install Kernel Support

Inside the activated virtual environment, install:

```bash
pip install ipykernel
```

---

### Register Virtual Environment as Jupyter Kernel

After activation, register the environment:

```bash
python -m ipykernel install --user --name=langchain-env --display-name "Python (langchain-env)"
```

Then open Jupyter Notebook or JupyterLab and select:

```
Python (langchain-env)
```

---

## ✅ Verify Environment Setup

### Check Python Version

```bash
python --version
```

---

### Check Active Python Path

```bash
python -c "import sys; print(sys.executable)"
```

---

### Inside Jupyter Notebook

```python
import sys

print(sys.executable)
```

If the path points to `.venv`, then the correct virtual environment is active.

---

## 🎯 Best Practices

* Use a separate `.venv` for each project
* Install all dependencies inside the virtual environment
* Select the correct Jupyter kernel before running notebooks
* Keep `requirements.txt` updated
* Avoid installing packages globally
* Refer to official documentation for latest updates and changes

---

🚀 Happy Learning
