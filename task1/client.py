import asyncio

from httpx import AsyncClient


async def make_request(num):
    url = "http://127.0.0.1:8080/"
    headers = {"request_id": f"{num}",
               "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"}
    async with AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response_json = response.json()
        print(response_json)
        return response_json


async def main():
    num = int(input('How many requests do you want?: '))
    queue = asyncio.Queue()
    current_num = 0
    task_list = []
    while current_num < num:
        current_num += 1
        task = asyncio.create_task(make_request(current_num))
        task_list.append(task)
    await queue.join()
    await asyncio.gather(*task_list, return_exceptions=True)
    print('Done!')

asyncio.run(main())
