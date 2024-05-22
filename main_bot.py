import discord
from discord.ext import commands
from botlogic import pass_gen

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passgen(ctx):
    await ctx.send("Ini Adalah Password Barumu:")
    await ctx.send(pass_gen(10))   

@bot.command()
async def pangkat(ctx):
    await ctx.send('Masukkan angka yang ingin dipangkatkan 2') 
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f'Pangkat 2 dari angka yang telah dimasukkan adalah {(int(message.content)**2)}')   

client = MyClient(intents=intents)
client.run('')
