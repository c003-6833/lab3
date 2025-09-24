import re
from collections import defaultdict

def ip_parse(line: str) -> str | None:
    # Regex for IPv4 addresses
    match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
    if match:
        return match.group(1)
    return None

counts = defaultdict(int)  # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1

print(counts)
