import requests
import json

url = "https://api.insights.cropwise.com/v2.0/predictions"

def identify_risks(url, planting_date = "2023-10-01T23:00:00.000+0000"):
    payload = json.dumps({
  "request_version": "v1.0",
  "fields": [
    {
      "models": [
        {
          "name": "avizio",
          "version": "v1.0"
        }
      ],
      "location": {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            7.3968164523321,
            48.06046185074764
          ]
        }
      },
      "crop": "WINTER_WHEAT", # grano tenero 
      "crop_variety": {
        "name": "VERSAILLES" # varietà versailles
      },
      "planting": {
        "date": planting_date
      },
      "soil": {
        "practice": "NO-TILL",
        "texture": "SANDY_CLAY"
      },
      "observations": [
        {
          "category": "crop_history",
          "values": [
            {
              "harvest_date": "2022-12-29T00:00:00Z",
              "crops": [
                "OTHERS"
              ]
            },
            {
              "harvest_date": "2023-12-29T00:00:00Z",
              "crops": [
                "CORN"
              ]
            }
          ]
        },
        {
          "category": "yield_potential",
          "yield_potential": {
            "value": 85,
            "unit": "q/ha"
          }
        }
      ],
      "applications": [
        {
          "sequence": 1,
          "date": "2023-12-01T12:24:17+00:00",
          "products": [
            {
              "name": "REVYSTAR XL",
              "rate_of_use": {
                "value": 0.6,
                "unit": "L/ha"
              },
              "diseases": [
                {
                  "code": "PSDCHA",
                  "is_effective": False
                },
                {
                  "code": "ERYSGR",
                  "is_effective": False
                },
                {
                  "code": "GIBBZE",
                  "is_effective": False
                }
              ]
            }
          ]
        }
      ]
    }
  ]
})
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNyb3B3aXNlLWJhc2UtdG9rZW4tcHViLWtleSJ9.eyJzdWIiOiIyZTE5MTdhZC1iMmM4LTQwNWYtOTIxNy1iMmFiMjg5MTZlZTIiLCJpc191c2luZ19yYmFjIjp0cnVlLCJhdWQiOlsic3RyaWRlci1iYXNlIl0sInVzZXJfbmFtZSI6ImFsZXNzYW5kcm8ubWlsZXRvQG1haWwucG9saW1pLml0Iiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sImlzcyI6ImNyb3B3aXNlLWJhc2Utc3RyaXgiLCJleHAiOjE3MTM2NzU1NDYsImF1dGhvcml0aWVzIjpbIkFTU0lHTkVFU19XUklURSIsIlBVUkNIQVNFX09SREVSU19SRUFEIiwiQVNTSUdORUVTX1JFQUQiLCJCVURHRVRTX1dSSVRFIiwiRkFSTVNIT1RTX1JFQUQiLCJURU1QTEFURVNfV1JJVEUiLCJWRU5ET1JTX1dSSVRFIiwiUFJPUEVSVElFU19XUklURSIsIkZJRUxEU19XUklURSIsIkVRVUlQTUVOVFNfUkVBRCIsIlNVUFBMSUVTX1dSSVRFIiwiVkVORE9SU19SRUFEIiwiUFJPUEVSVElFU19SRUFEIiwiUkVWRU5VRVNfUkVBRCIsIklORk9STUFUSU9OX1dSSVRFIiwiUFJPRFVDVFNfV1JJVEUiLCJTRUFTT05TX1JFQUQiLCJTRUFTT05fQVJFQV9XUklURSIsIlBVUkNIQVNFX09SREVSU19XUklURSIsIkVRVUlQTUVOVFNfV1JJVEUiLCJURU1QTEFURVNfUkVBRCIsIlJFUE9SVFNfV1JJVEUiLCJUQVNLU19XUklURSIsIldBUkVIT1VTRVNfUkVBRCIsIkVYUEVOU0VTX1JFQUQiLCJGSUVMRFNfUkVBRCIsIlNVUFBMSUVTX1JFQUQiLCJXQVJFSE9VU0VTX1dSSVRFIiwiT1JHX1JFQUQiLCJQUk9EVUNUU19SRUFEIiwiVEFTS1NfUkVBRCIsIkVYUEVOU0VTX1dSSVRFIiwiU0VBU09OU19XUklURSIsIlNFQVNPTl9BUkVBX1JFQUQiLCJSRVBPUlRTX1JFQUQiLCJSRVZFTlVFU19XUklURSIsIkJVREdFVFNfUkVBRCJdLCJqdGkiOiIyMWJkNzA2YS0yYTk5LTQ5ZmQtYTQwZC0yYmY0ODE1MzVlNmIiLCJjbGllbnRfaWQiOiI5NjYwMDA2ODM0ODE0NTlkYjM0YjA0YTNmMWVmNmYzZSJ9.npmFRqddPz_hPteb_DY3Gb1aBZ4BO5_5PwEOn0m2EH-dCthkwZlIYdFa5HY22gzn5nyV32JaG__G-Tf3FZ_9xIPNv2hTnCp4QZigr9MtoZcTsJlpmO4QV825wNNWTRUcNRK6bmMUJK_K0YvZlkLLSsTy1O7zQ3x09a__j88B-ZJauyesbmPDEjm2CM_INIxuO7dO0zYWo5vKK42cqeQzVMpQVgDvpctoSvy4Ccg12WJtcU0Cp_kzKYByVR5g97f26IS0Mz94KRDgorj44QTQXYSqw2NHZ2xAHcsQn8y30ubUntmJU8ayu30ytTiUngeS5nPt8GJSDr06TxzrGXo80w'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text 

r = identify_risks(url)
parsed_data = json.loads(r)

preds = parsed_data['results'][0]['predictions']
k = "risk_level_by_disease"

for p in preds:
    if p['feature_category'] == "potential_yield_loss":
        features = p['features']
        for f in features:
            if f['type'] == k and f['value'] >= 2:
                print(f"Risk level by disease {f['attributes']['disease_code']}: {f['value']}, we suggest you to call an expert!")
                # send the user a warning, since the risk level is high enough ---> "CALL THE EXPERT!"
    break

daily_recommendations = [p for p in preds if p['feature_category'] == "daily_recommendations"] # get daily recommendations
# pick tomorrow, and just print the recommendations
tomorrow = "2024-07-03T00:00:00Z"
for dr in daily_recommendations:
    if dr['prediction_window']['date'] == tomorrow:
        print(f"Daily recommendations for tomorrow {tomorrow}: ")
        for f in dr['features']:
            print(f"Apply recommendation {f['value']} for disease {f['attributes']['disease_code']}")

