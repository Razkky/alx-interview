#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Regular expression to match the input format
pattern = r'^([\d\.]+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(pattern, line)
        
        if match:
            ip_address, date, status_code, file_size = match.groups()
            
            # Update metrics
            total_file_size += int(file_size)
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_counts[status_code] += 1
            
            # Increment line count
            line_count += 1
            
            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print(f"Total file size: {total_file_size}")
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")
                print()
except KeyboardInterrupt:
    pass  # Handle CTRL + C gracefully

# Print the final metrics
print(f"Total file size: {total_file_size}")
for code in sorted(status_code_counts.keys()):
    print(f"{code}: {status_code_counts[code]}")
