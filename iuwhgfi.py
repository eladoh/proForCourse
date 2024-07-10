import requests
import json

API_KEY = "4bdf5f7ee65b605d9ed28f673a0e83b1d25490566ebb493725c1065430ab4ed9"
path = r"C:\Users\user1\Desktop\corcu\d.txt"
url_scan = "https://www.virustotal.com/vtapi/v2/file/scan"

def print_dict_values(d):
    for key, value in d.items():
        if key == "category" and value not in ["undetected", "type-unsupported"]:
            return True
        elif isinstance(value, dict):
            if print_dict_values(value):
                return True
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    if print_dict_values(item):
                        return True
    return False

def post_request():
    with open(path, 'rb') as file:
        params = {'apikey': API_KEY}
        files = {'file': file}
        posted = requests.post(url_scan, files=files, params=params)

    info_posted = posted.json()
    if info_posted["response_code"] == 1:
        print("Check request successfully")
        return info_posted["resource"]
    else:
        print("Failed to post request")
        return None

def get_request(resource):
    url_report = f"https://www.virustotal.com/api/v3/files/{resource}"
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.get(url_report, headers=headers)
    print(response.status_code)  # Print response status code
    print(response.json())
    return response.json()

# First post the file for scanning
resource = post_request()
if resource:
    # Get the scan report
    response = get_request(resource)

    # Print the response in a formatted way (optional)
    # print(json.dumps(response, indent=4))

    # Check if there's a virus
    if print_dict_values(response):
        print("There is a virus") 
    else:
        print("There isn't a virus")
else:
    print("Failed to get resource for scanning")