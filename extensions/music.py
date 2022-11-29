import lightbulb, hikari

plugin = lightbulb.Plugin('Music')

@plugin.command
@lightbulb.option('link', 'YouTube URL', type=str)
@lightbulb.command('play', 'Plays a video from YouTube')
@lightbulb.implements(lightbulb.SlashCommand)
async def play(ctx):
    await ctx.respond(ctx.options.link)

def load(bot):
    bot.add_plugin(plugin)

