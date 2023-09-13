import discord
from discord.ext import commands
from vars import *


# Initialize the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def pfsense(ctx):
    # Check if the command was issued in a specific channel where you want to accept rules
    if ctx.channel.name == '✅-rules':
        # Assign a role to the user as a way of accepting the rules
        role = discord.utils.get(ctx.guild.roles, name='Member')
        await ctx.author.add_roles(role)
        await ctx.send(f'Welkom, {ctx.author.mention}! Top je hebt de regels geaccepteerd :)')

@bot.command()
async def opnsense(ctx):
    # Check if the command was issued in a specific channel where you want to accept rules
    if ctx.channel.name == '✅-rules':
        # Assign a role to the user as a way of accepting the rules
        role = discord.utils.get(ctx.guild.roles, name='Member')
        await ctx.author.add_roles(role)
        await ctx.send(f'Welkom, {ctx.author.mention}! Top je hebt de regels geaccepteerd :)')

@bot.command()
async def mikrotik(ctx):
    # Check if the command was issued in a specific channel where you want to accept rules
    if ctx.channel.name == '✅-rules':
        # Assign a role to the user as a way of accepting the rules
        role = discord.utils.get(ctx.guild.roles, name='Member')
        await ctx.author.add_roles(role)
        await ctx.send(f'Welkom, {ctx.author.mention}! Top je hebt de regels geaccepteerd :)')

# Run the bot with your token
bot.run(token)
