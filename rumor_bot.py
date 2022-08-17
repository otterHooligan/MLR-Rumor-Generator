import random
import db_interface as db
import fake_rumor_assets as assets


def generate_rumor():
    rumor = random.choice(open('rumors.txt').read().splitlines())
    if rumor.count('[TEAM]') > 0:
        teams = random.sample(assets.team_names.items(), rumor.count('[TEAM]'))
        for i in range(rumor.count('[TEAM]')):
            rumor = rumor.replace('[TEAM]', teams[i][1], 1)
            gm, cogm = db.fetch_one('''SELECT gm, cogm FROM teamData WHERE abb=%s''', (teams[i][0],))
            if '[GM]' in rumor:
                rumor = rumor.replace('[GM]', gm, 1)
            if '[CO-GM]' in rumor:
                if cogm:
                    rumor = rumor.replace('[CO-GM]', cogm, 1)
                else:
                    return None
            if '[PLAYERNAME]' in rumor:
                players = db.fetch_data('SELECT playerName, priPos FROM playerData WHERE team=%s', (teams[i][0],))
                player = random.choice(players)
                rumor = rumor.replace('[PLAYERNAME]', player[0], 1)
                rumor = rumor.replace('[POS1]', player[1], 1)
    if rumor.count('[PLAYERNAME]') > 0:
        all_players = db.fetch_data('''SELECT playerName FROM playerData WHERE status=1''', None)
        players = random.sample(all_players, rumor.count('[PLAYERNAME]'))
        for i in range(rumor.count('[PLAYERNAME]')):
            rumor = rumor.replace('[PLAYERNAME]', players[i][0], 1)
    if '[FREEAGENT]' in rumor:
        free_agents = db.fetch_data('''SELECT playerName FROM playerData WHERE (team IS NULL or team='' or team=' ') AND status=1''', None)
        rumor = rumor.replace('[FREEAGENT]', random.choice(free_agents)[0])
    if '[COMPLAINT]' in rumor:
        rumor = rumor.replace('[COMPLAINT]', random.choice(assets.complaints))
    if '[INJURY]' in rumor:
        rumor = rumor.replace('[INJURY]', random.choice(assets.injuries))
    if '[LOCATION]' in rumor:
        rumor = rumor.replace('[LOCATION]', random.choice(assets.locations))
    if '[COMPANY]' in rumor:
        rumor = rumor.replace('[COMPANY]', random.choice(assets.company))
    if '[TRADE]' in rumor:
        rumor = rumor.replace('[TRADE]', random.choice(assets.trades))
    if '[PAYMENT]' in rumor:
        rumor = rumor.replace('[PAYMENT]', random.choice(assets.payments))
    if '[LEAGUE]' in rumor:
        rumor = rumor.replace('[LEAGUE]', random.choice(assets.leagues))
    if random.randint(0, 10) < 5:
        rumor = f'{rumor}, {random.choice(assets.reactions)}'
    else:
        rumor += '.'
    return rumor


print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())
print(generate_rumor())