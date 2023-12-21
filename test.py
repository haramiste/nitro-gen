import requests
from requests.structures import CaseInsensitiveDict
import time

url = "https://api.discord.gx.games/v1/direct-fulfillment"

headers = CaseInsensitiveDict()
headers["authority"] = "api.discord.gx.games"
headers["accept"] = "*/*"
headers["accept-language"] = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
headers["content-type"] = "application/json"
headers["origin"] = "https://www.opera.com"
headers["referer"] = "https://www.opera.com/"
headers["sec-ch-ua"] = 'Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = "Windows"
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "cross-site"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"

data = '{"partnerUserId":"a3e124b1b0ee5b23b7eaa3779aeb2a1191952ee1daf6c7fab3b1c56107d59937"}'

i = 0

while True:
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        response_json = resp.json()
        token = response_json.get('token', '')

        output_text = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n"

        with open('output.txt', 'a') as file:
            file.write(output_text)

        print(f"Generate {i}")

        i += 1  
        time.sleep(0.5)
    else:
        print("La requête a échoué")
        time.sleep(2)