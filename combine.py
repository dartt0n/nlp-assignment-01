from pathlib import Path


files = sorted(Path("data/1bwords").iterdir())

print(files)

with open("text-corpus-001-010.txt", "w") as f:
    for file in files[:10]:
        f.write(file.read_text())

with open("text-corpus-001-050.txt", "w") as f:
    for file in files[:50]:
        f.write(file.read_text())

with open("text-corpus-001-100.txt", "w") as f:
    for file in files[:100]:
        f.write(file.read_text())
