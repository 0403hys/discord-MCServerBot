import subprocess
import discord
import time
from mcstatus import MinecraftServer
from discord.ext import commands

TOKEN = "NzIzMDAzMjc0NDIwMTU4NTU1.XvY6MQ.ugIyJOkyqa21-g19uvjjzqEFum0"

def connectToServer():
    try:
        server = MinecraftServer.lookup('127.0.0.1:25565')
        server.status()
        return server
    except:
        return -1

def checkIfOnline(server):
    print(server)
    if(server == -1):
        return 'Off'
    return 'On'

bot = commands.Bot(command_prefix='!')

@bot.command(name='open-server', help='Open the server.')
async def openServer(ctx): 
    await ctx.send("Opening the server... [Estimated Time: 20.0s]")
    subprocess.Popen(['java', '-Xmx2G', '-Xms1G', '-jar', 'spigot-1.16.1.jar'], cwd='C://Minecraft Server')

@bot.command(name='close-server', help='Close the server')
async def closeServer(ctx):
    subprocess.call('taskkill /im java.exe')
    await ctx.send("Server Closed and saved!")

@bot.command(name='status', help='Check current server status')
async def checkStatus(ctx):
    await ctx.send('Checking...')
    server = connectToServer()
    await ctx.send('Server Status: {}'.format(checkIfOnline(server)))

bot.run(TOKEN)
