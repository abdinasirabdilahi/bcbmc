# Proof of Concept

Vulnerability 1: Spoofed User

Save and compile: acode.c, gcc acode.c -o acode
Run and redirect: ./acode > output.txt
Sort and count: cat output.txt | tr ' ' '\n' | sort | uniq -c | sort -nr > sorted_output.txt
- This will generate 10,000 auth codes and save them to sorted_output.txt, sorted by frequency.

Run the python script: python/python3 script.py
The python script will output the curl requests and the results.
- The script now automatically checks the server's responses for the specified auth_code.
- If a match is found, it prints a message indicating a successful auth code.
- If no match is found, it prints a message indicating a failure



Vulnerability 2: Command Injection After User Spoofing

To exploit this vulnerability, we must spoof user authentication. First, we need to obtain a valid authentication code for the user's session. This can be achieved by using a brute-force technique. Specifically, the technique outlined in the "Vulnerablility 1" section of the README.md. 

Once we obtain a valid auth code, we access the application at http://localhost:8888/auth_code/, where auth_code is the spoofed code. At this point, the application may allow the user to input a URL. 

We know that the application does not conduct proper input validation. So when we input a command, we can inject any arbitrary shell commands. For this example, we use "touch". 

In the URL, we can inject '; touch hack.txt; ' 

When the application processes the URL, it will execute the injected commands on the server. 
- We can verify the exploit by checking for the created file (hack.txt) in the user's home directory. 
- To see the newly added file, change directories into .bcbm using the command cd .bcbm/  
