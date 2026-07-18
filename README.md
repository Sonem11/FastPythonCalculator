# Fast Python Calculator

A simple and fast calculator written in Python.  
It supports basic operations: addition, subtraction, multiplication, division, power, and square root.

## Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/), with error handling for division by zero
- Power (^), e.g., 2 ^ 3 = 8
- Square root (sqrt), e.g., sqrt(16) = 4

## Project Structure
FastPythonCalculator/
│
├── calculator.py      # Main Python script
├── README.md          # Project documentation
├── requirements.txt   # Dependencies
└── .gitignore         # Ignored files for Git

Code

## How to Run
1. Open **Command Prompt (CMD)** and navigate to the project folder:
   ```bash
   cd C:\PythonProjekti\BeginnerProjects\FastPythonCalculator
Run the calculator:

bash
python calculator.py
Example
Code
Enter the first number: 9
Enter the second number: 2
Choose operation (+, -, *, /, ^, sqrt): sqrt
Result: 3.0
Requirements
Python 3.10 or higher

Standard Python library (math) is used for square root

Future Improvements
Add support for more advanced math functions (logarithms, trigonometry)

Create a graphical user interface (GUI)

Add unit tests for reliability

Code

---

## 📄 requirements.txt
```txt
# Standard Python library only
# No external dependencies required
📄 .gitignore
txt
# Ignore Python cache and temporary files
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore virtual environments
venv/
env/

# Ignore IDE/editor settings
.vscode/
.idea/

# Ignore OS files
.DS_Store
Thumbs.db