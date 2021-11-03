import requests

from pprint import pprint as print

app_id = "11795dab"
app_key = "2e131411f955e3b14e0cef227abadca0"
language = "en-gb"

word_id = "python"
url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + word_id.lower()


r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)
res = r.json()
# print(res)