The scripts are designed around the Internet Storm Center (ISC) DShield Honeypot.  The scripts were designed to aid in parsing the JSON files after noticing something interesting from the Kibana DShield dashboard on the DShield SIEM provided by Guy Bruneau: https://github.com/bruneaug/DShield-SIEM

# json_parser_folders.py
This Python script will extract pertinent details from cowrie.json.* files within a folder and organize it for easy viewing. You can either search by IP address or by session ID.

# webhoneypot_log_parser.py
This script extracts details from webhoneypot JSON logs contained in a folder, enabling you to search by IP address or even a partial URL.  In order to save resources and speed up processing, the results are saved to a txt file using either the IP address used to search or the URL as the filename.  The script limits the results to Time, Source IP, Method, URL, and Headers.  

The intent for both of the files is to begin analysis using Kibana and when something interesting is noticed to perform further analysis using the scripts.

