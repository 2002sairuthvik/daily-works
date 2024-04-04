# import requests
# from twilio.rest import Client

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = "your api key"
# account_sid = "your account id from twilio , u can use after signing up"
# auth_token = "this is porvided below the acct id"


# weather_params = {
#     "lat" : 16.290380,
#     "lon" : 80.445854,
#     "appid" : api_key,
#     "cnt" : 4
# }
# response  = requests.get(url=OWM_Endpoint,params= weather_params)
# response.raise_for_status()
# weather_data =  response.json()
# # print(weather_data["list"][0]["weather"][0]["id"])
# will_rain = False
# for hour_data in weather_data["list"]:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) > 700 :
#         will_rain=True
# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         from_='this num will be provided in twilio',
#         body="It's going to rain today. Please remember to bring an umbrella",
#         to='this will be your num which will be used for signing up'
#         )
#     print(message.status)
