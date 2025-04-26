import sys, pathlib

# Ensure project root is on the import path, no matter where pytest runs.
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root))
