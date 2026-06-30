import requests

url = "https://www.imdb.com/chart/top/"

try:
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    print("連線成功")
    print("狀態碼：", response.status_code)

except Exception as e:
    print("錯誤：", e)