from copper import *
from modules import *
import discord
from discord import File
from discord.ext import commands

bot = commands.Bot(command_prefix=C.Bot.prefix)
bot.remove_command('help')


@bot.event
async def on_ready():
    Commands.reloadHelp()
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(C.Bot.status))


@bot.event
async def on_message(message):
    if message.content.startswith(C.Bot.prefix):
        # TODO: remove this shit
        if "join_voice" in message.content:
            channel = ctx.author.voice.channel
            await channel.connect()
        elif "leave_voice" in message.content:
            await ctx.voice_client.disconnect()
        else:
            co = execute(message)
            if co is not None:
                botMessage = await message.channel.send(co.text)
                if co.deleteMessage:
                    await message.delete()
                for instruction in co.instructions:
                    if instruction.id == "addReaction":
                        await botMessage.add_reaction(instruction.params['emoji'])
