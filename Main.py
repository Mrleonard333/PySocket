import asyncio
import websockets
from os import system

connected = set()

async def server(websocket):
    connected.add(websocket) # < Store the WebSocket connection

                # v Store the messages of the WebSocket connection
    async for message in websocket:

                # v If the message is equal to the Terminate message
            if message == "<^798754613465461987513231871235952721487421^>":
                connected.remove(websocket) # < Remove the connection

              # v Store the connections of the connected set
            for C in connected:
                    # v If the connection is diferent from the WebSocket
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
                                # v Handler         # v Port
    async with websockets.serve(server, "localhost", 5000): # < Start the connection
        await asyncio.Future()              # ^ Host
                # ^ Make a loop

asyncio.run(main()) # < Start the main system