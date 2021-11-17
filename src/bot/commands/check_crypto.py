from discord.ext.commands import Bot
from discord import Embed
from discord import Color
from src.request import check_crypto_values


def load_check_crypto(bot: Bot):
    @bot.command(name='crypto', help='Returns the price in USD of the specified cryptos')
    async def check_crypto(ctx, *args):
        try:
            results = check_crypto_values(list(args))

            for item in results:

                embed = __build_embed__(bot, item)

                await ctx.channel.send(embed=embed)

        except Exception as error:

            print(error)

            await ctx.channel.send('Call to api failed :sob:')


def __build_embed__(bot: Bot,response: dict) -> Embed:
    embed = Embed(title=response['id'],
                  description=response['name'],
                  color=Color.green())

    embed.set_author(name=bot.user.display_name, icon_url=bot.user.avatar_url)

    embed.set_thumbnail(url=response['logo'])

    embed.add_field(name='Price',
                    value=f'{response["price"]} USD',
                    inline=False)

    embed.add_field(name='Status',
                    value=response['status'],
                    inline=False)

    embed.add_field(name='Price Date',
                    value=response['price_date'],
                    inline=False)

    print(response['logo'])

    return embed



