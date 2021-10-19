import requests
import time
from datetime import datetime

previous_supply = 0.0
page_code = 200
wait_time = 30      # In seconds

while True:
    page = requests.get("https://hexvisionpublicapi.azurewebsites.net/api/TotalSupply")
    supply = float(page.content.decode("utf-8"))
    if page.status_code == 200 and supply != previous_supply:
        print(datetime.now(), supply)
        if previous_supply > 0:
            print("Difference: ", supply-previous_supply, '\n')
        previous_supply = supply
        page_code = 200
    elif page.status_code == 200 and supply == previous_supply:
        page_code = 200
    elif page.status_code != 200:
        if page_code == 200:
            print(datetime.now(), "Error code: ", page.status_code, '\n')
            page_code = page.status_code
    time.sleep(wait_time)