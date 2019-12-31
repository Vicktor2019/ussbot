import discord
from discord.ext import commands 
import random
from discord.ext.commands import Bot
from random import choice
import asyncio
import datetime
from itertools import cycle
import os

prefix = '/'

Bot = commands.Bot(command_prefix= prefix)

Bot.remove_command('help')

        

@Bot.event
async def on_ready():
    await Bot.change_presence(status=discord.Status.idle, activity=discord.Game('Uniform Samp Server (by V.Bag)'))
    print("Bot is online")


@Bot.command(pass_context= True)
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.mention))


@Bot.command(pass_context= True)
async def info(ctx, member: discord.Member):
    """Информация о юзере """
    emb = discord.Embed(title= "Информация о {}".format(member.name), colour= 0x39d0d6)
    emb.add_field(name= "Ник", value= member.name)
    emb.add_field(name= "ID юзера", value= member.id)
    emb.add_field(name= "Создал аккаунт", value= str(member.created_at)[:16])
    emb.add_field(name= "Вошёл на сервер", value= str(member.joined_at)[:16])
    emb.set_thumbnail(url= member.avatar_url)
    emb.set_author(name= "Bot USS", url= member.avatar_url)
    emb.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

    

@Bot.command(pass_context= True)
async def aboutserver(ctx):
    """Приветствие"""
    emb = discord.Embed(title= "Добро пожаловать на офф. дискорд сервер :radioactive: Uniform Samp Server :radioactive:", description= "`Доброго времени суток, приветствуем Вас на discord-сервере USS.`                                                        `Тематика нашего сервера - SAMP&CRMP, но мы будем рады игрокам и прочих игр.`                                       `Желаем Вам приятного времяпровождения, в нашей дружной компании.`                                                   `С уважением, USS Team.`", colour= 0x39d0d6)
    emb.set_image(url= "https://i.imgur.com/wYO2dTc.jpg")
    emb.set_footer(text= "USS Bot • 20.12.2019", icon_url= Bot.user.avatar_url)
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def rules(ctx):
    """Правила"""
    emb = discord.Embed(title= "Правила Discord-сервера USS.", description= "`Запрещено следующее: flood, caps, offtopic, spam, нецензурная лексика, завуалированный мат, розжиг, неадекватное поведение, оскорбление чувств и/или унижение достоинства другого пользователя, оскорбление и/или  упоминание родных. Запрещено распространение личной информации, реклама сторонних ресурсов/Discord серверов. Запрещены массовые упоминания, упоминания без причины. Запрещена порнография в любых её проявлениях. Запрещены любые проявления оскорблений в NickName.`", colour= 0x39d0d6)
    emb.add_field(name= "**Незнание правил не освобождает вас от ответственности, при присоединении к серверу вы даёте согласие с данными правилами. Модератор сам определяет меру наказания.**", value= "С уважением, USS Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/wYO2dTc.jpg")
    emb.set_footer(text= "USS Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def predlog(ctx):
    """Правила"""
    emb = discord.Embed(title= "Предложения по улучшению Discord-сервера USS.", description= "`Доброго времени суток, уважаемые участники USS. Если у Вас есть предложения по улучшению и развитию нашего Discord-сервера, Вы можете изложить их в этом канале. Рассматриваются любые разумные предложения и нововведения.`", colour= 0x39d0d6)
    emb.add_field(name= "**В данном канале запрещенны любые проявления offtop`a. Форма подачи предложения по улучшению свободная, главное чёткое и обоснованое объяснение цели и необходимость нововведения.**", value= "С уважением, USS Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/wYO2dTc.jpg")
    emb.set_footer(text= "USS Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def meme(ctx):
    """Правила"""
    emb = discord.Embed(title= "Screenshots and Memes.", description= "`Доброго времени суток, уважаемые участники USS. Если у Вас имееться множество интересных или смешных скриншотов касаемых SAMP'a и прочих игр, Вы можете поделиться этим в этом текстовом канале. `", colour= 0x39d0d6)
    emb.add_field(name= "**Offtop/flood в данном канале карается длительным mute`ом.**", value= "С уважением, USS Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/wYO2dTc.jpg")
    emb.set_footer(text= "USS Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def razdat(ctx):
    emb = discord.Embed(title= "Раздачи и конкурсы", description= f'`Доброго времени суток, уважаемые участники USS. В данном текстовом канале будут проходить разнообразные раздачи (Giveaway) и конкурсы. Спонсором раздач игровой валюты на сервере Diamond RP Amber будет` {ctx.author.mention}', colour= 0x39d0d6)
    emb.add_field(name= f"**Если Вы хотите стать спонсором или организатором любой раздачи либо конкурса, будь то раздача игровой валюты на любом сервере, отписывайте модераторам USS Team.**", value= "С уважением, USS Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/wYO2dTc.jpg")
    emb.set_footer(text= "USS Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)


@Bot.command(pass_context= True) 
async def help(ctx): 
    emb = discord.Embed(title= "Команды", colour= 0x39d0d6)
    emb.add_field(name= "Информация про команды", value= "`{}help`".format(prefix))
    emb.add_field(name= "Проверить ping", value= "`{}ping`".format(prefix))
    emb.add_field(name= "Игра Coin", value= "`{}coin`".format(prefix))
    emb.add_field(name= "Посмотреть аватарку юзера", value= "`{}avatar @username`".format(prefix))
    emb.add_field(name= "Игра 8-ball", value= "`{}ball`".format(prefix))
    emb.add_field(name= "Правила сервера", value= "`{}rules`".format(prefix))
    emb.add_field(name= "Информация о юзере", value= "`{}info @username`".format(prefix))
    emb.add_field(name= "Команды для модератора:", value= "`/petuh`,`/say <channel> <text>`,`/update_channel <channel>`,`/update_channel2 <channel>`,`/giveaway <channel> <msgid>`,`/cmd`", inline=True)
    emb.set_image(url= "https://i.imgur.com/wYO2dTc.jpg")
    emb.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command()
@commands.has_permissions(administrator = True) 
async def say(ctx, channel: discord.TextChannel, *, cnt):
   await ctx.message.delete() 
   embed = discord.Embed(description = cnt, colour = 0x00ff80) 
   await channel.send(embed=embed) 

@Bot.command(pass_context=True, name= 'ping', brief= 'Показать текущую задержку')
@commands.cooldown(1, 1, commands.BucketType.user)
async def ping(ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        emb = discord.Embed(title= '**Текущая задержка:**', description= f'``{Bot.ws.latency * 1000:.0f} ms``', colour= 0x00ff80)
        emb.set_author(name= f'Ping', icon_url= Bot.user.avatar_url)
        emb.set_footer(text= f'{ctx.author}', icon_url= ctx.author.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)

@commands.has_permissions(administrator=True)
@Bot.command()
async def petuh(ctx):

    role = ctx.guild.get_role(657904038913900573) 

    balbes = "Ghetto Петухов"
    bot = "бота"
    bots = "бота"
    member = "участников"
    members = "участников"

    members_counter = len(ctx.guild.members)
    role_counter = len([m for m in ctx.guild.members if role in m.roles])
    bots_counter = len([m for m in ctx.guild.members if m.bot])
    valid_members = [m for m in ctx.guild.members if not m.bot and role not in m.roles]

    if members_counter - bots_counter < 2:
        return await ctx.send(f'{ctx.author.mention} Ты один на сервере, {"не считая меня!" if bots_counter == 1 else f"не считая {bots_counter} {bot}!"}')

    elif not valid_members:
        return await ctx.send('**ой, все пользователи уже Ghetto Петушня!** :smirk:')

    elif len(valid_members) is 1:
        await ctx.send(f'{ctx.author.mention} Ну тут выбор очевиден! На сервере остался только один человек без роли :smirk:')
        random_member = valid_members[0]
    else:
        await ctx.send(f'{ctx.author.mention} Немного подожди, я выбераю рандомного Ghetto Петуха среди **{members_counter}** {member}! :smirk:'
                       f'\nА если быть точнее то из **{members_counter - bots_counter - role_counter}**, т.к на сервере ' + \
                       (f'**{bots_counter}** {bots}' if bots_counter > 1 else 'есть я, а я не считаюсь') + \
                       f' и у **{role_counter}** {members} уже есть роль!')

        try:
            await asyncio.sleep(5)
            random_member = choice(valid_members)
            await random_member.add_roles(role)
        except Exception as error:
            return await ctx.send(f'**Произошло GG **{type(error).__name__}**:\n{error}')

    embed = discord.Embed(
        color=0x99ff99,
        description=f'Роль {role.mention} присуждается {random_member.mention}\nТеперь на сервере **{role_counter + 1}** {balbes}')
    embed.set_footer(text= f"Вызвал(а): {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    await ctx.send(embed=embed)


@Bot.command()
async def avatar(ctx, member : discord.Member = None):
    user = ctx.message.author if (member == None) else member
    await ctx.message.delete()
    embed = discord.Embed(title=f'Аватар пользователя {user}', description= f'[Ссылка на изображение]({user.avatar_url})', color=user.color)
    embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    embed.set_image(url=user.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@Bot.command()
async def coin(ctx):
    num=random.randint(1,2)
    if (num == 1):
           await ctx.send("Вым выпал - Орёл")
           print("[?coin] - done")
    if(num == 2):    
           await ctx.send("Вам выпала - Решка")
           print("[?coin] - done")
        
@Bot.command()
async def ball(ctx):
    num=random.randint(1,4)
    if (num == 1):
           await ctx.send("Однозначно - да :ok_hand_tone5: ")
           print("[?coin] - done")
    if(num == 2):    
           await ctx.send("Мой ответ - нет :thumbsdown_tone5: ")
           print("[?coin] - done")
    if (num == 3):
           await ctx.send("Скорее всего :smiling_imp: ")
           print("[?coin] - done")
    if (num == 4):
           await ctx.send("Даже не думай :skull_crossbones: ")
           print("[?coin] - done")


@Bot.command()
@commands.has_permissions(administrator = True) 
async def cmd(ctx):
    await ctx.message.delete() 
    role = ctx.guild.get_role(656579155479232513) 
    emb = discord.Embed(title= "GIVEAWAY начат", description=f" {role.mention} **Для участия нажмите на реакцию ниже. Приз: 100.000$. Результат через 23 часа.**", color=0x99ff99)
    emb.set_footer(text= f"Cпонсор: {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=emb) 

@Bot.command()
@commands.has_permissions(administrator = True) 
async def giveaway(ctx, channel: discord.TextChannel, msgid: int):
    await ctx.message.delete() 
    await asyncio.sleep(82800)
    message = await channel.fetch_message(msgid)
    users = set([user for reaction in message.reactions for user in await reaction.users().flatten()])
    random_member = random.sample(users, 1)[0] 
    emb = discord.Embed(title= "GIVEAWAY закончен", description=f"**Участник {random_member.mention} выиграл приз! Поздравляем!**", color=0x99ff99)
    emb.set_footer(text= f"Cпонсором был: {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=emb)


@Bot.command()
async def update_channel(ctx, channel: discord.VoiceChannel, *, new_name):
 members_counter = len(ctx.guild.members)
 channel = Bot.get_channel(658049586501255168)
 await channel.edit(name=f" 📌 Нас: {members_counter}")

@Bot.command()
async def update_channel2(ctx, channel: discord.VoiceChannel, *, new_name):
 guild=ctx.message.guild
 total_text_channels = len(guild.text_channels + guild.voice_channels)
 channel = Bot.get_channel(658058242559311882)
 await channel.edit(name=f" 📌 Всего каналов: {total_text_channels}")



token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
