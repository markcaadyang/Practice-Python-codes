import urlib.request as ur
import urlib.parse as up 
import json


service_url = "http://py4e-data.dr-chuck.net/json?key=42&"

address_input = input("Enter Location: ")
params = {"sensor": "false", "address": address_input}
url = service_url + up.urlencode(params)
print("retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print("retrieved", len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("place id", place_id)