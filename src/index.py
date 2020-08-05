import discord
from discord.ext import commands

import datetime
from urllib import parse, request
import re

from script import main

from config import BOT_TOKEN



bot = commands.Bot(command_prefix='$', description='This is a lolpatch bot')



@bot.command(name="Suma")
async def sum(ctx, numOne: int, numTwo: int):
    """
    Suma dos numeros
    """
    await ctx.send(numOne + numTwo)

@bot.command(name="testing")
async def _testing(ctx):

    print(ctx.valid, ctx.cog, ctx.guild, ctx.channel, ctx.author, ctx.me, ctx.voice_client)

    embed = discord.Embed(title="A", color=discord.Color.dark_blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    
    await ctx.send(embed=embed)
    # await ctx.send(f"{ctx.guild.icon}")

@bot.command()
async def lol_patch(ctx, version):
    # image = discord.File(main(version))
    # await ctx.send(file=image)
    e = discord.Embed(title=f'Notas de la version {version}', color=discord.Color.blue())
    img = main(version)
    e.set_image(url=img)
    await ctx.send(embed=e)



@bot.command()
async def server_info(ctx):
    """
    Info del servidor
    """
    embed = discord.Embed(title=f"{ctx.guild.name}", description='Server info', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue() )
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f'{ctx.guild.owner}')
    embed.add_field(name="Server Region", value=f'{ctx.guild.region}')
    embed.add_field(name="Server ID", value=f'{ctx.guild.id}')

    await ctx.send(embed=embed)



# @bot.command()
# async def youtube(ctx, *, search):
#     """
#     Buscador videos youtube
#     """
#     query_string = parse.urlencode({'search_query': search})
#     html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
#     search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
#     print(search_results)

#     await bot.change_presence(activity=discord.Streaming(name=f"{search}", url='https://www.youtube.com/watch?v=' + search_results[0]))
#     await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])




@bot.command()
async def matuco(ctx):
    await ctx.send('sin huevucos')

@bot.command()
async def esteban(ctx):
    await ctx.send("Bosteed")


# Events
@bot.event
async def on_ready():
    # await bot.change_presence(activity=discord.Streaming(name="Tu vieja", url="https://www.youtube.com/watch?v=Tup1uJ7DHLk"))
    print('My Bot is Ready')

bot.run(BOT_TOKEN)

