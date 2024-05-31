import discord
import os
import random
from discord.ext import commands
from botlogic import pass_gen


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

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)

@bot.command()
async def meme(ctx):
    import random, os
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)    

def get_duck_image_url():    
    import requests
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)    

@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir('animals'))
    with open(f'animals/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

daur_ulang = [
    "Botol plastik", "Kaleng aluminium", "Kertas", "Karton", "Botol kaca",
    "Kemasan makanan", "Sampah elektronik", "Kain bekas", "Botol deterjen",
    "Barang pecah belah", "Barang dari baja", "Kantong belanja", "CD dan DVD bekas",
    "Baterai", "Karet bekas", "Kayu bekas", "Lampu bekas", "Kardus bekas",
    "Mainan bekas", "Pakaian bekas", "Tas plastik", "Ember plastik", "Papan reklame",
    "Perabotan tua", "Kunci bekas", "Tali rafia", "Botol plastik", "Barang dari logam",
    "Kaleng cat"
]

@bot.command()
async def cek_sampah(ctx):
    await ctx.send('Apa sampah yang anda mau periksa?')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    sampah = message.content.lower().strip()


    for item in daur_ulang:
        if sampah == item.lower().strip():
            await ctx.send('Sampah tersebut haruslah di daur ulang, berikut tips untuk mendaur ulang!')
            await ctx.send('https://arahenvironmental.com/7-tips-untuk-memulai-kebiasaan-daur-ulang-sampah-sendiri/')
            return
    await ctx.send('Sepertinya sampah itu tidak dapat anda daur ulang')   
bot.run('YOUR_BOT_TOKEN')

