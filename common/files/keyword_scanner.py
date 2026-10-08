import os
import glob
from pathlib import Path

class KeywordScanner:
    """
    A class to scan files in a directory for specific keywords.
    """
    def __init__(
            self, root_dir:str, pattern:str="*.md",keywords=None
    ):
        """
        Initialize the KeyWordScanner with the root directory, file pattern, and keywords to search for.

        Args:
            root_dir (str): The root directory to start scanning from.
            pattern (str): The glob pattern to match files against. Defaults to "*.md".
            keywords (list, optional): List of keywords to search for. Defaults to ["TODO"].
        """
        self.root_dir = root_dir
        self.pattern = pattern
        self.keywords = keywords or ["TODO"]
        self.matched_files = []

    def scan_with_os_walk(self):
        """
        Scan files in the root directory and its subdirectories using os.walk.

        This method searches for files matching the specified pattern and checks if they contain any of the specified keywords.
        Matched files are added to the `matched_files` list.
        """
        print(f"Searching with os.walk for {self.pattern} in {self.root_dir}")
        for dirpath, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                if glob.fnmatch.fnmatch(filename, self.pattern):
                    full_path = os.path.join(dirpath, filename)
                    if self.search_file(full_path):
                        self.matched_files.append(full_path)

    def scan_with_pathlib(self):
        """
        Scan files in the root directory and its subdirectories using pathlib.Path.rglob.

        This method searches for files matching the specified pattern and checks if they contain any of the specified keywords.
        Matched files are added to the `matched_files` list.
        """
        print(f"Searching with path.rglob for {self.pattern}")
        for file_path in Path(self.root_dir).rglob(self.pattern):
            if file_path.is_file() and self.search_file(file_path):
                self.matched_files.append(str(file_path))

    def search_file(self, filepath):
        """
        Search for the specified keywords in a given file.

        Args:
            file_path (str or Path): The path to the file to search.

        Returns:
            bool: True if any of the keywords are found, False otherwise.
        """
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for keyword in self.keywords:
                    if keyword in self.keywords:
                        if keyword in content:
                            print(f"Match in {filepath} -> keyword: '{keyword}'")
                            return True
        except (IOError, UnicodeDecodeError) as e: #Exception as e:
            print(f"Error reading file {filepath}: {e}")
        return False

    def report_result(self):
        """
        Print the list of matched files.
        """
        print(f"Total matched found: {len(self.matched_files)}")
        for f in self.matched_files:
            print(f" - {f}")