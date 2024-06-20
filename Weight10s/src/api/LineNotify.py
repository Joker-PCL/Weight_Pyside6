import requests

class LineNotify:
    def __init__(self, token: str, message: str = ""):
        self.url = "https://notify-api.line.me/api/notify"
        self.headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer " + token,
        }

        # ส่งไลน์แจ้งเตือน
        if message:
            try:
                response = requests.post(self.url, headers=self.headers, data={"message": message})
                if response.status_code == 200:
                    print("*** Message send successfully")
                else:
                    print(f"*** Failed to send message: {response.status_code}, {response.text}")
            except Exception as error:
                print(error)
                pass