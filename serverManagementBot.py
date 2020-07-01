import subprocess
import discord
from mcstatus import MinecraftServer
from discord.ext import commands

TOKEN = "NzIzMDAzMjc0NDIwMTU4NTU1.XvY6MQ.ugIyJOkyqa21-g19uvjjzqEFum0"
server = MinecraftServer.lookup("ysondev.kro.kr:25565")
status = server.status()

def checkIfOnline():
    if(status.latency > 0):
        return 'On'
    else:
        return 'Off'

bot = commands.Bot(command_prefix='!')

@bot.command(name='open-server', help='Open the server.')
async def openServer(ctx):
    await ctx.send("Opening the server...")
    subprocess.Popen(['java', '-Xmx2G', '-Xms1G', '-jar', 'spigot-1.16.1.jar'], shell=True, cwd='C:\Server\serverl')


@bot.command(name='close-server', help='Close the server')
async def closeServer(ctx):
    subprocess.call('taskkill /im java.exe')
    await ctx.send("Server Closed and saved!")

@bot.command(name='status', help='Check server status')
async def checkPlayers(ctx):
    await ctx.send("Server Status: {}\n# of online players: {}".format(checkIfOnline(), status.players.online))

bot.run(TOKEN)