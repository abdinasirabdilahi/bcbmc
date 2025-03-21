# bcbmc

Vulnerability 1: Spoofed User

Save and compile: acode.c, gcc acode.c -o acode
Run and Redirect: ./acode > output.txt
Sort and Count: cat output.txt | tr ' ' '\n' | sort | uniq -c | sort -nr > sorted_output.txt
- This will generate 10,000 auth codes and save them to sorted_output.txt, sorted by frequency.

Run the python script: python/python3 script.py
The python script will output the curl requests and the results.
- The script now automatically checks the server's responses for the specified auth_code.
- If a match is found, it prints a message indicating a successful auth code.
- If no match is found, it prints a message indicating a failure