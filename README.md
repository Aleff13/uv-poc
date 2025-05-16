# 🧪 UV Test Project

This repository is a minimal Python project created to test and experiment with [**UV**](https://docs.astral.sh/uv/), an extremely fast Python package installer and resolver built by [Astral](https://astral.sh).

---

## 🔧 What is UV?

[UV](https://docs.astral.sh/uv/) is a drop-in replacement for `pip`, `virtualenv`, and `pip-tools`, written in Rust. It's designed for **speed**, **reproducibility**, and **ease of use**, supporting workflows based on `pyproject.toml`.

---

## 📁 Project Structure

```
uv-test/
├── pyproject.toml
├── README.md
└── src/
    └── app.py
```

---

## 🚀 Getting Started with UV

### 1. Install UV

Follow the official installation guide: https://docs.astral.sh/uv/installation/

Or install via shell script:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Make sure `uv` is available in your `PATH`.

---

### 2. Set Up the Virtual Environment

Create a `.venv` using UV:

```bash
uv venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

If using `pyproject.toml`:

```bash
uv pip install .
```

Or if using a `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

---

### 4. Run the App

```bash
python src/app.py
```

---

## ✅ What This Project Tests

- Speed and reliability of `uv pip install`
- `uv venv` compared to `python -m venv` or `virtualenv`
- Dependency resolution using `pyproject.toml`
- Compatibility with existing Python tooling

---

## 📝 Example `pyproject.toml`

```toml
[project]
name = "uv-test"
version = "0.1.0"
description = "Minimal project to test the UV Python tool"
authors = [{ name = "Your Name", email = "you@example.com" }]
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests"
]

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

---

## 📚 Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub Repository](https://github.com/astral-sh/uv)
- [PEP 621 - `pyproject.toml` Project Metadata](https://peps.python.org/pep-0621/)

---

## 📄 License

This project is licensed under the MIT License.

## Start locally

build docker image

```bash
docker build -t uv-poc .
```

run container

```bash
docker run -p 8000:80 uv-poc
```
