# Cowrie JSON Log Parser
# Josh Jobe
# 3 Mar 2024
# Ver. 1.0
"""
Background:
Created as part of SANS Technology Institute, Internet Storm Center Internship
to facilitate parsing cowrie json files based on either target IP address or session
ID. The IP or session ID is discovered from data first observed from a local DShield 
ELK Server provided by Guy Bruneau:
https://github.com/DShield-ISC/dshield

Example Output:
$ python3 scripts/json_parser_folders.py
Enter the folder name to search in (relative to script location): ../sensor1
Enter 1 to search by Source IP or 2 to search by Session ID: 1
Enter the Source IP: 45.95.147.236
Search results:
Event ID: cowrie.session.connect
Timestamp: 2024-02-12T02:29:35.585811Z
Source IP: 45.95.147.236
Session ID: 51add7e71ed7
"""

import os
import json

def search_logs_by_source_ip(source_ip, folder):
    results = []
    for filename in os.listdir(folder):
        if filename.startswith('cowrie.json.'):
            with open(os.path.join(folder, filename), 'r') as file:
                for line in file:
                    try:
                        log = json.loads(line)
                        if 'src_ip' in log and log['src_ip'] == source_ip:
                            results.append(log)
                    except json.JSONDecodeError:
                        pass
    return results

def search_logs_by_session_id(session_id, folder):
    results = []
    for filename in os.listdir(folder):
        if filename.startswith('cowrie.json.'):
            with open(os.path.join(folder, filename), 'r') as file:
                for line in file:
                    try:
                        log = json.loads(line)
                        if 'session' in log and log['session'] == session_id:
                            results.append(log)
                    except json.JSONDecodeError:
                        pass
    return results

def format_log_entry(log):
    formatted_log = f"Event ID: {log['eventid']}\n"
    formatted_log += f"Timestamp: {log['timestamp']}\n"
    formatted_log += f"Source IP: {log['src_ip']}\n"
    formatted_log += f"Session ID: {log['session']}\n"
    if 'username' in log:
        formatted_log += f"Username: {log['username']}\n"
    if 'password' in log:
        formatted_log += f"Password: {log['password']}\n"
    if 'input' in log:
        formatted_log += f"Command Input: {log['input']}\n"
    if 'outfile' in log:
        formatted_log += f"File Outfile: {log['outfile']}\n"
    if 'filename' in log:
        formatted_log += f"Uploaded File: {log['filename']}\n"
    if 'hassh' in log:
        formatted_log += f"Client SSH Fingerprint: {log['hassh']}\n"
    formatted_log += "\n"
    return formatted_log

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder = input("Enter the folder name to search in (relative to script location): ")
    folder_path = os.path.join(script_dir, folder)
    if not os.path.isdir(folder_path):
        print("Folder not found.")
        return

    while True:
        choice = input("Enter 1 to search by Source IP or 2 to search by Session ID: ")
        if choice == '1':
            source_ip = input("Enter the Source IP: ")
            results = search_logs_by_source_ip(source_ip, folder_path)
            break
        elif choice == '2':
            session_id = input("Enter the Session ID: ")
            results = search_logs_by_session_id(session_id, folder_path)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("Search results:")
    for result in results:
        print(format_log_entry(result))

if __name__ == "__main__":
    main()
