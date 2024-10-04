import requests
from time import sleep
from prettytable import PrettyTable
from datetime import datetime

# List of subdomains to check

subdomains = [
    'http://subdomain1.awesomeweb',
    'http://subdomain2.awesomeweb',
    'http://subdomain3.awesomeweb'
]


# Function to check the status of each subdomain
def check_subdomains_status(subdomains):
    table = PrettyTable()
    table.field_names = ["Subdomain", "Status", "Last Checked"]
    
    for subdomain in subdomains:
        try:
            # Send a GET request to the subdomain
            response = requests.get(subdomain)
            
            # Check if the response status code is 200 (OK)
            if response.status_code == 200:
                status = "UP"
            else:
                status = f"DOWN (Status Code: {response.status_code})"
        except requests.exceptions.RequestException:
            status = "DOWN (Request Failed)"
        
        # Add the result to the table
        table.add_row([subdomain, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    
    return table

# Main function to repeatedly check subdomains status every minute
def main():
    while True:
        # Clear the terminal screen (works for Unix-based OS, for Windows use 'cls')
        print("\033[H\033[J")
        print("Checking subdomain statuses...\n")

        # Check the status of each subdomain and display the result in a table
        table = check_subdomains_status(subdomains)
        print(table)

        # Wait for 60 seconds before checking again
        sleep(60)

if __name__ == "__main__":
    main()
