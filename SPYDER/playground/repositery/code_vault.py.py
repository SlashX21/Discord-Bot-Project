@bot.command()
async def ban(ctx, member : discord.Member, reason=None):
    youbadbad = f"You are banned by {ctx.author.mention} because you bad bad"
    await member.send(youbadbad)
    await member.ban(reason=reason)
    
@bot.command()
async def unban(ctx, *, member):
    banned_list = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_list:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return     