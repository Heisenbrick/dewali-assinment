# DIWALI INDEPENDENT LEARNING ASSIGNMENT: THE DIGITAL DETECTIVE
> *Explore Your Computer • Build a Mini System Report*

## Student Information

| Field | Details |
| :--- | :--- |
| **Name** | Ayush Kumar Mahato |
| **USN** | [Redacted for privacy] |
| **Campus / Section** | Computer Science and Engineering |
| **GitHub Username** | Heisenbrick |
| **GitHub Repository Name** | dewali-assinment |
| **GitHub Repository URL** | https://github.com/Heisenbrick/dewali-assinment |

---

## Project Overview

**The Digital Detective** is an independent, practical investigation into the foundational layers of modern computer systems. Through a sequential series of nine structured missions, this project bridges theoretical computer science fundamentals with real-world, hands-on command-line operations, operating system investigations, data encoding mechanics, and distributed version control using Git and GitHub.

Every mission is self-contained within its own dedicated directory, thoroughly documented using a uniform analytical structure, and committed to version control in strict sequential order.

---

## Mission Index

| Mission | Focus Area | Status | Folder / Documentation Link |
| :---: | :--- | :---: | :--- |
| **0** | Repository and workspace setup | Complete | [mission-00-setup/README.md](mission-00-setup/README.md) |
| **1** | Computer fundamentals and IPOS | Complete | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) |
| **2** | Terminal and file management | Complete | [mission-02-terminal/README.md](mission-02-terminal/README.md) |
| **3** | Operating system, processes and permissions | Complete | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) |
| **4** | How programs run (Compiler vs Interpreter) | Complete | [mission-04-programs/README.md](mission-04-programs/README.md) |
| **5** | Number systems, Python and text encoding | Complete | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) |
| **6** | Git, GitHub, branches and Pull Requests | Complete | [mission-06-git-github/README.md](mission-06-git-github/README.md) |
| **7** | Computer networks and web communication | Complete | [mission-07-networking/README.md](mission-07-networking/README.md) |
| **8** | Final review and submission checklist | Complete | [mission-08-final-report/README.md](mission-08-final-report/README.md) |

---

## Topics Explored Across the Missions

1. **Hardware & The IPOS Cycle**: Mapping human interaction (input) to CPU/RAM computation (processing), persistent SSD block storage (storage), and display rendering (output).
2. **Command-Line Interface (CLI)**: Navigating directory trees, inspecting file metadata, manipulating files safely (`cp`, `mv`, `cat`), and harnessing UNIX pipes and flags.
3. **Operating System Architecture**: Inspecting system resource utilization, understanding the Process Control Block and Process Identifiers (PID), absolute vs. relative path resolution, and filesystem security/permissions (`rwx`).
4. **Program Execution Paradigms**: Comparing Ahead-Of-Time (AOT) compiled binaries with runtime-interpreted dynamic languages.
5. **Data Representation & Encoding**: Manual and programmatic conversions across Base-10 (Decimal), Base-2 (Binary), and Base-16 (Hexadecimal), alongside ASCII and UTF-8 text encoding.
6. **Distributed Version Control**: Repository initialization, staging index mechanics, atomic commits, feature branching, and collaborative Pull Request workflows.
7. **Networking & Internet Protocols**: Deconstructing LAN, MAN, WAN topologies, client-server architectures, packet switching, DNS name resolution, and the complete 7-step lifecycle of an HTTP/HTTPS web request.

---

## Instructions: Running the Number Converter

The Python number converter program is located in `mission-05-numbers-data/number_converter.py`. It accepts a positive decimal integer and outputs its exact Binary and Hexadecimal equivalents.

To execute the converter from your terminal:

```bash
# 1. Navigate into the mission-05 folder
cd mission-05-numbers-data

# 2. Run the script using Python 3
python number_converter.py
```

*Example session:*
```text
=============================================
   Digital Detective: Number Converter
=============================================
Enter a positive decimal integer: 42

--- Conversion Results ---
Decimal (Base 10)     : 42
Binary (Base 2)       : 0b101010  (Raw: 101010)
Hexadecimal (Base 16) : 0x2A  (Raw: 2A)
=============================================
```

---

## Summary of Key Learnings

Throughout this investigative assignment, I developed a grounded mental model of how computing machinery operates from low-level binary bit representations up to distributed network communications:
- I learned that the operating system acts as a protective mediator between software applications and physical silicon hardware, efficiently scheduling threads and guarding memory.
- I discovered how file paths, permission bits, and processes interact within the shell environment, and how pipeline composition allows small terminal utilities to perform complex data filters.
- I mastered numerical base conversions by hand through successive division and positional weight summation, validating them using Python.
- I gained practical experience with Git version control, learning to distinguish between working tree modifications, staged index snapshots, and commit records.

---

## Workflow and Privacy Notice

- **Sequential Commits**: Each mission was finished, verified, and committed with an independent, descriptive commit message in sequential order.
- **Privacy Compliance**: All personal identifiable information, including system usernames, hardware serial numbers, private IP addresses, and Wi-Fi SSIDs, has been sanitized or masked as `[redacted]` in all documentation and logs.

---

## My Learning

During the Digital Detective assignment, several foundational computing insights stood out:
1. **The Layered Computing Stack**: How user interactions trigger an interconnected chain of events from physical hardware interrupts (IPOS cycle) up through kernel process scheduling and display rendering.
2. **Deterministic Data Representations**: How diverse data types—from numerical integers in base-10, base-2, and base-16 to international characters in Unicode UTF-8—are represented systematically in binary bits.
3. **Professional Version Control Disciplines**: How Git feature branches and Pull Requests empower developers to make isolated, testable improvements without disrupting the stable `main` codebase.
