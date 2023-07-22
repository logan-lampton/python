import requests
import sys
from datetime import datetime

# importing passwords/tokens
sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords')
import habit_tracker

USERNAME = "logan-l"
TOKEN = habit_tracker.keys("token")

pixela_endpoint = "https://pixe.la/v1/users"

# ---- params to create a new user ----
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# ---- creating (POSTING) graph ----

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


# ---- creating (POSTING) pixels in the graph ----

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"

# 20 Mi/32.19 Km goal
quantity = "32.19"

# datetime with the strftime method
today = datetime.today()
formatted_today = today.strftime("%Y%m%d")

pixel_params = {
    "date": formatted_today,
    "quantity": quantity
}

# create_p_response = requests.post(url=graph_endpoint, json=pixel_params, headers=headers)
# create_p_response.raise_for_status()

# ---- update a pixel (PUT) ----

# can change the date to update in the endpoint via the variable below
date_to_update = formatted_today

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date_to_update}"

update_params = {
    "quantity": "0.0"
}

# update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# update_response.raise_for_status()

# delete a pixel (DELETE)
# can change the date to delete in the endpoint via the variable below
date_to_delete = formatted_today
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date_to_delete}"

# No params needed

delete_response = requests.delete(url=delete_endpoint, headers=headers)
delete_response.raise_for_status()
