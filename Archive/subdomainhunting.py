import requests

# Define the target domain
domain = input("Enter the target domain (example.com): ")

# Define a list of common subdomains to test
subdomains = ['www', 'mail', 'ftp', 'blog', 'test', 'admin', 'vpn', 'dev']

# Loop through each subdomain and check if it exists
for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        # Attempt to connect to the URL
        response = requests.get(url)
        
        # If successful, print the found subdomain
        if response.status_code == 200:
            print(f"Subdomain found: {url}")
    except requests.ConnectionError:
        pass  # Ignore failed connections

