# import requests
# from datetime import datetime
# APP_ID = "0d408cc3"
# API_KEY = "74ff6821d2ba4762c8ae2e0b427c453f	"

# GENDER = "female"
# WEIGHT_KG = 67
# HEIGHT_CM = 154
# AGE = 38


# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = "https://api.sheety.co/203cb28ac79de5e2161c509bd8a2a03f/workouts/workouts"
# exercise_text = input("Tell me which exercises you did: ")

# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }

# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }

# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# # print(result)

# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

#     # headers_sheety = { "Authorization": "cnV0aHZpazp3b3Jrb3V0MDk4Nw", }

#     sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

#     print(sheet_response.text)