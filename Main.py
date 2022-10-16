import asyncio
import websockets
from os import system

async def server(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    system('cls')
    print('[Starting the WebScoket connection]')

    async with websockets.serve(server, "localhost", 5000):
        await asyncio.Future()

asyncio.run(main())