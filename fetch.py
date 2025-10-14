# imports
import requests

def fetch_info_from_api(category):
    url = f"https://www.dnd5eapi.co/api/2014/{category}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('results', []):
            returnable = {item['name'] for item in data.get('results', [])}
        else:
             returnable = {item for item in data}
        return returnable
        
    except requests.RequestException as e:
        print(f"Error fetching {category}: {e}")
        return set()

races = fetch_info_from_api("races")
classes = fetch_info_from_api("classes")
