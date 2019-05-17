#Solution to 538's Riddler Challenge of 5/17/19
#https://fivethirtyeight.com/features/how-many-soldiers-do-you-need-to-beat-the-night-king/
from random import randint
import pandas
x = 0
statslist = []
numtrials = 500

for z in range(500):
    alivenum = 100+x
    deadnum = 100
    resultlist = []

    for j in range(numtrials):
        dead = []
        alive = []

        for i in range(deadnum):
            dead_soldier = 1
            dead.append(dead_soldier)

        for i in range(alivenum):
            alive_solider = 1
            alive.append(alive_solider)

        i = 0
        while (len(dead) > 1 or len(alive) > 1):
            if (len(alive) == 0 or len(dead) == 0):
                break
            chance = randint(1,2)
            if chance == 1:
                dead.pop()
            else:
                alive.pop()
                dead.append(1)
            i += 1
            
        if len(alive) > len(dead):
            winner = 'Alive'
        else:
            winner = 'Dead'

        results = {'Trial': j+1, 'Alive': len(alive), 'Dead': len(dead), 'Winner': winner}
        resultlist.append(results)

    df = pandas.DataFrame(resultlist)
    statistics = {'NumAlive' : alivenum, 'NumDead' : deadnum, 'AvgAlive' : df['Alive'].mean(), 'AvgDead' : df['Dead'].mean(), 'WinAlive%' : df.Winner.str.count('Alive').sum() / numtrials, 'WinDead%' : df.Winner.str.count('Dead').sum() / numtrials}
    statslist.append(statistics)
    print(statistics)
    if df.Winner.str.count('Alive').sum() / 1000 < 0.5:
        x += 25
    else:
        x -= 25

df_stats = pandas.DataFrame(statslist)
print(df_stats)
df_stats.to_excel("test_zombie.xlsx")