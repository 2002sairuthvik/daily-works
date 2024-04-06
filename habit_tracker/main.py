# import requests
# from datetime import datetime
# pixela_endpoint = "https://pixe.la/v1/users"

# USER_NAME = "ruthvik"
# TOKEN = "qwjd8wdjq92jdmw"
# GRAPH_ID = "graph1"

# user_params = {
#     "token" : TOKEN,
#     "username" : USER_NAME,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes",
# }


# # response = requests.post(url=pixela_endpoint,json=user_params)
# # print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

# graph_params = {
#     "id" : GRAPH_ID,
#     "name" : "Cycling Graph",
#     "unit" : "Km",
#     "type" : "float",
#     "color" : "ajisai",
# }

# headers = {
#     "X-USER-TOKEN" : TOKEN,
# }

# # response = requests.post(url=graph_endpoint,json=graph_params, headers=headers)
# # print(response.text)
# today = datetime(year=2024, month=4, day=3)

# pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "17.5",
# }
# # response = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
# # print(response.text)
# update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"
# update_data = {
#     "quantity" : "10.5"
# }
# # response =  requests.put(url=update_endpoint,json=update_data,headers=headers)
# # print(response.text)

# delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)