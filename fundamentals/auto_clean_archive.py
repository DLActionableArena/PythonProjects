import os
from datetime import datetime, timedelta
from common.files import LogArchiver

def simulate_log_environment(log_dir):
    """
    Simulate a log environment by creating the specified log directory.
    Args:
        log_dir: Path to the directory where log files will be simulated.
    """
    os.makedirs(log_dir, exist_ok=True)
    now = datetime.now()
    for i in range(10):
        age = timedelta(days=i*5)
        file_path = os.path.join(log_dir, f"shipment_logs{i}.log")
        with open(file_path, 'w') as f:
            f.write("Log entry...\n" * 5)
        old_time = now - age
        mod_time = old_time.timestamp()
        os.utime(file_path, (mod_time, mod_time))
    print(f"Simulated 10 dummy log files in {log_dir}")

if __name__ == "__main__":
    log_directory = "logs"
    archive_output = "archived_logs"
    archiver = LogArchiver(
        log_root=log_directory,
        archive_folder=archive_output,
        archive_name_prefix="shipment_logs",
        delete_after_days=30,
        archive_within_days=7
    )
    simulate_log_environment(log_directory)
    archiver.scan_logs()