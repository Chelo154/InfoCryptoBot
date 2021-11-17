from discord.ext.commands import Bot
from discord import Embed
from discord import Color
from src.request import check_crypto_info


def load_info_crypto(bot: Bot):
    @bot.command(name='about', help='return information about a crypto currency project')
    async def info_crypto(ctx, *args):
        try:
            crypto_data = check_crypto_info(list(args))

            for crypto in crypto_data:

                embed = __build__embed(crypto)

                await ctx.channel.send(embed=embed)

        except Exception as error:
            print(error)

            await ctx.channel.send('Called failed :sob:')


def __build__embed(crypto: dict) -> Embed:
    embed = Embed(title=f'{crypto["name"]} data', color=Color.blue())

    embed.set_thumbnail(url=crypto['logo'])

    embed.add_field(name='Symbol', value=crypto['id'])

    embed.add_field(name='Description',
                    value=crypto['description'].split('.')[0],
                    inline=False)

    embed.add_field(name='Website',
                    value=crypto['website'],
                    inline=False)

    embed.add_field(name='Discord',
                    value=crypto['discord'] if crypto['discord'] != '' else 'Unknown',
                    inline=False)

    embed.add_field(name='Facebook',
                    value=crypto['facebook'] if crypto['facebook'] != '' else 'Unknown',
                    inline=False)

    embed.add_field(name='Twitter',
                    value=crypto['twitter'] if crypto['twitter'] != '' else 'Unknown',
                    inline=False)

    embed.add_field(name='Github',
                    value=crypto['github'] if crypto['github'] != '' else 'Unknown',
                    inline=False)

    return embed
