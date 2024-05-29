import socket
import csv

# List of websites to check
websites = [
    "www.example0.com",
    
]

# List to store results
results = []

# Check each website
for website in websites:
    try:
        ip_address = socket.gethostbyname(website)
        results.append([website, ip_address])
        print(f"{website} resolves to {ip_address}.")
    except socket.gaierror:
        results.append([website, "No IP address found"])
        print(f"{website} does not resolve to an IP address.")

# Write the results to a CSV file
with open('dns_resolution_results.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Website', 'IP Address'])
    csvwriter.writerows(results)

print("DNS resolution check complete. Results saved to 'dns_resolution_results.csv'.")
