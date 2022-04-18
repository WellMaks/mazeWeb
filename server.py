import websockets
import asyncio
from maze_generator import createMaze, solution


PORT = 8000
async def echo(websocket, path):
    print("Client connected")
    created = False
    a = ""
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            try:
                h = int(message.split(",")[0])
                w = int(message.split(",")[1])
                if(3 < h < 21 and 3 < w < 21):
                    a = createMaze(h, w)
                    await websocket.send(a)
                    created = True
                else:
                    await websocket.send("Please use values between 4 and 20")
            except ValueError:
                await websocket.send("Wrong input!")

            if(message == "dick" and created == True):
                await websocket.send(solution(a))
            if(message == "dick" and created == False):
                await websocket.send("Not generated yet u moron")

    except websocket.exceptions.ConnectionClosed as e:
        print("A client just disconnected!")

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()