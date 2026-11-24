"""One Letter: Coffee or Tea — the answer is A (coffee).

Writes exactly one character, "A", to /output/entry.txt (mode 0644)
and prints it. No trailing newline: the entry is a single character.
"""
import os

os.umask(0o022)
os.makedirs("/output", exist_ok=True)
path = "/output/entry.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("A")
os.chmod(path, 0o644)
print("A")
