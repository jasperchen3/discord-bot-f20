import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.command()
async def ping(ctx):
    await ctx.send('pong')

'''
Outputs to the console once a connection is made with the discord server and
the bot changes the on_ready boolean to True.
'''
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name='DiscordBotF20')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

'''
Sends a direct message to a new user joining the channel.
'''
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Discord_Bot_F20!'
    )

'''
The bulk of the 'Dad Bot'. Reponds to all messages that contains the phrases
"I'm", "I'm dad", or "shut up".
'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    index_of_im = message.content.lower().find('i\'m ')
    if 'shut up' in message.content.lower():
        response = f'Listen here {message.author.mention}, I will not tolerate you saying the words ' +\
        'that consist of the letters \'s h u t u p\' being said in this server, so take your ' +\
        'own advice and close thine mouth. :rage:'
        await message.channel.send(response)
    elif 'i\'m dad' in message.content.lower() or 'im dad' in message.content.lower():
        response = 'You\'re not Dad, I am! :thinking:'
        await message.channel.send(response)
    elif index_of_im != -1:
        response = 'Hi ' + message.content[index_of_im + 4:] + ', I\'m Dad! :laughing:'
        await message.channel.send(response)

    await client.process_commands(message)

'''
Has the bot output a simple embed.
Output 1: Chow chow
'''
@client.command()
async def displayembedtest(ctx):
    file = discord.File("C:\\Users\\nehcr\\test_image\\chowchow.jpg", filename="chowchow.jpg")
    emb = discord.Embed(
        title = 'Chowder',
        description = 'Might not be the goodest girl, but definitely the fluffiest.',
        colour = discord.Colour.blue()
    )

    emb.set_footer(text = 'Fully grown dogs have blue-black tongues that almost look lizard-like.')
    emb.set_image(url = 'attachment://chowchow.jpg')
    emb.set_thumbnail(url = client.user.avatar_url)
    emb.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    emb.add_field(name = 'Gender', value = 'Female', inline = True)
    emb.add_field(name = 'Age', value = '2 years, 5 months', inline = True)
    emb.add_field(name = 'Weight', value = '50 lbs.', inline = True)
    emb.add_field(name = 'Hair Color', value = 'Gold, White', inline = True)
    emb.add_field(name = 'Likes', value = 'Eating chimken', inline = True)
    emb.add_field(name = 'Dislikes', value = 'Staying home alone', inline = True)

    await ctx.send(file = file, embed = emb)

'''
Has the bot output a simple embed.
Output 2: Labradoodle
'''
@client.command()
async def displayembedtest2(ctx):
    file = discord.File("C:\\Users\\nehcr\\test_image\\fendi.jpeg", filename="fendi.jpeg")
    emb = discord.Embed(
        title = 'Fendi',
        description = 'heehee',
        colour = discord.Colour.blue()
    )

    emb.set_footer(text = 'The first one was bred in Australia in 1988 by crossing a Labrador and a Poodle.')
    emb.set_image(url = 'attachment://fendi.jpeg')
    emb.set_thumbnail(url = client.user.avatar_url)
    emb.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    emb.add_field(name = 'Gender', value = 'Female', inline = True)
    emb.add_field(name = 'Age', value = '1 year old', inline = True)
    emb.add_field(name = 'Weight', value = '20 lbs.', inline = True)
    emb.add_field(name = 'Hair Color', value = 'Tan, White', inline = True)
    emb.add_field(name = 'Likes', value = 'Fighting big dog', inline = True)
    emb.add_field(name = 'Dislikes', value = 'The house', inline = True)

    await ctx.send(file = file, embed = emb)


client.run([TOKEN])
