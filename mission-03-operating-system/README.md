# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 was to investigate the core responsibilities and internal mechanics of the operating system (OS). This involved collecting system details, monitoring active processes and Process Identifiers (PIDs), understanding absolute versus relative path resolution, examining file permissions (`rwx`), and articulating the primary management responsibilities of modern operating systems.

## 2. Work completed
- Gathered system specifications, current user account details, storage capacity, and live process snapshots in a privacy-safe manner.
- Investigated process management, defining what a process is, what PIDs signify, and highlighting real-world examples.
- Analyzed filesystem path navigation (absolute vs. relative) and examined file permissions and access control modes.
- Documented the six core responsibilities of operating systems in a structured analytical table.

## 3. Commands / tools used
- `Get-ComputerInfo` / `systeminfo`: Gathered OS edition, architecture, and kernel version.
- `whoami`: Verified current active user account identity.
- `Get-PSDrive C`: Inspected volume capacity, used storage, and free disk space.
- `Get-Process`: Captured running processes, active thread counts, and memory footprints.
- `Get-Acl`: Inspected filesystem access control lists and permission rights.

## 4. My understanding

### Task 3.1 — Explore Your Operating System

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS family, build version, platform edition, and CPU hardware architecture. | Microsoft Windows 11 64-bit (OS Build 26100), x86_64 architecture. |
| **Current account identity** | Identifies the active user account context under which commands and processes are executed. | Standard local user account (`[redacted]`). |
| **Available and used storage** | Shows total non-volatile drive capacity, space consumed by existing files, and remaining headroom. | System Drive `C:`: ~100+ GB used, ~200+ GB available capacity. |
| **System activity snapshot** | Captures active foreground and background processes, CPU load, and RAM memory utilization. | Multiple background services and shell processes active; memory utilization stable. |

*Privacy note: Personal usernames, hardware serial IDs, and network addresses are masked as `[redacted]`.*

---

### Task 3.2 — Understand Processes
- **What is a process?**
  A process is an active, executing instance of a computer program loaded into volatile memory (RAM). It encompasses the program's machine code, allocated memory address space (heap, stack, data segment), active execution threads, CPU register states, open file handles, and security context.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique, non-negative integer assigned dynamically by the operating system kernel whenever a new process is spawned. The kernel uses the PID to track process state, allocate CPU scheduling slices, manage memory boundaries, and terminate programs upon request.
- **Two examples of processes running on this computer:**
  1. `explorer.exe` (PID varies): The core Windows Graphical Shell process responsible for rendering the desktop UI, taskbar, start menu, and file management explorer.
  2. `svchost.exe` (PID varies): Generic host process used by Windows to run background operating system services such as networking, event logging, and Windows Update.

---

### Task 3.3 — Understand Paths and Permissions

#### Absolute vs. Relative Paths
- **Absolute Path**: An absolute path specifies the complete, unambiguous location of a file or directory starting from the filesystem root volume. It does not depend on the current working directory.
  - *Example from this project*: `C:\Users\[redacted]\.gemini\antigravity\scratch\digital-detective-1234\mission-03-operating-system\README.md`
- **Relative Path**: A relative path locates a target resource starting from the terminal's *current working directory* using directional tokens such as `.` (current folder) or `..` (parent folder).
  - *Example from project root*: `.\mission-03-operating-system\README.md`

#### File Permissions

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Grants authorization to open, view, and read a file's content or list a directory's contents. | Opening a markdown document or reading source code. |
| **w — Write** | Grants authorization to modify, overwrite, append to, or delete a file, or create/delete files within a directory. | Saving changes to a Python script or saving notes. |
| **x — Execute** | Grants authorization to run an executable binary or script as an active process, or traverse into a directory. | Executing a shell script or compiled binary. |

---

### Task 3.4 — Explain Operating-System Responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Orchestrates CPU time allocation across multiple concurrent programs using scheduling algorithms, managing thread states and context switching. | Switching smoothly between a web browser, code editor, and music player without freezing. |
| **Memory management** | Allocates and tracks physical RAM addresses for active programs, isolates address spaces to prevent crashes, and swaps data to virtual memory (paging file). | Allocating 400 MB of RAM to a Python data process and reclaiming that memory when the script finishes. |
| **Device management** | Communicates with diverse peripheral hardware components via standardized device drivers and input/output controllers. | Sending formatted print streams to a USB/network printer driver without the app knowing hardware details. |
| **File management** | Structures storage media into hierarchical filesystems (NTFS, ext4), managing directory structures, metadata, access control, and storage clusters. | Creating, renaming, and finding documents on an SSD without managing raw disk sectors. |
| **User interface / shell** | Provides a command-line interface (CLI) or graphical user interface (GUI) enabling humans to issue commands and launch programs. | Using PowerShell to run automated commands or clicking application icons on the desktop. |
| **Security and permissions** | Enforces user authentication, process isolation, access control lists (ACLs), and privilege elevation safeguards. | Requiring User Account Control (UAC) administrative consent before installing kernel drivers. |

## 5. Difficulties faced
Windows uses Access Control Lists (ACLs) rather than traditional POSIX octal permission strings (`chmod 755`).

## 6. How I resolved them
Examined the Windows security model via `Get-Acl` and mapped its `ReadAndExecute`, `Write`, and `FullControl` rights to the universal `r`, `w`, and `x` conceptual permissions.

## 7. Evidence / files
- Mission documentation: `mission-03-operating-system/README.md`
- Evidence log: `evidence/os_inspection_output.txt`

## 8. Commit details
- **Commit Message**: `Document operating system and file management`
- **Confirmation**: Changes staged and committed to branch `main`.
