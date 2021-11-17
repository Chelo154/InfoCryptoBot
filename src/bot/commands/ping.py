from discord.ext.commands import Bot


def load_ping(bot: Bot):
    @bot.command(name='ping', help='The bot will response pong after this')
    async def ping(ctx):
        await ctx.channel.send('pong')


