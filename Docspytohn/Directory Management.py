import os
from pathlib import Path

# Creating a directory with os
os.makedirs("new_directory", exist_ok=True)

# Creating a directory with pathlib
Path("new_directory").mkdir(parents=True, exist_ok=True)
