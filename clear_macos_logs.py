#!/usr/bin/env python3

import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode('utf-8')


def clear_logs(log_files):
    for log_file in log_files:
        if os.path.isfile(log_file):
            try:
                with open(log_file, 'w') as f:
                    f.write('')
                print(f"Successfully cleared {log_file}")
            except Exception as e:
                print(f"Failed to clear {log_file}: {e}")
        else:
            print(f"{log_file} not found")


def main():
    log_files = [
        "/var/log/wtmp",
        "/var/log/btmp",
        "/var/log/lastlog",
        "/var/log/system.log",
        "/var/log/wifi.log",
        "/var/log/install.log",
        "/var/log/secure.log",
        "/var/log/appfirewall.log",
        "/var/log/fsck_hfs.log",
    ]
    
    # Run 'log erase' command to clear unified logs from macOS Sierra and later
    unified_logs_command = "log erase --all"
    print("Clearing unified logs...")
    run_command(unified_logs_command)

    print("Clearing log files...")
    clear_logs(log_files)
    

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root.")
    else:
        main()

