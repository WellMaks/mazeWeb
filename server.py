import websockets
import asyncio
from maze_generator import createMaze, printFloorRow


PORT = 8000
async def echo(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            try:
                h = int(message.split(",")[0])
                w = int(message.split(",")[1])
                if(3 < h < 21 and 3 < w < 21):
                    await websocket.send(createMaze(h, w))
                else:
                    await websocket.send("Please use values between 4 and 20")
            except ValueError:
                await websocket.send("Wrong input!")
    except websocket.exceptions.ConnectionClosed as e:
        print("A client just disconnected!")

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()