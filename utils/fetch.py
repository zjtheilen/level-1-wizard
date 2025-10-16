import requests

API_BASE = "https://www.dnd5eapi.co/api/2014"

def get_race_data(race_name):
    url = f'{API_BASE}/races/{race_name.lower()}'
    response = requests.get(url)
    return response.json() if response.ok else None

def get_class_data(class_name):
    url = f'{API_BASE}/classes/{class_name.lower()}'
    response = requests.get(url)
    return response.json() if response.ok else None

def get_background_data(background_name):
    url = f'{API_BASE}/backgrounds/{background_name.lower()}'
    response = requests.get(url)
    return response.json() if response.ok else None

def fetch_list_from_api(category):
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

races = fetch_list_from_api("races")
classes = fetch_list_from_api("classes")
backgrounds = fetch_list_from_api("backgrounds")