import os
import requests

# Create a directory to store HTML files if it doesn't exist
html_dir = 'html'
if not os.path.exists(html_dir):
    os.makedirs(html_dir)

# Read country names from the text file
with open('worldometers_countrylist.txt', 'r') as file:
    countries = [line.strip() for line in file]

# Download and save HTML files for each country
for country in countries:
    # Construct the URL for the country
    url = f"https://www.worldometers.info/coronavirus/country/{country.lower().replace(' ', '-')}/"
    
    # Download the HTML content
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the HTML content to a file
        with open(os.path.join(html_dir, f"{country}.html"), 'wb') as file:
            file.write(response.content)
        print(f"Successfully downloaded {country} HTML page.")
    else:
        print(f"Failed to download {country} HTML page from {url}.")

print("All HTML pages downloaded and saved in the 'html' folder.")
