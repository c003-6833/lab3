import re
import time
from collections import defaultdict

LOGFILE = "sample_auth_small.log"  # change filename if needed

def ip_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "ip", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            return port.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

LOGFILE = "sample_auth_small.log"

# run counting
start = time.time()
counts = defaultdict(int)  # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parser(line)
            if ip:
                counts[ip] += 1


def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

top_ips=top_n(counts , 5)

print("top five attacker ips:")
final_list = top_n(counts, 5)
rank = 0
for i in final_list:
    rank += 1
    print(rank, ":", i[0], "-",i[1])

with open("failed_counts.txt", "w") as f:
    for line in final_list:
        f.write(str(final_list))  # writing the whole list each time!


# end counting
end = time.time()

print("wrote failed_counts.txt")
print("Elapsed:", end-start, "seconds")



