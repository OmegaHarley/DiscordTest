import discord
from discord.ext import commands
random = __import__("random")

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Bit Heroes'))
    print('Il bot è pronto e funzionante.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def fire(ctx):
    responses = ['https://i.kym-cdn.com/photos/images/newsfeed/001/505/718/136.jpg', #gattoschifomado
                 'https://res.cloudinary.com/lmn/image/upload/c_limit,h_360,w_640/e_sharpen:100/f_auto,fl_lossy,q_auto/v1/gameskinnyc/b/i/t/bit-heroes-skeleton-key-0dd37.png', #bit heroes
                 'https://imgur.com/a/zNHwlcp', #imgur bhchiesa crossover 
                 'https://imgur.com/a/J9iUd5L', #notre chiesa bh
                 'https://cdn02.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_download_software_1/H2x1_NSwitchDS_Warframe_image1600w.jpg'] #warframe
    await ctx.send(random.choice(responses))

@client.command()
async def rose(ctx):
    responses = ['https://i.kym-cdn.com/photos/images/original/000/862/912/fdf.gif', #anime ass
                 'https://media.giphy.com/media/6CBGoJnEBbEWs/giphy.gif', #red taiga
                 'https://media.giphy.com/media/jTU09JLRaYCt2/giphy.gif', #taiga sfrontata
                 'https://media.giphy.com/media/wUf0jPd2ksY92/giphy.gif', #jojo balls
                 'https://media.giphy.com/media/gDciyiNcDhYXu/giphy.gif', #ohmygod joo reference
                 'https://i.kym-cdn.com/photos/images/newsfeed/000/869/852/a28.gif', #n'altro culo
                 'https://i.pinimg.com/originals/d5/8b/5b/d58b5be495a07dfda4672aaf7aa2e35b.gif', #donnasenzabocce
                 'https://media.giphy.com/media/SpzdWtMmREEaA/giphy.gif'] #taiga felice
    await ctx.send(random.choice(responses))

@client.command()
async def cappu(ctx):
    responses = ['https://tenor.com/y8kZ.gif', #ragazzo cool
                'https://tenor.com/rpCn.gif'] #sguardo sexy
    await ctx.send(random.choice(responses))

@client.command()
async def arty(ctx):
    responses = ['Lasciami stare',
                 'Vuoi un ban?',
                 'https://media.giphy.com/media/uC9e2ojJn1ZXW/giphy.gif',
                 'https://media.giphy.com/media/qPD4yGsrc0pdm/giphy.gif',
                 'Sono pigro daiiii']
    await ctx.send(random.choice(responses))

@client.command()
async def nic(ctx):
    await ctx.send('https://media.giphy.com/media/3h40Gfu1mwk5xFAfcN/giphy.gif') #hanzo

@client.command()
async def eva(ctx):
    await ctx.send('Sei bello Rose!')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print(author, content)
    await client.process_commands(message)


@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(
        color = discord.Colour.blue()  
    )
    
    embed.set_author(name='Help')
    embed.add_field(name = '.rose', value = 'Le migliori gif di Rose', inline=False)
    embed.add_field(name = '.arty', value = 'Il meglio di Arty', inline=False)
    embed.add_field(name = '.cappu', value = 'Le migliori gif di Cappu', inline=False)
    embed.add_field(name = '.fire', value = 'Le migliori gif di Firemage', inline=False)
    embed.add_field(name = '.eva', value = 'La frase meno iconica di Evan', inline=False)
    embed.add_field(name = '.nic', value = 'La miglior gif di Nic', inline=False)
    embed.add_field(name = '.ping', value = 'Controlla quanto lagga Arty', inline=False)
    embed.add_field(name = 'Il bot è semplice e sviluppato col culo, abbiate pazienza.', value = 'Imparerò a programmare, lo giuro', inline=False)
    
    await ctx.send(embed=embed)


client.run('NjExODQ5MTkzMTM2NTg2NzYz.XVh6_Q.bQaygaWd9PY3Rb4mchRxeXN8uR4')