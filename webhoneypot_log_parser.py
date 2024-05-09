# DShield Cowrie webhoneypot JSON Log Parser
# Josh Jobe
# 8 May 2024
# Ver. 1.0

"""
Example Output:
$ python3 webhoneypot_log_parser.py
Enter the folder name containing webhoneypot JSON files: ../sensor2
Include results with only a forward slash in the URL? (y/n): n
Enter the start log date to begin searching (YYYY-MM-DD) (leave blank to search all logs): 2024-04-15
Enter 1 to search by Source IP or 2 to search by partial URL: 2
Enter a partial URL to search: /cgi-bin/nas_sharing.cgi
Search results saved to _cgi-bin_nas_sharing.cgi.txt
"""
# still need to add comments
import os
import json
from datetime import datetime

def search_logs_by_source_ip(source_ip, folder, include_forward_slash=False, start_log=None):
    results = []
    search_from_start_log = start_log is not None
    for filename in sorted(os.listdir(folder)):
        if filename.startswith('webhoneypot-') and filename.endswith('.json'):
            if search_from_start_log:
                if filename < start_log:
                    continue
                else:
                    search_from_start_log = False
            with open(os.path.join(folder, filename), 'r') as file:
                for line in file:
                    try:
                        log = json.loads(line)
                        if 'sip' in log and log['sip'] == source_ip:
                            if include_forward_slash or ('url' not in log or log['url'] != "/"):
                                results.append(log)
                    except json.JSONDecodeError:
                        pass
    return results

def search_logs_by_partial_url(partial_url, folder, include_forward_slash=False, start_log=None):
    results = []
    search_from_start_log = start_log is not None
    for filename in sorted(os.listdir(folder)):
        if filename.startswith('webhoneypot-') and filename.endswith('.json'):
            if search_from_start_log:
                if filename < start_log:
                    continue
                else:
                    search_from_start_log = False
            with open(os.path.join(folder, filename), 'r') as file:
                for line in file:
                    try:
                        log = json.loads(line)
                        if 'url' in log:
                            url = log['url']
                            if include_forward_slash or (url != "/" and partial_url in url):
                                results.append(log)
                    except json.JSONDecodeError:
                        pass
    return results

def format_log_entry(log):
    formatted_log = f"Time: {log['time']}\n"
    formatted_log += f"Source IP: {log['sip']}\n"
    formatted_log += f"Method: {log['method']}\n"
    formatted_log += f"URL: {log['url']}\n"
    if 'headers' in log:
        formatted_log += f"Headers: {log['headers']}\n"
    if log.get('response_id') is not None and 'status_code' in log['response_id']:
        formatted_log += f"Response Status Code: {log['response_id']['status_code']}\n"
    formatted_log += "\n"
    return formatted_log

def save_results_to_file(results, search_criteria):
    filename = f"{search_criteria}.txt"
    with open(filename, "w") as f:
        for result in results:
            f.write(format_log_entry(result))

def main():
    folder = input("Enter the folder name containing webhoneypot JSON files: ")
    if not os.path.isdir(folder):
        print("Folder not found.")
        return

    while True:
        forward_slash_option = input("Include results with only a forward slash in the URL? (y/n): ").lower()
        if forward_slash_option in ['y', 'n']:
            include_forward_slash = forward_slash_option == "y"
            break
        else:
            print("Invalid option. Please enter 'y' or 'n'.")

    start_log_date = input("Enter the start log date to begin searching (YYYY-MM-DD) (leave blank to search all logs): ")
    if start_log_date:
        try:
            start_log = datetime.strptime(start_log_date, "%Y-%m-%d").strftime("webhoneypot-%Y-%m-%d.json")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return
    else:
        start_log = None

    while True:
        choice = input("Enter 1 to search by Source IP or 2 to search by partial URL: ")
        if choice == '1':
            source_ip = input("Enter the Source IP: ")
            search_criteria = f"ip_{source_ip.replace('.', '_')}"
            results = search_logs_by_source_ip(source_ip, folder, include_forward_slash, start_log)
            break
        elif choice == '2':
            partial_url = input("Enter a partial URL to search: ")
            search_criteria = partial_url.replace('/', '_')
            results = search_logs_by_partial_url(partial_url, folder, include_forward_slash, start_log)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if results:
        save_results_to_file(results, search_criteria)
        print(f"Search results saved to {search_criteria}.txt")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
