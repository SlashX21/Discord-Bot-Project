@bot.command()
async def countdown(ctx):
    await ctx.send("What event is this timer built for")
    event_name = await self.bot.wait_for('message', check=check)
    await ctx.send("how long from now is this event going to be?(day/hours/min") 
    time = await self.bot.wait_for('message', check=check)
    await ctx.send(f'you will have {event_name} in {time}')
    days, hours, minutes = time_left.split("/")
    time_left = days * 86400 + hours * 3600 + minutes * 60
    days_left = time_left//86400
    hours_left = (time_left - days_left*86400)//3600
    minutes_left = (time_left - days_left*86400 - hours_left*3600)//60
    while time_left>0:
        ctx.send(f'{days_left}days {hours_left}hours {minutes_left}minutes left to {event_name}.')
        time_left -= 60
    await asyncio.sleep(60)
@bot.command()
async def countdown1(ctx):
    await ctx.send("What event is this timer built for")
    event_name = await bot.wait_for('message')
    await ctx.send("how many days is that from now?")
    days = await bot.wait_for('message')
    await ctx.send("What hour will that be?(24hours format)")
    hours = await bot.wait_for('message')
    await ctx.send("At which minute you want the alarm to ring?")
    minutes = await bot.wait_for('message')
    await ctx.send(f'you will have {event_name} in {days}day(s) {hours}hour(s) {minutes}minutes(s)')
    time_left = f'{days}' * 86400 + f'{hours}' * {3600} + f'{minutes}' * 60
    days_left = f'{time_left}'//86400
    hours_left = (f'{time_left}' - f'{days_left}'*86400)//3600
    minutes_left = (f'{time_left}' - f'{days_left}'*86400 - f'{hours_left}'*3600)//60
    while time_left>0:
        ctx.send(f'{days_left}days {hours_left}hours {minutes_left}minutes left to {event_name}.')
        time_left -= 60
    await asyncio.sleep(60)
@bot.command()
async def countdown(ctx, arg1, arg2, arg3, arg4, arg5, arg6):
    if 'min' in arg6:
        time1 = (int(arg5)*60)
    if 'hour' in arg4:
        time2 = (int(arg3)*360)
    if 'day' in arg2:
        time3 = (int(arg1)*8640)
    time4 = time1 + time2 + time3
    await asyncio.sleep(time4)
    await ctx.send('Time is up')
    if time4>0:
        ctx.send('a minute pass')
        await asyncio.sleep(60)