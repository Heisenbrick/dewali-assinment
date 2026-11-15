# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 was to understand and practice distributed version control workflows using Git and GitHub. This included mastering the staging and committing lifecycle, creating and switching to feature branches (`update-about`), opening and evaluating Pull Requests (PRs), and building a clear Git command glossary.

## 2. Work completed
- Inspected repository state and documented the mechanics of `git status`, `git add`, `git commit`, and `git log`.
- Articulated the fundamental difference between staging changes in the index and committing them to the permanent repository history.
- Created and checked out a dedicated feature branch named `update-about`.
- Updated the root `README.md` on the feature branch by adding a dedicated `"## My Learning"` section documenting core takeaways.
- Simulated and completed the Pull Request review and merge workflow back into `main`.
- Authored a comprehensive one-line Git command glossary covering 9 core version-control operations.

## 3. Commands / tools used

### Task 6.1 — Git Workflow Reference

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Inspects the working directory and staging index, identifying untracked files, modified files, and files prepared for the next commit. |
| **Stage selected changes** (`git add <file>`) | Promotes specific modified or newly created files from the working directory into the staging area (index), queuing them for snapshotting. |
| **Create a commit** (`git commit -m "<msg>"`) | Records a permanent, cryptographically hashed snapshot of all currently staged changes along with author metadata, timestamp, and a descriptive message. |
| **View commit history** (`git log` / `git log --oneline`) | Displays the chronological timeline of past commits, illustrating commit hashes, branch heads, and commit summaries. |

#### Difference Between Staging and Committing
**Staging** (`git add`) is like packing items into a shipping box: it allows you to selectively gather and review specific modified files in an intermediate buffer (the index) before finalizing them. **Committing** (`git commit`) is like sealing the box and stamping it with an official tracking number: it permanently writes that snapshot into the repository's cryptographic history database.

---

### Task 6.2 & 6.3 — Branches and Pull Requests

#### Branch Creation (`update-about`)
```bash
git checkout -b update-about
# Added '## My Learning' section to root README.md
git add README.md
git commit -m "Add My Learning section to root README"
```

#### Pull Request Workflow
1. Pushed `update-about` to the remote repository.
2. Opened a Pull Request comparing `update-about` against `main`.
3. Added a PR description summarizing the learning additions made to `README.md`.
4. Reviewed file diffs and completed the merge into `main`.
5. Returned locally to `main` and synchronized changes.

**Why Branches and Pull Requests are Essential:**
A **branch** is an isolated line of development branching off the main codebase. It allows developers to work on new features, bug fixes, or experiments without destabilizing the working `main` branch. 

A **Pull Request (PR)** is a formal review mechanism on platforms like GitHub. It invites team members to inspect, comment on, and test code changes before they are integrated into production. This prevents regressions, enforces code standards, and facilitates knowledge sharing across engineering teams.

---

### Task 6.4 — Git Command Glossary

- **Initialise a repository** (`git init`): Creates a new local Git repository by generating an internal `.git` metadata and tracking directory.
- **Check status** (`git status`): Shows the current state of the working directory and staging area relative to the latest commit.
- **Stage changes** (`git add <file>`): Moves modified or newly created files into the staging index to be included in the next commit.
- **Commit changes** (`git commit -m "<msg>"`): Takes a permanent historical snapshot of staged files with a descriptive message.
- **View history** (`git log`): Displays the chronological list of commits in the current branch history.
- **Create or list branches** (`git branch`): Lists all existing local branches or creates a new branch pointer.
- **Switch branches** (`git switch <branch>` / `git checkout <branch>`): Updates the working directory files to match the specified branch state.
- **Publish changes** (`git push <remote> <branch>`): Uploads local branch commits to a remote hosting platform like GitHub.
- **Retrieve remote changes** (`git pull <remote> <branch>`): Fetches updates from a remote repository and automatically merges them into the current local branch.

## 5. Difficulties faced
Understanding how branch pointers move independently during local checkouts and merges.

## 6. How I resolved them
Used `git log --oneline --graph --all` to visualize the branching tree and verify clean merge integration.

## 7. Evidence / files
- Updated root documentation: `README.md` (with `"## My Learning"` section)
- Mission documentation: `mission-06-git-github/README.md`
- Evidence log: `evidence/git_log_output.txt`

## 8. Commit details
- **Commit Message**: `Complete Git and GitHub collaboration mission`
- **Confirmation**: Feature branch merged into `main` and mission documentation committed.
