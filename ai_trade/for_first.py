import requests
import time

def get_gold_price(api_key):
    url = 'https://www.goldapi.io/api/XAU/USD'
    headers = {'x-access-token': api_key}
    response = requests.get('https://th.investing.com/currencies/xau-usd-chart%20?utm_source=google&utm_medium=cpc&utm_campaign=20484512094&utm_content=671236894202&utm_term=dsa-1944158649753_&GL_Ad_ID=671236894202&GL_Campaign_ID=20484512094&ISP=1&npl=1&af_adset_id=151469545614&gad_source=1&gclid=Cj0KCQjw9vqyBhCKARIsAIIcLMFoxlt2RPXdVG6z0xHj0PQVVkmOY-rVSWX5SBJhDs9daF_p-C-e1PkaAvpbEALw_wcB')
    
    if response.status_code == 200:
        data = response.text
        return data
    else:
        return None

# ใส่ API Key ของคุณที่นี่
api_key = 'goldapi-f9xwisslx01aolv-io'

# ตั้งค่าระยะเวลาการอัปเดต (เช่น ทุก 60 วินาที)
update_interval = 60

while True:
    gold_price = get_gold_price(api_key)
    
    if gold_price:
        print(f"Current Gold Price (USD): {gold_price}")
    else:
        print("Failed to retrieve data")

    # รอเวลาตามที่กำหนดก่อนดึงข้อมูลอีกครั้ง
    time.sleep(update_interval)

