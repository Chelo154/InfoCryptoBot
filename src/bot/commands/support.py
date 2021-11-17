from discord.ext.commands import Bot
from discord import Color, Embed


def load_support(bot: Bot):
    @bot.command(name='support', help='Support this project by giving a donation :smile:')
    async def support(ctx):
        embed = __build_embed__(bot)

        await ctx.channel.send(embed=embed)


def __build_embed__(bot: Bot) -> Embed:
    embed = Embed(title='Support Project!!', description='Thank you for support this project, you can make a donation '
                                                         'via ceneka', color=Color.gold())

    embed.set_author(name='cheavlo154', icon_url='https://i.ibb.co/QM960vb/Perfil.jpg', url='github.com/chelo154')

    embed.add_field(name='Developed by', value='@chelo154 (github.com/chelo154)')

    embed.add_field(name='Support', value='You can donate via ceneka clicking here -> https://ceneka.net/chelo154')

    embed.add_field(name='Contact', value='For feedback and new ideas you can contact me via e-mail '
                                          'mdjnunez9706@gmail.com')

    embed.set_thumbnail(url=bot.user.avatar_url)

    return embed
