# Directory Comparison Tool

This repository contains a simple Python script for comparing two directories by file **content** rather than just filenames.  
It uses **SHA-256 hashing** to identify identical files across directories and reports files that are unique to each directory.

---

## Features
- Recursively scans two directories.
- Calculates SHA-256 hash for each file (in chunks, so large files are supported).
- Collects file metadata: name, path, size, and hash.
- Identifies files that are unique to either directory (based on content).
- Handles unreadable files and reports skipped files.

---

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/dir-compare.git
   cd dir-compare
   ```
2. Replace directory 1 and directory 2 placeholders with actuals paths to compare
   ```python
   compare_dirs_by_hash("directory 1", "directory 2")
   ```
3. Run the script
   ```bash
   python main.py
   ```

