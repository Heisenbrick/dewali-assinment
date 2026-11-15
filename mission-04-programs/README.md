# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 was to write and execute a simple Python program (`hello.py`) from the terminal, observe program execution output, and conduct a comparative analysis between **compilers** and **interpreters**.

## 2. Work completed
- Created `mission-04-programs/hello.py` containing a single print statement.
- Executed `hello.py` using the Python interpreter from the terminal and verified its printed output.
- Analyzed the translation mechanisms, advantages, and tradeoffs of compiled versus interpreted execution models.
- Documented findings and comparison tables in `mission-04-programs/README.md`.

## 3. Commands / tools used
- Python 3 interpreter: Executed `hello.py` via `python hello.py`.
- VS Code / Text Editor: Authored the Python program.

## 4. My understanding

### Task 4.1 — Create and Run a Python Program
Inside `mission-04-programs/hello.py`:
```python
print("Hello from Python")
```

**Observed Terminal Output:**
```text
Hello from Python
```
The Python interpreter loaded `hello.py`, parsed the source code into an Abstract Syntax Tree (AST), compiled it into bytecode, and executed the instructions inside the Python Virtual Machine (PVM), streaming the string to standard output (`stdout`).

---

### Task 4.2 — Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translation happens **ahead-of-time (AOT)** before program runtime. The entire source code is translated in one batch. | Translation happens **at runtime**, reading, translating, and executing instructions sequentially as the program runs. |
| **Typical output** | A standalone executable binary file in machine code (`.exe` on Windows, binary executable on Linux/macOS). | Immediate runtime execution results; optionally produces intermediate bytecode files (e.g. `.pyc`). |
| **One example** | C (`gcc`), C++ (`g++`), Rust (`rustc`), Go. | Python (`cpython`), JavaScript (Node.js/V8), Ruby, PHP. |
| **One advantage** | Maximum runtime execution speed and performance; catches syntax and type errors before deployment. | Platform independence (runs on any system with the runtime) and rapid, interactive prototyping without a compile step. |

### Explanation of Differences
A **compiler** translates high-level human-readable source code into native machine code instructions in an ahead-of-time step before the program is ever executed. This creates a self-contained executable binary that runs at maximum speed directly on the host CPU, though the build process takes time and the binary is tied to a specific hardware architecture. 

In contrast, an **interpreter** analyzes and carries out source code instructions on the fly during runtime, line-by-line or through an intermediate virtual machine bytecode layer. While interpreted languages incur a slight performance overhead during execution, they offer immediate feedback, interactive debugging, and write-once-run-anywhere flexibility across different operating systems.

## 5. Difficulties faced
No major difficulties. Running Python scripts requires ensuring the correct interpreter binary is referenced in the environment.

## 6. How I resolved them
Verified the active Python path and executed `hello.py` cleanly.

## 7. Evidence / files
- Python program: `mission-04-programs/hello.py`
- Mission documentation: `mission-04-programs/README.md`
- Evidence log: `evidence/hello_run_output.txt`

## 8. Commit details
- **Commit Message**: `Compare compilers and interpreters`
- **Confirmation**: Program and documentation staged and committed to branch `main`.
