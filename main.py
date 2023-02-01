import requests
import json
import time
from pythonosc.udp_client import SimpleUDPClient

battleMetricsServerID = 6324892 #get from url "https://www.battlemetrics.com/servers/rust/#######"

IP, PORT = "127.0.0.1", 9000
client = SimpleUDPClient(IP, PORT) 
buffer = 3 * 60 #3min


while True:

    serverReq= requests.get(f'https://api.battlemetrics.com/servers/{battleMetricsServerID}').text
    serverData = json.loads(serverReq)

    if serverData == None:
        print('hehe lol xd')

    serverPlayers = serverData['data']['attributes']['players']
    serverMaxPlayers = serverData['data']['attributes']['maxPlayers']
    serverQueue = serverData['data']['attributes']['details']['rust_queued_players']

    if serverQueue > 0:
        print(f"{serverPlayers}/{serverMaxPlayers} players / queue {serverQueue}")
        client.send_message("/avatar/parameters/serverPlayers", serverPlayers)
        client.send_message("/avatar/parameters/serverMaxPlayers", serverMaxPlayers)
        client.send_message("/avatar/parameters/serverQueue", serverQueue)
    else:
        print(f"{serverPlayers}/{serverMaxPlayers} players / no queue")
        client.send_message("/avatar/parameters/serverPlayers", serverPlayers)
        client.send_message("/avatar/parameters/serverMaxPlayers", serverMaxPlayers)
        client.send_message("/avatar/parameters/serverQueue", serverQueue)

        time.sleep(buffer)
        
