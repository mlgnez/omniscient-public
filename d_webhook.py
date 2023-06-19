import datetime, httpx, ip_generator, d_bot

import cosmos


def sendServerWebhook(ip, players_online, players_max, description, latency, version):

    print(ip_generator.getLocationOfIp(str(ip).replace(":25565", "")))

    webhook = ""

    httpx.post(webhook, json={
        "content": "<@&1086809109166301194>",
        "embeds": [
            {
                "title": "Omniscient | New Server Located",
                "description": "Description: ```" + description + "```",
                "color": 16579836,
                "fields": [
                    {
                        "name": "Server Latency:",
                        "value": str(latency),
                        "inline": True
                    },
                    {
                        "name": "Server Version:",
                        "value": version,
                        "inline": True
                    },
                    {
                        "name": "Server Players:",
                        "value": str(players_online) + "/" + str(players_max),
                        "inline": True
                    },
                    {
                        "name": "Server Location:",
                        "value": ip_generator.getLocationOfIp(str(ip).replace(":25565", ""))["city"] + ", " +
                                 ip_generator.getLocationOfIp(str(ip).replace(":25565", ""))["country_name"],
                        "inline": True
                    },
                    {
                        "name": "Total Server Count:",
                        "value": str(int(len(cosmos.read_items(9999))) + 1),
                        "inline": True
                    },
                    {
                        "name": "Storage Type:",
                        "value": "CosmosDB",
                        "inline": True
                    },
                ],
                "author": {
                    "name": "IP: " + ip
                },
                "footer": {
                    "text": "Server BEAMED by Omniscient at " + str(datetime.datetime.now())
                },
                "thumbnail": {
                    "url": "https://api.mcstatus.io/v2/icon/" + ip
                }
            }
        ],
        "attachments": []
    })
