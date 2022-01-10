class movies:
    """topic for quiz bot"""

    def __init__(movie, questions, answer):
        movie.questions = questions
        movie.answer = answer

Q1 = movies("Who's the actor for Captain Jack Sparrow in Pirates of the Caribbean?","Johnny Depp")

print(Q1.questions)


    while game_timer>0:
        game_timer -= 1
        await asyncio.sleep(1)
        while game_timer<11 and game_timer>0:
            await ctx.send(f'You have {game_timer} seconds left!')
    else:
        await ctx.send(f'Your marks is {player_score}')
    while game_timer > 0:
        a = randint(1, 50)
        b = randint(1, 50)
        c = a + b
        question = f'{a}+{b}=?'
        embed = discord.Embed(title=f'Countdown: {game_timer}',description=question)
        await ctx.send(embed=embed)
        reply = await bot.wait_for("message")
        if reply.content == c:
            game_timer += 10
            player_score += 1
        else:
            game_timer -= 5
    else:
        congrats = "You have finished the game"
        embed = discord.Embed(title=congrats, color=0xf1c40f)
        await ctx.send(embed=embed)
