import discord
from discord.ext import commands

TOKEN = 'NzM1MjE2MDE1ODY0MTAzMDAy.XxdBRQ.XHoCV3ssuWtDrOThw7KjIILCMnk'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def бот_ты(ctx, arg):  # создаем асинхронную фунцию бота
    if arg == "тыгей":
        await ctx.send('нет ты')
    else:
        await ctx.send("нет ты " + arg)  # отправляем обратно аргумент


bot.run(TOKEN)
