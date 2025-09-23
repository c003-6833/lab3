import re

LOGFILE = "sample_auth_small.log"

if __name__ == "__main__":
    unique_ips = set()
    total_lines = 0

    pattern = r"\d+\.\d+\.\d+\.\d+"  # regex for IP addresses

    with open(LOGFILE, "r") as f:
        for line in f:
            total_lines += 1
            # Check if 'from' is in the line and extract IPs
            if "from" in line:
                ips_in_line = re.findall(pattern, line)
                unique_ips.update(ips_in_line)  # add all found IPs to set

    sorted_ips = sorted(unique_ips)

    print("\n--- Summary ---")
    print("Total lines read:", total_lines)
    print("Number of unique IPs:", len(unique_ips))
    print("First 10 unique IPs (sorted):")
    for ip in sorted_ips[:10]:
        print(ip)

    # Optional: write all unique IPs to a file
    with open("ip.txt", "w") as f:
        for ip in sorted_ips:
            f.write(ip + "\n")


    