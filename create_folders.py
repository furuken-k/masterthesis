import os

folders = [
    "data/raw",
    "data/interim",
    "data/processed",
    "notebooks",
    "src",
    "src/models",
    "results",
    "results/figures",
    "results/tables",
    "results/models",
    "thesis",
    "thesis/images",
    "thesis/drafts"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("All folders created successfully!")
