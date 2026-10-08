import os
import json
import portalocker  # filelocking support. Requires pip install "portalocker[win32]" on windows

class JSONKeyValueStore:
    """
    A class to manage a JSON-based key-value store with file locking support.
    """
    def __init__(self, store_root:str, filename):
        self.store_root = store_root       
        os.makedirs(self.store_root, exist_ok=True)
        self.filename = os.path.join(store_root, filename)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)  # Write aan empty JSON to make sure the file exists

    def _read_store(self):
        with open(self.filename, "r") as f:
            portalocker.lock(f, portalocker.LOCK_SH)  # Acquire a shared lock for reading
            data = json.load(f)
            portalocker.unlock(f)  # Release the shared lock after reading
        return data

    def _write_strore(self, data):
        with open(self.filename, "w") as f:
            portalocker.lock(f, portalocker.LOCK_EX)  # Acquire an exclusive lock for writing
            json.dump(data, f, indent=2)
            portalocker.unlock(f)  # Release the exclusive lock after writing

    def set(self, key, value):
        data = self._read_store()
        data[key] = value
        self._write_strore(data)
        print(f"Set key '{key}' -> '{value}'")

    def get(self, key):
        data = self._read_store()
        value = data.get(key)
        print(f"Get key '{key}' -> '{value}'")
        return value

    def delete(self, key):
        data = self._read_store()
        if key in data:
            del data[key]
            self._write_strore(data)
            print(f"Deleted key '{key}'")
        else:
            print(f"Key '{key}' not found")

    def list_all(self):
        data = self._read_store()
        print("Current store content:")
        for key, value in data.items():
            print(f"'{key}': '{value}'")
        return data