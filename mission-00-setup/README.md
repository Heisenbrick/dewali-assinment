# Mission 0 — Repository and workspace setup

## 1. Task / objective
The objective of Mission 0 was to establish a structured, version-controlled workspace for the Digital Detective assignment. This required verifying the local development environment (Python 3 and Git installations), establishing a uniform project directory hierarchy with dedicated mission subfolders, initializing a Git repository with a standardized naming convention based on student USN (`digital-detective-1234`), and publishing the initial workspace structure.

## 2. Work completed
- Verified system installation and operational versions of Python 3 (`Python 3.14.6`) and Git (`git version 2.54.0.windows.1`).
- Initialized a local Git repository with `main` as the default branch.
- Created the standardized mission folder structure:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`
- Authored the comprehensive root `README.md` providing an overview, student details table, mission index, and topic catalog.
- Prepared initial placeholder files including `mission-04-programs/hello.py` and `mission-05-numbers-data/number_converter.py`.

## 3. Commands / tools used
- `git --version`: Displayed the installed Git binary version.
- `python --version` / `uv run python --version`: Displayed the active Python interpreter version.
- `git init -b main`: Initialized a new local Git repository with the `main` branch.
- `git config user.name "Heisenbrick"`: Configured the local Git commit author name.
- `git config user.email "ayushxmahato@gmail.com"`: Configured the local Git commit email.
- `mkdir` / `New-Item`: Created the required folder hierarchy across all missions.

## 4. My understanding
A **Git repository** is a structured, version-controlled database that tracks the chronological history of changes made to files within a project. Unlike simple cloud storage or backup folders, a repository records who made each change, when it occurred, and why, allowing developers to revert mistakes, compare states, and collaborate seamlessly.

Organizing the project into separate mission folders establishes clear separation of concerns. Each mission focuses on a distinct architectural layer of computing (hardware, terminal, OS, programming, data, version control, networking). Having an individual `README.md` in every mission folder ensures that investigations, data tables, and evidence remain modular, legible, and easy for instructors and peers to evaluate.

## 5. Difficulties faced
When initially executing `python --version` in Windows PowerShell, the command resulted in an application execution alias redirect error (`Program 'python.exe' failed to run: The file cannot be accessed by the system`). This occurred because the Windows Store execution alias was taking precedence in `PATH` over installed Python runtimes.

## 6. How I resolved them
I located the active Python installation managed on the system under `uv` (`C:\Users\ayush\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\python.exe`) and confirmed that `Python 3.14.6` was fully functional. Commands were executed using this verified Python runtime.

## 7. Evidence / files
- Root directory index: `README.md`
- Mission documentation: `mission-00-setup/README.md`
- Evidence log: `evidence/env_check.txt`

## 8. Commit details
- **Commit Message**: `Set up Digital Detective mission structure`
- **Confirmation**: All workspace folders, root README, and Mission 0 documentation staged and committed to branch `main`.
