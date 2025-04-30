# Project Directory Tree Viewer

This repository contains a simple yet effective Python script (`tree.py`) that generates a clean, recursive view of your project’s directory structure—excluding clutter from IDEs, virtual environments, and cache folders.

## ✨ Features

- Starts from the current working directory
- Recursively displays all relevant files and folders
- Skips common clutter like:
  - `.idea/`
  - `.venv/`
  - `__pycache__/`
  - `.pytest_cache/`

## 🛠 Requirements

- Python 3.6 or higher

## 🚀 Quick Start

1. Clone or download this repository to your local machine.
2. Open a terminal in the root of your project directory.
3. Run the script:

```bash
python tree.py
```

## 📁 Example Output

```
project/
├── src/
│   └── main.py
├── data/
│   └── sample.csv
└── README.md
```

> Note: The output will vary depending on the structure of your current working directory.

## 🧹 Automatically Skipped Directories

To keep the output clean, the following directories are ignored:
- `.idea/`
- `.venv/`
- `__pycache__/`
- `.pytest_cache/`
