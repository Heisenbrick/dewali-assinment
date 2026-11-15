# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 was to examine fundamental computer architecture concepts, specifically the **IPOS** (Input, Processing, Output, Storage) cycle, classify primary hardware and software components, and analyze the function of everyday embedded computer systems beyond personal computers.

## 2. Work completed
- Deconstructed a daily digital task (authoring and running a Python script) into its four IPOS stages with associated hardware components.
- Compiled an analytical table of four hardware items and four software applications/utilities with their functional classifications.
- Investigated three real-world embedded computer systems (ATM, Smart TV, Automated Traffic Signal), identifying their primary purpose, inputs, and outputs.
- Documented findings in `mission-01-computer-basics/README.md`.

## 3. Commands / tools used
- Conceptual architectural analysis tools.
- Markdown text editor (VS Code) for authoring structured tabular documentation.

## 4. My understanding

### Task 1.1 — Trace One Activity Using IPOS
**Selected Activity**: *Writing, editing, and executing a Python script in a terminal editor*

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | The user types Python code instructions using the keyboard and clicks the terminal run button with the mouse. Keystrokes generate electrical scan codes that the OS interprets as character input. | Mechanical/Membrane Keyboard, Optical Mouse |
| **Processing** | The Central Processing Unit (CPU) fetches instructions, loads the Python interpreter into RAM, parses source code into bytecode, executes arithmetic/logical operations, and coordinates memory registers. | Multi-core CPU, System RAM (Memory) |
| **Output** | The terminal displays the printed results of the program (`stdout`) onto the screen. Error logs, UI elements, and graphical feedback are rendered visually. | LCD / OLED Display Monitor |
| **Storage** | The source code (`.py` file) and intermediate compiled bytecode (`.pyc`) are written into non-volatile storage blocks so they persist after power is turned off. | NVMe Solid-State Drive (SSD) / HDD |

*Explanation of Flow*: 
The activity begins at the **Input** stage, where physical key presses are converted by keyboard microcontrollers into binary interrupt signals sent to the OS. The OS transfers these inputs into active volatile memory (RAM). During **Processing**, the CPU executes the editor and interpreter processes, manipulating variables inside CPU cache and registers. When the user saves or executes, the data is pushed through system buses to **Storage** (persisted on disk blocks) and simultaneously routed to the GPU/display buffer as visual **Output** pixels on screen.

---

### Task 1.2 — Identify Hardware and Software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Mechanical Keyboard** | Hardware | Not applicable | Captures physical user keypresses and converts them to binary character scan codes for text input. |
| **Display Monitor** | Hardware | Not applicable | Converts frame buffer digital video signals into visual light matrices for user graphical output. |
| **Central Processing Unit (CPU)** | Hardware | Not applicable | Executes machine-level arithmetic, logical, and control instructions driving all system computations. |
| **NVMe Solid-State Drive (SSD)** | Hardware | Not applicable | Provides persistent, non-volatile block storage for operating system binaries, applications, and user files. |
| **Microsoft Windows 11** | Software | Operating system software | Controls hardware resources, manages process scheduling, mediates filesystem I/O, and enforces security boundaries. |
| **Visual Studio Code** | Software | Application software | Integrated development environment allowing users to author, syntax-highlight, and debug source code. |
| **Windows Defender Antivirus** | Software | Utility software | Continuously scans filesystem operations and running memory to identify and neutralize malicious threats. |
| **Git Version Control** | Software | Utility software | Tracks historical revisions across source code repositories and coordinates distributed multi-developer merges. |

---

### Task 1.3 — Computer Systems Around You

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Dispense cash, query bank accounts, and process financial deposits securely. | User PIN and transaction selections entered via the numeric keypad / touch display. | Banknote cash dispensing mechanism and printed transaction receipt. |
| **Smart TV** | Decode, render, and stream high-definition digital audio/video media over network connections. | Infrared / Bluetooth remote control commands or microphone voice queries. | High-resolution 4K display panel and integrated stereo speaker audio output. |
| **Automated Traffic Signal Controller** | Regulate intersection traffic flow safely and dynamically prevent collisions. | Inductive loop road sensors detecting vehicle electromagnetic presence. | Red, Amber, and Green high-intensity LED light signal arrays. |

## 5. Difficulties faced
No major difficulties. Differentiating between system utility software and application software required careful consideration of whether the tool serves the user's primary application goal (e.g. writing documents) or maintains system health/development pipelines (e.g. Git, antivirus).

## 6. How I resolved them
Referenced standard operating system taxonomy: utilities optimize, maintain, or secure computing workflows without being the end goal itself, whereas application software directly solves end-user productivity tasks.

## 7. Evidence / files
- Mission documentation: `mission-01-computer-basics/README.md`

## 8. Commit details
- **Commit Message**: `Complete computer basics and IPOS mission`
- **Confirmation**: Changes staged and committed to branch `main`.
