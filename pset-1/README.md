# Problem set 1

Complete the four functions in `src/pset1/`. All imports are already provided.
Replace each TODO comment and `raise NotImplementedError(...)` line with
your code. Leave the imports and `__init__.py` as provided.

| Function | File |
| --- | --- |
| `countNucleotides` | `src/pset1/count_nucleotides.py` |
| `patternIndex` | `src/pset1/pattern_index.py` |
| `patternCount` | `src/pset1/pattern_count.py` |
| `frequentWords` | `src/pset1/frequent_words.py` |

Refer to the assignment for function requirements.

## Setup

Use Python 3.10 or newer. Open a terminal in the repository root, the folder
containing both `in-class/` and `pset-1/`. Run:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ./in-class -e ./pset-1
```

If you already have a virtual environment, activate it and run just the
install command. On Windows, use `python` instead of `python3` if needed;
activate with `.venv\Scripts\activate` in Command Prompt or
`.venv\Scripts\Activate.ps1` in PowerShell.

The install command connects both local packages to your environment.
The `-e` means edits in either folder take effect without reinstalling.
Activate this same environment when you return to work in a new terminal.
If using an editor, select this environment's Python interpreter there too.

## Imports

The in-class functions are already imported in the corresponding assignment
files under these names:

| Assignment file | Imported name | Source |
| --- | --- | --- |
| `pattern_count.py` | `inclass_pattern_count` | `PatternCount` in `in-class/src/frequent_words/pattern_count.py` |
| `frequent_words.py` | `inclass_frequent_words` | `FrequentWords` in `in-class/src/frequent_words/frequent_words.py` |

The `as` keyword in each import provides a local nickname for the imported
function. The setup command above makes the in-class package available;
no file copying or changes to Python's search path are needed.

To import your assignment functions, start `python` in your activated
environment and enter:

```python
from pset1 import countNucleotides, patternIndex, patternCount, frequentWords
```

Use the package imports instead of running individual source files directly.
Unfinished stubs raise `NotImplementedError` when called.
