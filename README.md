# SmartFix

SmartFix is a Python-based utility designed to optimize memory usage in Windows, improving application performance and system stability. It achieves this by trimming the working set of processes that consume a significant amount of RAM.

## Features

- Iterates over all running processes and attempts to reduce their memory usage.
- Targets processes consuming more than 50 MB of RAM.
- Runs as a background service, checking and optimizing memory usage every 10 minutes.

## Requirements

- Python 3.6 or above
- `psutil` library
- Windows operating system

## Installation

1. Ensure Python 3.6 or greater is installed on your Windows system.
2. Install the required Python library:
   ```bash
   pip install psutil
   ```
3. Download the `smartfix.py` script to your local machine.

## Usage

Run the script using Python:

```bash
python smartfix.py
```

The script will continuously monitor and optimize memory usage every 10 minutes. It logs all actions, including any errors or warnings, to help diagnose potential issues.

## Logging

SmartFix logs its activities to the console, showing information about which processes are being optimized and any errors that occur.

## Disclaimer

SmartFix attempts to optimize memory usage by trimming working sets; however, it might not be suitable for all system configurations. Use at your own risk, and ensure critical data is backed up before running the script in a production environment.

## License

This project is licensed under the MIT License.