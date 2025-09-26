import re
from collections import defaultdict
import time

def ip_parse(line: str) -> str | None:
    # Extract IPv4 address from a line using regex
    match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
    return match.group(1) if match else None

def top_n(counts: dict, n=5):
    # Return top n IPs sorted by count descending
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

# Start timing
start = time.time()

counts = defaultdict(int)

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1

# End timing
end = time.time()

# Print Top 5 IPs
print("\nTop 5 IPs by failed login attempts:")
for rank, (ip, count) in enumerate(top_n(counts, 5), start=1):
    print(f"{rank}. {ip} — {count}")

# Write full counts to file
with open("failed_counts.txt", "w") as out_file:
    out_file.write("ip,failed_count\n")
    for ip, count in counts.items():
        out_file.write(f"{ip},{count}\n")

# Print elapsed time
print(f"\nElapsed: {end - start:.4f} seconds")
