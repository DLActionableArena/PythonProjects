import os
import zipfile
from datetime import datetime # , timedelta

class LogArchiver:
    """
    A class to manage the archiving of log files.
    """
    def __init__(
        self,
        log_root:str,
        archive_folder:str,
        archive_name_prefix:str,
        delete_after_days:int=30,
        archive_within_days:int=7
    ):
        """ 
        Initialize the LogArchiver instance.
        Args:
            log_root: Root directory containing the log files to manage.
            archive_folder: Destination folder where archived log files are stored.
            delete_after_days: Number of days to keep archived files before deleting them.
            archive_within_days: Archive log files that are older than this many days.
        """
        self.log_root = log_root
        self.archive_folder = archive_folder
        self.delete_after_days = delete_after_days
        self.archive_within_days = archive_within_days
        self.archive_name_prefix = archive_name_prefix
        self.files_to_archive = []
        os.makedirs(self.archive_folder, exist_ok=True)

    def scan_logs(self):
        """
        Scan the log root directory for log files to archive.
        """
        print(f"Scanning logs in {self.log_root}...")
        # self.files_to_archive = []
        for root, _, files in os.walk(self.log_root):
            for file in files:
                if file.endswith(".log"):
                    file_path = os.path.join(root, file)
                    self.process_file(file_path)

        if self.files_to_archive:
            self.archive_all()

    def process_file(self, file_path):
        """
        Process a single log file to determine if it should be archived.
        Args:
            file_path: Path to the log file to process.
        """
        stat_info = os.stat(file_path)
        file_fmtime = datetime.fromtimestamp(stat_info.st_mtime)
        now = datetime.now()
        age_days = (now - file_fmtime).days
        if age_days > self.delete_after_days:
            self.delete_file(file_path)
        elif age_days <= self.archive_within_days:
            self.files_to_archive.append(file_path)
            
    def delete_file(self, file_path):
        """
        Delete a log file.
        Args:
            file_path: Path to the log file to delete.
        """
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except OSError as e:  # Exception as e
            print(f"Error deleting file {file_path}: {e}")
            
    def archive_all(self):
        """
        Archive all log files that have been marked for archiving.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d")
        archive_name = os.path.join(self.archive_folder, f"{self.archive_name_prefix}_{timestamp}.zip")
        try:
            with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file_path in self.files_to_archive:
                    arcname = os.path.relpath(file_path, self.log_root)
                    zipf.write(file_path, arcname=arcname)
                    print(f"Added to Archived: {file_path}")
                    os.remove(file_path)  # Optionally delete the file after archiving
            print(f"All recent logs archived to: {archive_name}")
        except OSError as e:  # Exception as e
            print(f"Error creating archive {archive_name}: {e}")