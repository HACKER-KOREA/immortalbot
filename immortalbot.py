import asyncio
import discord
import os


from discord.ext import commands

app = commands.Bot(command_prefix='=')
client = commands.Bot(command_prefix = '=')

calcResult = 0
calcResult1 = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("24h host powerd by HEROKU")
    await app.change_presence(status=discord.Status.online, activity=game)





@app.event
async def on_message(message):
    await app.process_commands(message)

    if message.content.startswith("=계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                await message.channel.send("결과 : "+str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                await message.channel.send("결과 : "+str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                await message.channel.send("결과 : "+str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                await message.channel.send("결과 : "+str(calcResult))
        except IndexError:
            await message.channel.send("무슨 숫자를 계산할지 알려주세요.")
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("0으로 나눌수 없습니다.")


    if message.content.startswith("=calc"):
        global calcResult1
        param = message.content.split()
        try:
            if param[1].startswith("plus"):
                calcResult1 = int(param[2])+int(param[3])
                await message.channel.send("Result : "+str(calcResult1))
            if param[1].startswith("minus"):
                calcResult1 = int(param[2])-int(param[3])
                await message.channel.send("Result : "+str(calcResult1))
            if param[1].startswith("multiply"):
                calcResult1 = int(param[2])*int(param[3])
                await message.channel.send("Result : "+str(calcResult1))
            if param[1].startswith("devide"):
                calcResult1 = int(param[2])/int(param[3])
                await message.channel.send("Result : "+str(calcResult1))
        except IndexError:
            await message.channel.send("tell me what number to calculate.")
        except ValueError:
            await message.channel.send("this is not a number.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")

    if message.content.startswith("=commands"):
        embed = discord.Embed(title="Commands | 명령어", color=0x00ff56)
        embed.set_thumbnail(
            url="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/91_Discord_logo_logos-512.png")
        embed.add_field(name="command help", value="=help commands", inline=True)
        embed.add_field(name="명령어", value="=help commands", inline=True)
        embed.add_field(name="building command", value="music player", inline=True)
        embed.add_field(name="개발중인 명령어", value="음악 재생 기능", inline=True)
        embed.set_footer(text="IMMORTALBOT")
        await message.channel.send(embed=embed)

    @app.command(name="따라하기", pass_context=True)
    async def _saySame(ctx, args):
        await ctx.send(args)\

    @app.command(name="followme", pass_context=True)
    async def _saySame(ctx, args):
        await ctx.send(args)

        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel  # 채널 구하기
            await channel.connect()

    @app.command(name="참가", pass_context=True)
    async def _join(ctx):
        if ctx.author.voice and ctx.author.voice.channel:  # 채널에 들어가 있는지 파악
            channel = ctx.author.voice.channel  # 채널 구하기
            await channel.connect()  # 채널 연결
        else:  # 유저가 채널에 없으면
            await ctx.send("채널에 연결되지 않았습니다.")  # 출력

    await app.voice_clients[0].disconnect()


    @app.command(name="연결끊기")
    async def _leave(ctx):  # ctx를 안 써도 ctx가 필요하다는 사실을 잊지 마세요.
        await app.voice_clients[0].disconnect()  # 목록의 첫 번째 채널에서 나가기

    @app.command(name="join", pass_context=True)
    async def _join(ctx):
        if ctx.author.voice and ctx.author.voice.channel:  # 채널에 들어가 있는지 파악
            channel = ctx.author.voice.channel  # 채널 구하기
            await channel.connect()  # 채널 연결
        else:  # 유저가 채널에 없으면
            await ctx.send("user is not connected to channel.")  # 출력

    await app.voice_clients[0].disconnect()


    @app.command(name="disconnect")
    async def _leave(ctx):  # ctx를 안 써도 ctx가 필요하다는 사실을 잊지 마세요.
        await app.voice_clients[0].disconnect()  # 목록의 첫 번째 채널에서 나가기




access_token = os.environ["BOT_TOKEN"]
app.run(access_token)