import requests
import json

url = "https://elines.coscoshipping.com/ebschedule/public/purpoShipmentWs"

payload = json.dumps({
  "fromDate": "2022-10-16",
  "pickup": "B",
  "delivery": "B",
  "estimateDate": "D",
  "toDate": "2022-11-12",
  "originCityUuid": "738872886234414",
  "destinationCityUuid": "738872886265409",
  "originCity": "Ho Chi Minh, ,Ho Chi Minh,Vietnam,VNHCM",
  "destinationCity": "Helsinki, ,Uusimaa,Finland,FIHEL",
  "cargoNature": "All"
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
