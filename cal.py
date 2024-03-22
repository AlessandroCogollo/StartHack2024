import requests 
import json

url = "https://api.insights.cropwise.com/v2.0/predictions"

def get_data(url, planting_date, forecast_begin, forecast_end):
    payload = json.dumps({
  "request_version": "v1.0",
  "fields": [
    {
      "models": [
        {
          "name": "DSSAT",
          "version": "v2.0"
        }
      ],
      "location": {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            -58.737,
            -29.025
          ]
        }
      },
      "crop": "MAIZE",
      "crop_variety": {
        "name": "SYN897"
      },
      "planting": {
        "date": planting_date
      },
      "water_supply": {
        "is_irrigated": False
      },
      "time_period": {
        "historical": {
          "start_date": "2004-11-24T00:00:00Z",
          "end_date": "2022-05-09T00:00:00Z" # depend on the dataset 
        },
        "forecast": {
          "start_date": forecast_begin,
          "end_date": forecast_end
        }
      }
    }
  ]
})
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNyb3B3aXNlLWJhc2UtdG9rZW4tcHViLWtleSJ9.eyJzdWIiOiIyZTE5MTdhZC1iMmM4LTQwNWYtOTIxNy1iMmFiMjg5MTZlZTIiLCJpc191c2luZ19yYmFjIjp0cnVlLCJhdWQiOlsic3RyaWRlci1iYXNlIl0sInVzZXJfbmFtZSI6ImFsZXNzYW5kcm8ubWlsZXRvQG1haWwucG9saW1pLml0Iiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sImlzcyI6ImNyb3B3aXNlLWJhc2Utc3RyaXgiLCJleHAiOjE3MTM2NzU1NDYsImF1dGhvcml0aWVzIjpbIkFTU0lHTkVFU19XUklURSIsIlBVUkNIQVNFX09SREVSU19SRUFEIiwiQVNTSUdORUVTX1JFQUQiLCJCVURHRVRTX1dSSVRFIiwiRkFSTVNIT1RTX1JFQUQiLCJURU1QTEFURVNfV1JJVEUiLCJWRU5ET1JTX1dSSVRFIiwiUFJPUEVSVElFU19XUklURSIsIkZJRUxEU19XUklURSIsIkVRVUlQTUVOVFNfUkVBRCIsIlNVUFBMSUVTX1dSSVRFIiwiVkVORE9SU19SRUFEIiwiUFJPUEVSVElFU19SRUFEIiwiUkVWRU5VRVNfUkVBRCIsIklORk9STUFUSU9OX1dSSVRFIiwiUFJPRFVDVFNfV1JJVEUiLCJTRUFTT05TX1JFQUQiLCJTRUFTT05fQVJFQV9XUklURSIsIlBVUkNIQVNFX09SREVSU19XUklURSIsIkVRVUlQTUVOVFNfV1JJVEUiLCJURU1QTEFURVNfUkVBRCIsIlJFUE9SVFNfV1JJVEUiLCJUQVNLU19XUklURSIsIldBUkVIT1VTRVNfUkVBRCIsIkVYUEVOU0VTX1JFQUQiLCJGSUVMRFNfUkVBRCIsIlNVUFBMSUVTX1JFQUQiLCJXQVJFSE9VU0VTX1dSSVRFIiwiT1JHX1JFQUQiLCJQUk9EVUNUU19SRUFEIiwiVEFTS1NfUkVBRCIsIkVYUEVOU0VTX1dSSVRFIiwiU0VBU09OU19XUklURSIsIlNFQVNPTl9BUkVBX1JFQUQiLCJSRVBPUlRTX1JFQUQiLCJSRVZFTlVFU19XUklURSIsIkJVREdFVFNfUkVBRCJdLCJqdGkiOiIyMWJkNzA2YS0yYTk5LTQ5ZmQtYTQwZC0yYmY0ODE1MzVlNmIiLCJjbGllbnRfaWQiOiI5NjYwMDA2ODM0ODE0NTlkYjM0YjA0YTNmMWVmNmYzZSJ9.npmFRqddPz_hPteb_DY3Gb1aBZ4BO5_5PwEOn0m2EH-dCthkwZlIYdFa5HY22gzn5nyV32JaG__G-Tf3FZ_9xIPNv2hTnCp4QZigr9MtoZcTsJlpmO4QV825wNNWTRUcNRK6bmMUJK_K0YvZlkLLSsTy1O7zQ3x09a__j88B-ZJauyesbmPDEjm2CM_INIxuO7dO0zYWo5vKK42cqeQzVMpQVgDvpctoSvy4Ccg12WJtcU0Cp_kzKYByVR5g97f26IS0Mz94KRDgorj44QTQXYSqw2NHZ2xAHcsQn8y30ubUntmJU8ayu30ytTiUngeS5nPt8GJSDr06TxzrGXo80w'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response 

ret = get_data(url = url, planting_date="2024-03-02T00:00:00Z", forecast_begin="2024-03-21T00:00:00Z",  forecast_end= "2024-03-28T00:00:00Z")
data = ret.json()

# import time 
# time.sleep(2) 

preds = data['results'][0]['predictions']

t = ['growth_stage:Ritchie scale', 'growth_stage:BBCH' ] 

for p in preds: 
    for j in  range(len(p['features'])):
        x = p['features'][j]['type']
        if x in t: 
            # print(f"Index {x} :\t\t{p['features'][j]['value']}\t\t{p['features'][-1]['value']}")
            print(f"Page growth according to index {x:<30} {p['features'][j]['value']:<10} at time {p['features'][-1]['value']}")