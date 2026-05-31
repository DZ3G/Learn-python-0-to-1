# CLI Budget Tracker
> A command-line personal finance tracker built in Python — my first independent project after completing a beginner Python course.

---

## What This Project Does

This is a terminal-based budget tracker that lets a user:
- Add income and expense transactions
- View current balance (income − expenses)
- Browse transaction history
- Persist all data to a `.txt` file so nothing is lost between sessions

Everything runs in a loop-based CLI menu with full input validation — no invalid entry can crash the program.

---

## Why I Built This

After finishing my first Python course, I wanted to prove to myself that I actually understood what I had learned — not just followed along. I asked Claude (Anthropic's AI) to give me a project that would test every concept from the course at once. The challenge it gave me was deliberately hard: build a working CLI budget tracker using only built-in Python, with no templates, no tutorials, and real data persistence.

The requirements Claude set:
- Organized code using functions (no spaghetti)
- Full input validation with `try/except`
- Data that persists between runs (file I/O)
- A clean menu loop the user can actually navigate

Claude acted as a code reviewer throughout — pointing out bugs, asking me to explain my logic, and refusing to just give me the answers. Every line of code was written by me. When I was stuck, I got hints and explanations, not solutions.

---

## What I Applied From The Course

| Concept | Where it shows up in this project |
|---|---|
| Variables & data types | Storing `income`, `expenses`, `username` |
| Arithmetic operators | Computing balance with `income - expenses` |
| Conditionals | Routing menu choices, income vs expense |
| While loops | Main menu loop, input validation loops |
| Functions | Every feature is its own function |
| String methods | `.strip()`, `.split()`, `.startswith()` for file parsing |
| File I/O | Saving transactions to `transaction.txt`, loading on startup |
| `try/except` | All user input is wrapped in error handling |
| Global variables | Used to share `income` and `expenses` across functions |

---

## How I Built It — The Real Process

### Step 1 — Skeleton first
I started by writing the basic structure: global variables, a greeting function, a menu, and a `while True` loop. No logic yet — just the shape of the program.

### Step 2 — Input validation
I wrote the option selection logic first and immediately ran into my first bug: I tried using `select != range(10)` thinking it would check if the input was a valid number. It doesn't — a string is never equal to a `range` object so the condition was always `True`. I learned that the correct approach is `try/except ValueError` around `int(input(...))`.

I then noticed I was writing the same validation loop in multiple places. I refactored it into a single reusable `input_handling(op)` function that takes a list of valid options as a parameter. This was my own idea — it wasn't in the course material.

### Step 3 — Add transaction & file saving
I added income/expense input and wrote transactions to a `.txt` file using `open("transaction.txt", "a")`. Early on I was saving the running total instead of logging individual entries, which would have made the file useless for history. I redesigned the save format to write labeled lines:
```
income: 500
expenses: 200
Net income: 300
```

### Step 4 — Loading from file on startup
This was the hardest part. The problem: every time the program restarts, `income` and `expenses` reset to 0 even though the file has data. I needed to read the file on startup and reconstruct those values.

I wrote `load_transactions()` which reads the file line by line in reverse (to get the most recent values first) and extracts numbers using `.split(":")` and `.strip()`.

---

## Bugs I Hit and How I Fixed Them

### Bug 1 — `income += add` crashed
`input()` returns a string. Adding a string to an int raises a `TypeError`. Fixed by wrapping with `int()` or `float()`.

### Bug 2 — `select != range(10)` never worked
A string compared to a `range` object is always not equal. Replaced with `try/except ValueError` and `if select not in [1, 2, 3]`.

### Bug 3 — Program crashed on first run (no file yet)
`open("transaction.txt", "r")` raises `FileNotFoundError` if the file doesn't exist. Fixed with `try/except FileNotFoundError`.

### Bug 4 — `load_transactions()` silently loaded nothing
This was the trickiest bug. The function ran without errors but `income` and `expenses` stayed at 0. After adding debug prints I discovered the save format wrote `income : 500` (with a space before the colon) but the loader checked `line.startswith("income:")` (no space). One character mismatch meant the condition never matched. Fixed by making the save and load format identical. 
### Bug 5 — transaction.txt path

When moving `transaction.txt` into the same folder as `CLI ATM.py`, the script could no longer find it because Python looks for files relative to where you *run* the script, not where the script lives.

**The fix was to make the path relative to the script file itself:**

```python
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSACTION_FILE = os.path.join(BASE_DIR, "transaction.txt")
```

Then replace every `"transaction.txt"` in the code with `TRANSACTION_FILE`.

> I had to use Claude for this one as I wasn't familiar with how Python resolves file paths at runtime.

**Lesson learned:** the format you write to a file and the format you read from it must be character-perfect. One space breaks everything silently.

---

## What I Would Improve With More Knowledge

- **Replace global variables with a class** — right now `income` and `expenses` are globals shared across functions. The clean solution is a `BudgetTracker` class with those as attributes. I know globals are bad practice from my course but I didn't yet have the OOP knowledge to do it differently.
- **Use CSV format** — Python's built-in `csv` module would make saving and loading much more reliable than manually parsing text lines.
- **Add a delete transaction feature** — the file only grows, there's no way to remove an entry.
- **Ask for username on first run** — currently hardcoded.

---

## What This Project Taught Me

Beyond the technical fixes, the most valuable thing I learned was **debugging methodology**. When `load_transactions()` wasn't working, I didn't guess — I added `print("DEBUG lines:", lines)` and `repr(line)` to see exactly what Python was reading. That approach — make the invisible visible — is how I solved every hard bug in this project.

I also learned that writing code that *runs* and writing code that *works correctly after a restart* are completely different problems. File I/O and state persistence added a layer of complexity that no tutorial exercise had prepared me for.

---

## Tech Stack

- **Language:** Python 3
- **Libraries:** `time` (built-in only)
- **Storage:** Plain text file (`transaction.txt`)

---

## How To Run

```bash
python CLI_ATM.py
```

Make sure `CLI_ATM.py` and `transaction.txt` (if you have existing data) are in the same directory.

---

*First independent project — completed after finishing the Python beginner course by Tech With Tim. Project challenge and code review provided by Claude (Anthropic). All code written independently.*