import requests
from bs4 import BeautifulSoup

def scrape_brightest_stars():
    url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'  # Replace this URL with the actual website URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            star_data = []

            # Assuming the data is presented in a table with rows and columns
            star_table = soup.find('table')  # Adjust this based on the actual HTML structure
            rows = star_table.find_all('tr')[1:]  # Skip the header row

            for row in rows:
                columns = row.find_all('td')
                name = columns[0].text.strip()
                distance = columns[1].text.strip()
                mass = columns[2].text.strip()
                radius = columns[3].text.strip()
                luminosity = columns[4].text.strip()

                star_data.append({
                    'name': name,
                    'distance': distance,
                    'mass': mass,
                    'radius': radius,
                    'luminosity': luminosity,
                })

            return star_data

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    stars = scrape_brightest_stars()
    if stars:
        for star in stars:
            print(star)
    else:
        print("No data retrieved.")
