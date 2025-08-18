import hashlib
from pathlib import Path


def hash_file(filepath, chunk_size=8192):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
    except Exception as e:
        print(f"could not read file: {filepath} - {e}")
        return None
    return hasher.hexdigest()


def collect_files(base_path):
    file_data = []
    skipped = []
    for filepath in Path(base_path).rglob('*'):
        if filepath.is_file():
            try:
                size = filepath.stat().st_size
                hash_ = hash_file(filepath)
                if hash_:
                    file_data.append((filepath.name, str(filepath), size, hash_))
                else:
                    skipped.append(filepath.name)
            except Exception as e:
                print(f"failed to collect {filepath}: {e}")
    print(f"Total files found: {len(file_data) + len(skipped)}")
    print(f" - Files with hash: {len(file_data)}")
    print(f" - Files without hash (skipped): {len(skipped)}")
    return file_data


def compare_dirs_by_hash(dir1, dir2):
    data1 = collect_files(dir1)
    data2 = collect_files(dir2)

    # make hash → (name, path, size)
    hash_map1 = {entry[3]: entry for entry in data1}
    hash_map2 = {entry[3]: entry for entry in data2}

    # Find unique hash-values
    unique_in_1 = set(hash_map1.keys()) - set(hash_map2.keys())
    unique_in_2 = set(hash_map2.keys()) - set(hash_map1.keys())

    print(f"\nFiles unique for {dir1}:")
    for h in unique_in_1:
        name, path, size, _ = hash_map1[h]
        print(f"{path} ({size} bytes)")

    print(f"\nFiles unique for {dir2}:")
    for h in unique_in_2:
        name, path, size, _ = hash_map2[h]
        print(f"{path} ({size} bytes)")


def main():
    compare_dirs_by_hash("directory 1", "directory 2")


if __name__ == "__main__":
    main()