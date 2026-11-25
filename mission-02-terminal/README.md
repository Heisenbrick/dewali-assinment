# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 was to develop practical competence with the command-line interface (CLI). This encompassed learning core file-system navigation and manipulation commands, testing redirection and appending behaviors safely inside a designated sandbox folder, understanding the power of command-line flags and pipes (`|`), and explaining the role of software package managers.

## 2. Work completed
- Explored 9 fundamental terminal operations and documented their functions and behaviors.
- Created an isolated practice folder `terminal-practice/` inside the repository to safely perform file creation, modification, appending, copying, and renaming.
- Analyzed the behavioral difference between file truncation/overwriting (`>`) and end-of-file appending (`>>`).
- Executed and compared standard directory listings against detailed/hidden listings (`ls -la`), and piped results into line-limiting filters (`head` / `Select-Object`).
- Articulated the operational principles of package managers (such as Homebrew, winget, uv, and apt).

## 3. Commands / tools used

### Task 2.1 — Basic Terminal Operations Reference

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display** (`pwd` / `Get-Location`) | Prints the full absolute path of the directory currently active in the terminal session. | Displayed the complete hierarchical path to the current working folder. |
| **Directory listing** (`ls` / `dir`) | Lists the names of visible files and folders present in the current working directory. | Returned a clean list of files and subdirectories located within the folder. |
| **Detailed listing** (`ls -la` / `Get-ChildItem -Force`) | Displays file names alongside detailed metadata including file mode/permissions, file sizes, and timestamps. | Displayed file permissions, last modification timestamps, byte lengths, and hidden dotfiles. |
| **Change directory** (`cd ..`) | Navigates one level up in the filesystem directory tree into the parent folder. | The terminal prompt updated to reflect the parent directory path. |
| **Create directory** (`mkdir terminal-practice`) | Creates a new directory at the specified target path. | A new folder appeared in the directory listing immediately. |
| **Create empty file** (`New-Item practice.txt` / `touch practice.txt`) | Generates a new 0-byte file or updates the timestamp of an existing file. | An empty text file was created on disk ready for editing. |
| **Copy file** (`cp practice.txt backup.txt` / `Copy-Item`) | Creates an exact duplicate of a file at a new destination path while preserving the original. | Two identical independent files were confirmed in the directory listing. |
| **Move / rename file** (`mv backup.txt archive.txt` / `Move-Item`) | Changes the filename or moves the file to a different folder path without duplicating data. | The original filename disappeared and the file reappeared under the new name. |
| **Display file contents** (`cat practice.txt` / `Get-Content`) | Reads a text file sequentially and prints its contents directly to standard output. | The text lines stored inside the file were printed into the terminal console. |

---

### Task 2.2 — Practise File Changes Safely
Inside `terminal-practice/`:
1. Created `practice.txt` and wrote line 1: `"First line of digital detective notes."`
2. Appended line 2 using `>>`: `"Second line added without removing the first."`
3. Confirmed with `cat` that both lines were preserved.
4. Created a backup copy `backup.txt` and renamed it to `archive.txt`.

**Questions Answered:**
- **What is the difference between replacing a file's contents and adding text to the end?**
  Replacing a file's contents (using the `>` redirection operator) truncates the target file to zero bytes before writing, permanently overwriting any prior data. Adding text to the end (using the `>>` append operator) preserves existing file contents and writes the new stream starting immediately at the end of the file.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) duplicates the file data, allocating new storage blocks and creating a second independent file entry. Moving (`mv`) relocates or renames the directory entry pointer without duplicating the underlying data blocks on disk; the file ceases to exist at its former path.
- **What information does the current-directory display provide?**
  The current-directory command (`pwd`) outputs the absolute filesystem path from the root volume down to the exact folder where the shell session is presently situated, providing spatial context for relative path resolution.
- **Why is a directory-listing operation useful?**
  Directory listings (`ls` / `dir`) allow developers to inspect folder contents, verify that files were created or modified as expected, check file sizes and permissions, and confirm the exact names of target files before running operations on them.

---

### Task 2.3 — Understand Flags and Pipes
- **Flags Comparison**: Running `ls` only lists visible file and directory names. Adding flags like `-l` (long format), `-a` (all files including hidden files starting with `.`), and `-h` (human-readable file sizes like KB, MB) changes the command's behavior to output comprehensive metadata tables. In PowerShell, `Get-ChildItem -Force` similarly reveals hidden configuration files.
- **Pipes (`|`)**: A pipe operator takes the standard output (`stdout`) stream of the command on its left-hand side and connects it directly into the standard input (`stdin`) of the command on its right-hand side. For example, running `ls -la | head -n 5` allows `ls` to generate the complete directory list, while `head -n 5` filters the stream to display only the top five lines, preventing terminal clutter.

---

### Task 2.4 — Understand Package Managers
A **package manager** (such as Homebrew on macOS, `winget` or `choco` on Windows, `apt` on Linux, or `uv` for Python) is an automated system software tool that manages the installation, upgrading, configuration, and removal of computer programs. 

Package managers are indispensable because:
1. They automatically resolve and install complex dependency trees required by software packages.
2. They ensure software integrity and security by verifying cryptographic checksums and digital signatures from verified repositories.
3. They provide single-command system-wide upgrades without manual web searching, installer downloads, or wizard clicking.

## 4. My understanding
Working in the Terminal showed me that every file operation—navigating folders, creating files, copying, moving, and inspecting contents—can be done faster and more precisely through text commands than a graphical interface. Understanding the difference between overwriting (`>`) and appending (`>>`), as well as between duplicating data (`cp`) and relocating a directory entry (`mv`), helps prevent accidental data loss. Combining flags (like `ls -la`) with pipes (`|`) lets you filter and chain small tools together to get exactly the output you need, while package managers automate installing and updating software safely.

## 5. Difficulties faced
On Windows, native PowerShell commands use cmdlet aliases (e.g. `ls` aliases `Get-ChildItem`, `cat` aliases `Get-Content`). While basic aliases behave similarly to UNIX, advanced flags (like `-la`) require either running through Git Bash or using native PowerShell parameter syntax (`Get-ChildItem -Force`).

## 6. How I resolved them
Practiced and documented both cross-platform UNIX-style syntax and native PowerShell equivalents to ensure full clarity across environments.

## 7. Evidence / files
- Mission documentation: `mission-02-terminal/README.md`
- Practice directory: `mission-02-terminal/terminal-practice/`
- Evidence log: `evidence/terminal_practice_output.txt`

## 8. Commit details
- **Commit Message**: `Complete Terminal and file management mission`
- **Confirmation**: Changes staged and committed to branch `main`.
