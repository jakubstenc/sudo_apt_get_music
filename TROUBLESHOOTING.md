# Troubleshooting Strudel & Environment Issues

## 1. "Error: Could not register service worker"

**Problem:**
You see a red error banner: `Error loading webview: Error: Could not register service worker: InvalidStateError...`

**Cause:**
This is a known VS Code issue where the internal browser (webview) gets into a bad state, often after an update or if the editor has been open for a long time. It restricts the webview from registering necessary background workers.

**Solution:**
1.  **Restart VS Code:** Completely close the window and re-open it.
2.  **Kill Zombie Processes (if restart fails):**
    - Close VS Code.
    - Open a terminal and run: `killall code` (or check your system monitor for any "code" processes).
    - Re-open VS Code.

## 2. "Failed to automatically locate a python executable..." (Jupytext)

**Problem:**
A popup says: `Failed to automatically locate a python executable that can invoke Jupytext.`

**Cause:**
The Jupytext extension cannot find your Python install.

**Solution:**
1.  Open the Command Palette (`Ctrl+Shift+P`).
2.  Type and select: `Python: Select Interpreter`.
3.  Choose the recommended path (usually `/usr/bin/python3` or your virtual environment).
4.  If the error persists, you can safely ignore it if you are not actively converting Jupyter notebooks to text files in this session.
