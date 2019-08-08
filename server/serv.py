import asyncio
from aiohttp import web

FILE_PATH = './public'
MAIN_INDEX = '/index.html'

async def index(request):
    print("Get new req")
    with open(FILE_PATH + MAIN_INDEX) as f:
        return web.Response(text=f.read(),content_type='text/html')

async def test():
    while True:
        await asyncio.sleep(1)
        print("test")

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_static('/public','./public')
    app.router.add_get('/public/{name}',index)
    srv = await loop.create_server(app.make_handler(),host='0.0.0.0',port=11230)
    print("server created")
    return srv

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()

        #create task(can add any function)
        loop.create_task(test())
        
        loop.run_until_complete(init(loop))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
