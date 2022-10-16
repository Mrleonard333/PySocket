import asyncio
import websockets
from os import system

connected = set()

async def server(websocket):
    connected.add(websocket)

    async for message in websocket:
            for C in connected:
                if C != websocket:
                    print(C)
                    await C.send(f'Message for you: {message}')

async def main():
    system('cls')
    print('[Starting the WebScoket connection]')

    async with websockets.serve(server, "localhost", 5000):
        await asyncio.Future()

asyncio.run(main())