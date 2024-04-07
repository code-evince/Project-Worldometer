import os
import requests
import re

def downloader():
    # Create a directory to store HTML files if it doesn't exist
    html_dir = 'module_worldometer/html'
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
    z =0
    # Read country names from the text file
    with open('module_worldometer/worldometers_countrylist.txt', 'r') as file:
        countries = [line.strip() for line in file]

        fcountries = [s for s in countries if re.search(r'^[^:-]+$', s)]
        for i in range(len(fcountries)):
            if(fcountries[i]=='USA'):
                fcountries[i]='US'
                z=i
            if(fcountries[i]=='Vietnam'):
                fcountries[i]='viet-nam'
                z=i

    # Download and save HTML files for each country
    for country in fcountries:
        # Construct the URL for the country
        url = f"https://www.worldometers.info/coronavirus/country/{country.lower().replace(' ', '-')}/"
        
        # Download the HTML content
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the HTML content to a file
            if country == 'US':
                country = "USA"
            if country == 'viet-nam':
                country = "Vietnam"
            with open(os.path.join(html_dir, f"{country}.html"), 'wb') as file:
                file.write(response.content)
            
            print(f"Successfully downloaded {country} HTML page.")
        else:
            print(f"Failed to download {country} HTML page from {url}.")

    print("All HTML pages downloaded and saved in the 'html' folder.")
