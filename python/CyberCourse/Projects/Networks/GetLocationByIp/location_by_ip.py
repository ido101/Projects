import requests

def get_ip_location(ip_address=""):
    # If ip_address is empty, it will automatically use the public IP of the user
    # However, in this program I also found the users public IP address and used it to get the location of the user
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "success":
        print(f"IP: {data.get('query')}")
        print(f"Country: {data.get('country')}")
        print(f"Region: {data.get('regionName')}")
        print(f"City: {data.get('city')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Coordinates: {data.get('lat')}, {data.get('lon')}")
    else:
        print("Lookup failed:", data.get("message"))

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except requests.RequestException as e:
        return None

ip_address = input("Enter an IP address to lookup (or leave blank for your own): ")
if not ip_address:
     # lookup your own public IP
    ip_address = get_public_ip()
    if ip_address:
        print("Your Public IP Will Be Searched:", ip_address)
    else:
        print("Failed to retrieve public IP address.")
        exit()

get_ip_location(ip_address)