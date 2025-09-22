# lab2-2_starter.py

import re
LOGFILE = "sample_auth_small.log"  # change filename if needed

def ip_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " port " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("port")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            return port.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            print (ip_parser(line.strip()))

import re

pattern = r"\d+\.\d+\.\d+\.\d+"
with open("sample_auth_small.log", "r") as f:
    text = f.read()

ips= re.findall(pattern, text)

# Convert to a set to remove duplicates and sort them 
unique_ips = set(ips)
sorted_ips = sorted(unique_ips)

   print("\n--- Summary ---")
    print("Total lines read:", len(lines))
    print("Number of unique IPs:", len(unique_ips))
    print("First 10 unique IPs (sorted):")
    for ip in sorted_ips[:10]:
        print(ip)

    # Optional: Write all unique IPs to a file
    with open("ip.txt", "w") as f:
        for ip in sorted_ips:
            f.write(ip + "\n")

    