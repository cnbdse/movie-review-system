import json

movies = [
    {
        "title": "你的名字",
        "genre": "動畫",
        "rating": "4.8",
        "review": "劇情感人，畫面精美。"
    },
    {
        "title": "寄生上流",
        "genre": "劇情",
        "rating": "4.9",
        "review": "劇情反轉精彩。"
    }
]

with open("data/movies.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

print("資料已儲存完成")