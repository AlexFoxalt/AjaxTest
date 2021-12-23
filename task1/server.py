import asyncio
from random import randint

from aiohttp import web

from task1.utils import get_request_id, get_data


async def handle(request):
    ping = randint(1, 5)
    await asyncio.sleep(ping)
    response = {"ping": f"{ping*1000}ms",
                "request_id": get_request_id(request),
                "data": get_data(request)}
    return web.json_response(response)


app = web.Application()
app.add_routes([web.get('/', handle)])

if __name__ == '__main__':
    web.run_app(app)
