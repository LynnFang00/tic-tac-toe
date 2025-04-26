# Tic-Tac-Toe ♟️ – unbeatable AI with Minimax + α-β pruning


A tiny command-line Tic-Tac-Toe game written in pure Python.  
The computer uses the **Minimax** algorithm with **alpha–beta pruning**, so it never loses and usually wins when you make a mistake.

---

## Features

* Zero external runtime dependencies – only Python 3.8+.
* Clear, commented implementation of
  * state evaluation
  * recursive Minimax
  * α-β pruning to cut the search tree.
* **11 unit-tests** (pytest) that cover
  * win / draw detection  
  * move-generation logic  
  * AI behaviour (must pick winning move, pick centre/corner from empty board).
* Ready-to-use GitHub Actions workflow for automatic test runs on every push.

---

## Quick start

```bash
# Clone + enter the project
git clone https://github.com/LynnFang00/tic-tac-toe.git
cd tic-tac-toe

# (Optional) create virtual-env
python -m venv .venv
. .venv/Scripts/activate      # Windows PowerShell
# source .venv/bin/activate   # Linux / macOS

# Run the game
python -m tic_tac_toe
```
