import discord
from discord.ext import commands



##purge command

@client.command(aliases=['clear'])
@commands.has_permissions(manage_messages = True)
async def purge (ctx,amount=2):
  await ctx.channel.purge(limit= amount)


##kick and b

# command for kick users.
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason):
    await user.kick(reason='')

# command for ban users.
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason):
    await user.ban(reason)
