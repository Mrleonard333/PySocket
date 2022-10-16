# PySocket
## System created using [WebSockets](https://websockets.readthedocs.io/en/stable/) and [Asyncio](https://docs.python.org/3/library/asyncio.html) libraly
## The system can send the message to another Client, and<br>identify if the author is the User or the Client.
```
   /-------------------------------------------------------------------------------\
               v [Store the connections of the connected set]
            for C in connected:
                     v [If the connection is diferent from the WebSocket]
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
   \-------------------------------------------------------------------------------/
```

## <br>You are able to terminate the connection using the button Terminate
```
   /------------------------------------------------------------------------------\
   
     Terminate connection - <button onclick="END_CONNECTION()">Terminate</button>
  |--------------------------------------------------------------------------------|
   
     const END_CONNECTION = () => {
          socket.send("<^798754613465461987513231871235952721487421^>");
          window.alert('System terminated')
     }
  |--------------------------------------------------------------------------------|
      v [If the message is equal to the Terminate message]
      if message == "<^798754613465461987513231871235952721487421^>":
         connected.remove(websocket) < [Remove the connection]
         
   \------------------------------------------------------------------------------/
```
