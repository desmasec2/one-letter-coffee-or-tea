import os

os.umask(0o022)
os.makedirs("/output", exist_ok=True)
path = "/output/entry.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("A")
os.chmod(path, 0o644)
print("A")
