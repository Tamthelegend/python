#Imports
import discord
from discord.ext import commands
import random
from discord.reaction import Reaction
from discord import User
import asyncio
from dotenv import load_dotenv



#Variables
load_dotenv(os.path.join(os.getcwd(), '.env'))
bot = commands.Bot(command_prefix = PREFIX)
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")



#Bot OnReady Event

@bot.event
def load_extensions():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

async def on_ready():
    print('logged on as')
    print(bot.user.name)
    print(bot.user.id)
    print("test")
    load_extensions() 



#Bot Run Event
@bot.command()
async def ping(ctx):
    await ctx.send("raised")

@bot.command()
async def test(ctx):
    await ctx.send("test")



@bot.command()
async def register(ctx,name : str):
    await ctx.send("name registered as " + "trainer " + "`" + name + "`" + "!")









@bot.command()
async def maths(ctx,n1 : float,type : str, n2 : float,round : str):
    if type == "+":
        await ctx.send(n1+n2)
    if type == "-":
        await ctx.send(n1-n2)
    if type == "/":
        await ctx.send(n1/n2)
    if type == "*":
        await ctx.send(round(n1*n2))
        
@bot.command()
async def author(ctx):
    await ctx.send(ctx.message.author)

@bot.command()
async def server(ctx):
    await ctx.send(ctx.guild)

@bot.command()
async def channel(ctx):
    await ctx.send(ctx.message.channel)


@bot.command()
async def pfp(ctx):
    await ctx.send(ctx.message.author.avatar_url)

@bot.command()
async def react(ctx, pog):
    t = await ctx.send("reacting...")
    if pog == "troll":
        await t.add_reaction("<:trollololol:842127808162955274>")
    if pog == "pog":
        await t.add_reaction("<:pog:730280874204987442>")

@bot.command()
async def reactme(ctx):
    def checkvalid(reaction : Reaction, user : User):
        return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id
    await ctx.send("Quick! React to this message!")
    
    try:
        reaction, user = await bot.wait_for(event = 'reaction_add', check = checkvalid, timeout = 10.0)
    except asyncio.TimeoutError:
        await ctx.send("noob can't even add reaction in 10 sec")
        return
    else:
        await ctx.send("You reacted in time!")
@bot.command()
async def rps(ctx):
    b = random.randint(0,2)
    def checkvalid(reaction : Reaction, user : User):
        return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id
    c = await ctx.send("🥌 = rock,   📜 = paper, ✂ = scissor ")
    await c.add_reaction("📜")
    await c.add_reaction("🥌")
    await c.add_reaction("✂")
    print(b)

    try:
        t = reaction, user = await bot.wait_for(event = 'reaction_add', check = checkvalid, timeout = 10.0)

        if b == 0:
            if str(reaction.emoji) == "📜":
                e = discord.Embed(title="i lost :c", description="I picked", type = "image", color=0x00ff00)
                e.set_image(url = "https://static.wikia.nocookie.net/minecraft/images/d/d4/Stone.png/revision/latest?cb=20200825201332")
                await ctx.send(embed=e)
            if str(reaction.emoji) == "🥌":
                e = discord.Embed(title="well i didnt win, but neither did you", description="I picked",type = "image", color=0x00ff00)
                e.set_image(url = "https://static.wikia.nocookie.net/minecraft/images/d/d4/Stone.png/revision/latest?cb=20200825201332")
                await ctx.send(embed=e)
            if str(reaction.emoji) ==  "✂":
                e = discord.Embed(title="haha loser", description="I picked",type = "image", color=0x00ff00)
                e.set_image(url = "https://static.wikia.nocookie.net/minecraft/images/d/d4/Stone.png/revision/latest?cb=20200825201332")
                await ctx.send(embed=e)
        if b == 1:
            if str(reaction.emoji) == "📜":
                e = discord.Embed(title="well i didnt win, but neither did you", description="I picked", type = "image", color=0x00ff00)
                e.set_image(url = "https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f2/Paper_JE2_BE2.png/revision/latest/scale-to-width-down/160?cb=20190606162534")
                await ctx.send(embed=e)
            if str(reaction.emoji) == "🥌":
                e = discord.Embed(title="haha loser", description="I picked", type = "image", color=0x00ff00)
                e.set_image(url = "https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f2/Paper_JE2_BE2.png/revision/latest/scale-to-width-down/160?cb=20190606162534")
                await ctx.send(embed=e)
            if str(reaction.emoji) ==  "✂":
                e = discord.Embed(title="i lost :c", description="I picked", type = "image", color=0x00ff00)
                e.set_image(url = "https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f2/Paper_JE2_BE2.png/revision/latest/scale-to-width-down/160?cb=20190606162534")
                await ctx.send(embed=e)

        if b == 2:
            if str(reaction.emoji) == "📜":
                e = discord.Embed(title="haha loser", description="I picked", color=0x00ff00)
                e.set_image(url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.collinsdictionary.com%2Fdictionary%2Fenglish%2Fscissors&psig=AOvVaw2om_A5soWC2ijGd3g8o-W5&ust=1632034461397000&source=images&cd=vfe&ved=0CAkQjRxqFwoTCJCh0ab4h_MCFQAAAAAdAAAAABAD")
                await ctx.send(embed=e)
            if str(reaction.emoji) == "🥌":
                e = discord.Embed(title="i lost :c", description="I picked", color=0x00ff00)
                e.set_image(url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.collinsdictionary.com%2Fdictionary%2Fenglish%2Fscissors&psig=AOvVaw2om_A5soWC2ijGd3g8o-W5&ust=1632034461397000&source=images&cd=vfe&ved=0CAkQjRxqFwoTCJCh0ab4h_MCFQAAAAAdAAAAABAD")
                await ctx.send(embed=e)
            if str(reaction.emoji) == "✂":
                e = discord.Embed(title="well i didnt win, but neither did", description="I picked", color=0x00ff00)
                e.set_image(url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.collinsdictionary.com%2Fdictionary%2Fenglish%2Fscissors&psig=AOvVaw2om_A5soWC2ijGd3g8o-W5&ust=1632034461397000&source=images&cd=vfe&ved=0CAkQjRxqFwoTCJCh0ab4h_MCFQAAAAAdAAAAABAD")
                await ctx.send(embed=e)
    except asyncio.TimeoutError:
        await ctx.send("noob can't even add reaction in 10 sec")
        return


@bot.command()
async def embed(ctx):
    e = discord.Embed(title="Title", description="Desc", type = "image", color=0x00ff00)
    e.set_image(url = "https://static.wikia.nocookie.net/minecraft/images/d/d4/Stone.png/revision/latest?cb=20200825201332")
    await ctx.send(embed=e)

bot.run(token)


