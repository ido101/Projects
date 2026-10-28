from pathlib import Path
from urllib import response
import requests

virus_total_api_scan_file_url = "https://www.virustotal.com/api/v3/files"
virus_total_api_key = "ecc39f64c40af7a792a173000feedbff7b625b1af84498b32199ef1f53d857d2"

def iterate_directory_contents(directory_path):
    directory_path = Path(directory_path) 
    for item in directory_path.iterdir():
        if item.is_file():
            analysis_id = upload_file(item)
            get_analysis(analysis_id)
        else:
            iterate_directory_contents(item)

def upload_file(file_path):
    print(f"Scanning file: {file_path}")
    headers = {
        "x-apikey": virus_total_api_key,
    }
    response = requests.post(url=virus_total_api_scan_file_url, headers=headers, files={'file': open(file_path, 'rb')})
    response = response.json()
    response = response['data'] 
    return response['id']

def get_analysis(analysis_id):
    url = "https://www.virustotal.com/api/v3/analyses/"+analysis_id
    headers = {
    "x-apikey": "ecc39f64c40af7a792a173000feedbff7b625b1af84498b32199ef1f53d857d2"
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    result =  "Safe!" if str(response['data']['attributes']['stats']['malicious']) == "0" else "Virus!"
    print("response is:" + result)


if __name__ == "__main__":
    iterate_directory_contents(r'C:/Users/IDO123/Desktop/Projects/python/CyberCourse/Projects/AntiVirus')