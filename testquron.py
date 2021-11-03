import requests

url = "https://api.quran.com/api/v4/resources/tafsirs/%7Btafsir_id%7D/info"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)