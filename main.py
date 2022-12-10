import requests
import time


def main():
    url = 'https://api.stackexchange.com'
    epoch_time_now_minus_2days = int(time.time()) - 86400 * 2
    result = []
    i = 1
    while True:
        com = f'/2.3/questions?page={i}&pagesize=100&fromdate={epoch_time_now_minus_2days}&order=desc&sort=creation&tagged=python&site=stackoverflow'
        res = requests.get(url + com)
        result.extend(res.json()["items"])
        i += 1
        if not res.json()['has_more']:
            break
    print(f"На Stackoverflow за последние два дня было {len(result)} вопросов с тегом 'Python'. ")
    if input("Вывести список вопросов (y/n): ") == 'y':
        [print(item['title']) for item in result]


if __name__ == '__main__':
    main()
