import psutil
import ctypes
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def empty_working_set(pid):
    """
    Trims the working set of a process to free up memory.
    """
    try:
        process_handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
        if process_handle:
            ctypes.windll.psapi.EmptyWorkingSet(process_handle)
            ctypes.windll.kernel32.CloseHandle(process_handle)
            logging.info(f"Trimmed working set for PID {pid}")
            return True
        else:
            logging.warning(f"Failed to open process handle for PID {pid}")
    except Exception as e:
        logging.error(f"Error trimming working set for PID {pid}: {e}")
    return False

def optimize_memory():
    """
    Iterates over all running processes to optimize memory usage.
    """
    logging.info("Starting memory optimization...")
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memory_info = proc.info['memory_info']
            if memory_info.rss > 50 * 1024 * 1024:  # Consider processes using more than 50 MB of RAM
                if empty_working_set(proc.info['pid']):
                    logging.info(f"Optimized memory for {proc.info['name']} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            logging.warning(f"Could not process PID {proc.info['pid']}: {e}")
    logging.info("Memory optimization completed.")

if __name__ == "__main__":
    # Run optimization every 10 minutes
    while True:
        optimize_memory()
        time.sleep(600)  # Wait for 10 minutes before re-running