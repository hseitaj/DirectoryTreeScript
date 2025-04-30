import os

# Directories and files to exclude from the tree view
EXCLUDE_DIRS = {'.idea', '.venv', '__pycache__', '.pytest_cache'}
EXCLUDE_FILES = set()


def print_tree(root: str, prefix: str = '') -> None:
    """
    Recursively print the directory structure from the given root,
    excluding specified directories and files.

    :param root: Path to start printing from (default: current working directory)
    :param prefix: Prefix for visual indentation
    """
    try:
        entries = sorted(os.listdir(root))
    except PermissionError:
        return  # Skip directories that can't be accessed

    for name in entries:
        # Skip excluded directories/files
        if name in EXCLUDE_DIRS or name in EXCLUDE_FILES:
            continue
        path = os.path.join(root, name)

        # Print directory or file
        is_dir = os.path.isdir(path)
        print(f"{prefix}{name}{'/' if is_dir else ''}")

        # Recurse into directories
        if is_dir:
            print_tree(path, prefix + '    ')


if __name__ == '__main__':
    # Start from the current working directory
    start_path = os.getcwd()
    print_tree(start_path)
