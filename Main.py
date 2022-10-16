import asyncio
import websockets
from os import system

connected = set()

async def server(websocket):
    connected.add(websocket)

    async for message in websocket:

            if message == "<^798754613465461987513231871235952721487421^>":
                connected.remove(websocket)

            for C in connected:
                
                if C != websocket:
                    if message == "<^798754613465461987513231871235952721487421^>":
                        await C.send(f"[User has been disconected]")
                    else:
                        await C.send(f"User: {message}")
                        
                else:
                    if message == "<^798754613465461987513231871235952721487421^>":
                        continue
                    else:
                        await C.send(f"You: {message}")

async def main():
    system('cls')
    print('[Starting the WebScoket connection]')

    async with websockets.serve(server, "localhost", 5000):
        await asyncio.Future()

asyncio.run(main())