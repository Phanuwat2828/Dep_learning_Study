# Link-api:  https://www.goldapi.io/api/XAU/USD/20230617
import requests as re;
from datetime import datetime;
import time
# ดึงเวลาปัจจุบัน



def get():
    current_time = datetime.now()
    current_time =  current_time.strftime("%y%m%d")
    link_api_gold = f'https://www.goldapi.io/api/XAU/USD';
    header_api_gold = {
        "x-access-token":'goldapi-f9xwisslx01aolv-io',
        "content-Type":"application/json"
    }

    try:
        response = re.get(link_api_gold,headers=header_api_gold);
        response.raise_for_status()
        result = response.json()
        return result
    except re.exceptions.RequestException as e:
        return "Problem : ",e
    


while(True):
    data = get();
    # print("ask",data['ask'],"bid",data['bid']);
    print(data)