# import requests
# from twilio.rest import Client

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = "c42352e584bbd03d553e8ae722979928"
# account_sid = "AC0c9f5d418028d81e7d00af03170644f7"
# auth_token = "dfde7f5d6f9ea8a01793b3a5e914d33d"


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
#         from_='+12512610749',
#         body="It's going to rain today. Please remember to bring an umbrella",
#         to='+919059391729'
#         )
#     print(message.status)