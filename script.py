import subprocess

input_file = "sorted_output.txt"
base_url = "http://localhost:8888/"


with open(input_file, 'r') as file:
    for line in file:
        output = line.strip()
        auth_code = output.split()
        if len(auth_code) >= 2: 
            auth_code = auth_code[1]
            url = f"{base_url}{auth_code}"
            command = ["curl", "-X", "GET", url]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                print(f"URL fetched successfully:\n{url}\nOutput:\n{stdout}")
            else:
                print(f"Error fetching URL:\n{url}\nError:\n{stderr}")
        else:
            print(f"Warning: Invalid line format: {output}")





