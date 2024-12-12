# Importing necessary modules
import socket
from datetime import datetime

# Banner with instructions
print("Simple Port Scanner")

# Define target IP
target = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Start scanning process
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")

try:
    # Iterate over the defined range of ports
    for port in range(start_port, end_port + 1):
        # Create a new socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Attempt to connect to the port
        result = s.connect_ex((target, port))
        
        # Check if port is open
        if result == 0:
            print(f"Port {port}: Open")
        
        # Close the socket
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
except socket.gaierror:
    print("\nHostname could not be resolved.")
except socket.error:
    print("\nCouldn't connect to server.")

print(f"Scanning completed at: {datetime.now()}")

