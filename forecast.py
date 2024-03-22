import requests
import json 
import time 
# import os 

def get_fc_hourly(key, latitude, longitude, start_date, end_date):
    url = f"https://services.cehub.syngenta-ais.com/api/Forecast/ShortRangeForecastHourly?latitude={latitude}&longitude={longitude}&startDate={start_date}&endDate={end_date}&supplier=Meteoblue&measureLabel=Precip_HourlySum%20%28mm%29%3BPrecipProbability_Hourly%20%28pct%29%3BShowerProbability_Hourly%20%28pct%29%3BSnowFraction_Hourly%3BSunshineDuration_Hourly%20%28min%29%3BTempAir_Hourly%20%28C%29%3BVisibility_Hourly%20%28m%29%3BWindDirection_Hourly%20%28Deg%29%3BWindGust_Hourly%20%28m%2Fs%29%09%3BWindSpeed_Hourly%20%28m%2Fs%29%3BSoilmoisture_0to10cm_Hourly%20%28vol%25%29%3BSoiltemperature_0to10cm_Hourly%20%28C%29&format=json"
    payload = {}
    headers = {'accept': '*/*', 'ApiKey': key}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response 


def get_fc_daily(key, latitude, longitude, start_date, end_date):
    url = f"https://services.cehub.syngenta-ais.com/api/Forecast/ShortRangeForecastDaily?format=json&supplier=Meteoblue&startDate={start_date}&endDate={end_date}&measureLabel=TempAir_DailyAvg%20(C);TempAir_DailyMax%20(C);TempAir_DailyMin%20(C);Precip_DailySum%20(mm);WindDirection_DailyAvg%20(Deg);WindSpeed_DailyAvg%20(m/s);HumidityRel_DailyAvg%20(pct);WindDirection_DailyAvg;Soilmoisture_0to10cm_DailyAvg%20(vol%25);WindGust_DailyMax%20(m/s);Referenceevapotranspiration_DailySum%20(mm);TempSurface_DailyAvg%20(C);Soiltemperature_0to10cm_DailyAvg%20(C)&latitude={latitude}&longitude={longitude}"

    payload = ""
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'ApiKey': key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response 




key = "536e6d51-43a7-49db-b464-2bbb512a26ef" # os.argv[1] 


hourly = get_fc_hourly(key = key, latitude="47", longitude="7", start_date="2024-03-23", end_date="2024-03-24") # all day 
time.sleep(2) 
parsed_data = json.loads(hourly.text)
for item in parsed_data:
    if 'Precip' in  item['measureLabel']:
        print("Precipitation probability on", item['date'], "is", item['value'] + "%")
        # RAISE A WARNING TO THE USER ? Possibly, implement warnings in response to weather changes ... 

# daily 

threshold = 70
daily = get_fc_daily( key = key , latitude="47", longitude="7", start_date="2024-03-22", end_date="2024-03-22")
parsed_data = json.loads(daily.text)
for item in parsed_data: 
    if 'Precip' in  item['measureLabel'] :
        rain_prob = item['dailyValue']
        if(float(rain_prob) > threshold):
            print("Rainy Day with probability: ", rain_prob)
            print("Do not irrigate today!")
            # RAISE A WARNING TO THE USER  
