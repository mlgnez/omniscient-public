import discord, random, ip_generator, datetime, pinger, requests, interactions
from discord import app_commands
from discord.ext import commands, tasks
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from collections import Counter
from interactions.ext.files import command_send

import cosmos

description = 'A python program that exploits response ' \
              'pings from Minecraft Servers to anonymously scan the internet for minecraft servers '

bot = interactions.Client(description=description, intents=interactions.Intents.DEFAULT)


def generate_server_embed(description, ip, latency, version_name, online, max):
    embed = interactions.Embed(title="Omniscient | Server Requested",
                          description="Server Description: " + description, color=16579836)
    embed.set_author(name="Server IP: " + ip)
    embed.set_footer(text="Server requested by user at: " + str(datetime.datetime.now()))
    embed.add_field(name="Server Latency: ", value=str(latency), inline=False)
    embed.add_field(name="Server Version: ", value=str(version_name), inline=False)
    embed.add_field(name="Server Players: ",
                    value=str(online) + "/" + str(max),
                    inline=False)
    embed.add_field(name="Server Location: ",
                    value=ip_generator.getLocationOfIp(str(ip).replace(":25565", ""))["city"] + ", " +
                          ip_generator.getLocationOfIp(str(ip).replace(":25565", ""))["country_name"],
                    inline=False)

    return embed


def get_all_servers():
    servers = cosmos.get_all_servers()
    new_server_list = []

    for server in servers:
        new_server_list.append(server)

    return new_server_list


def get_number_of_players():
    online = 0
    for server in cosmos.get_all_servers():
        online += int(server["online"])

    return online


def get_most_common_versions():
    versions = []
    for server in cosmos.get_all_servers():
        versions.append(server["version:"])

    counter = Counter(versions).most_common(3)
    write = ""

    for count in counter:
        new_common = str(count).replace("(", "").replace(")", "").replace("',", " | Count:").replace("\'", "")
        write += "Version: " + str(new_common) + "\n"

    return write


@bot.event
async def on_ready():
    print(f'Logged in as {bot.me.name} (ID: {bot.me.id})')
    print('------')


@bot.command(name="ping", description="Pings an IP", options=
[interactions.Option(
    name="ip",
    description="IP of the server",
    type=interactions.OptionType.STRING,
    required=True,
),
interactions.Option(
        name="port",
        description="Port of the server",
        type=interactions.OptionType.STRING,
        required=True,
)])
async def ping(ctx: interactions.CommandContext, ip: str, port: str):
    if ip is None:
        await ctx.send("Please include an IP")

    if port is None:
        await ctx.send("Please include a Port")

    try:
        server = pinger.return_values_ping(ip + ":" + port, True)
        await command_send(ctx, embeds=generate_server_embed(server.description, server.ip, server.latency, server.version.name, server.online, server.max), ephemeral=True)
    except Exception:
        await ctx.send("Failed to ping; Either try again later, or try another IP")


@bot.command(name="stats", description="Interesting stats on all of Omniscient's collected servers")
async def stats(ctx: interactions.CommandContext):
    await ctx.send("Loading Stats...")
    embed = interactions.Embed(title="Omniscient | Server Stats", color=16579836)
    embed.add_field(name="Total # of Servers Indexed", value=str(len(get_all_servers())))
    embed.add_field(name="Total # of Players Found", value=str(get_number_of_players()))
    embed.add_field(name="Most Common Versions:", value=str(get_most_common_versions()))
    await ctx.send(embeds=embed)




if __name__ == "__main__":
    bot.start('')
