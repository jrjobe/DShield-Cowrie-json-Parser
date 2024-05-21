The scripts are designed around the Internet Storm Center (ISC) DShield Honeypot.  The scripts were designed to aid in parsing the JSON files after noticing something interesting from the Kibana DShield dashboard on the DShield SIEM provided by Guy Bruneau: https://github.com/bruneaug/DShield-SIEM

# json_parser_folders.py
This Python script will extract pertinent details from cowrie.json.* files within a folder and organize it for easy viewing. You can either search by IP address or by session ID.

# webhoneypot_log_parser.py
This script extracts details from webhoneypot JSON logs contained in a folder, enabling you to search by IP address or even a partial URL.  In order to save resources and speed up processing, the results are saved to a txt file using either the IP address used to search or the URL as the filename.  The script limits the results to Time, Source IP, Method, URL, and Headers.  

The intent for both of the files is to begin analysis using Kibana and when something interesting is noticed to perform further analysis using the scripts.

# AI Usage
Time is valuable, especially when it is limited.  We can spend time researching and reading every technique out there on how to do something, wasting precious time.  These scripts were created with the help of OpenAI ChatGPT.  The process always begins with a template of the data that I would like to pull and in a format/order that I want to use.  I submit this to ChatGPT along with an example of the data I would like to parse and a little bit of an explanation.  Within seconds I am presented with a rather well structured script that is mostly ready to go.  Sometimes it works as is, other times you might have to work through an unexpected error.  I have worked through the errors manually when I had the time (not studying for an exam) and I have presented the errors to ChatGPT for a recommended solution.  The majority, if not 99% of the time, ChatGPT provided me with a solution I could implement very quickly, or gave me what I needed to work through the error.  AI is the way of the future and cuts through the enormous amount of websites, articles, and books to give you just what you need with minimal explanation unless requested.
