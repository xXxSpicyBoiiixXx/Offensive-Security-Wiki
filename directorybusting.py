import requests

# Target URL
target_url = input("Enter the target URL (example.com): ")

# Wordlist file path (a file with common directories)
wordlist_path = input("Enter the wordlist file path: ")

# Open the wordlist file and check each entry
with open(wordlist_path, 'r') as file:
    for line in file:
        directory = line.strip()
        url = f"{target_url}/{directory}"
        
        # Try to access the directory
        response = requests.get(url)
        
        # If a directory exists, print it
        if response.status_code == 200:
            print(f"Directory found: {url}")

