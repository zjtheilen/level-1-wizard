import requests

# base url for the API being used
API_BASE = "https://www.dnd5eapi.co/api/2014"

# get specific data such as {API_BASE}/races/dwarf or {API_BASE}/classes/druid
def get_data(category, name):
    url = f'{API_BASE}/{category}/{name}'
    response = requests.get(url)
    return response.json() if response.ok else None

# used to return a list of selectable races, classes, backgrounds, or skills
def fetch_list_from_api(category):
    url = f"{API_BASE}/{category}"
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

# fetch lists for all races, all classes, all backgrounds, all skills
races = fetch_list_from_api("races")
classes = fetch_list_from_api("classes")
backgrounds = fetch_list_from_api("backgrounds")
skills = fetch_list_from_api("skills")