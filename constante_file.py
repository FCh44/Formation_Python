from pathlib import Path

SOURCE_FILE=Path(__file__).resolve()
SOURCE_DIR=SOURCE_FILE.parent
ROOT_DIR=SOURCE_DIR.parent
DATA_DIR=ROOT_DIR/"DATA"

print(SOURCE_FILE)
print(SOURCE_DIR)
print(ROOT_DIR)
print(DATA_DIR)