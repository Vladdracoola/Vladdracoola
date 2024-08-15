import random
team1_num = random.randint(5,6)#Вдруг заболел?
team2_num = random.randint(6,7)#Любимая команда учителя, но на всё воля случая :D
score1 = team1_num * random.randint(4,8)#Ребята вроде шарят, но Толя точно гений! Может кританёт? xD
score2 = team2_num * random.randint(5,6)#Стабильные любимчики. Ботаны.
team1_time = int((score1 / random.randint(15,30)) * 1000)#Толя сможет!
team2_time = int((score2 / random.randint(20,35)) * 1000)#Толя! Толя! Толя! - скандировали ученики школы
tasks_total = score1 + score2
time_avg =int((team1_time + team2_time) / tasks_total)
#Если вдруг вы заметите несостыковки по времени, то Бог рандома, он такой... :D
#Вдобавок учитывается только эффективное время(которое привело к успешному решению задачи)

def challenge_results():
    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        challenge_result = 'Победа команды Волшебники данных!'
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        challenge_result = 'Победа команды Мастера кода!'
    else:
        challenge_result = 'Ничья!'
    return challenge_result


print('"В команде Волшебники данных участников: ' '%(name)s!"' % {'name': team1_num})
print('"В команде Мастера кода участников: ' '%(name)s!"' % {'name': team2_num})
print('"Итого сегодня в командах участников: ' '%(name)s' ' и ' '%(name2)s!"' % {'name': team1_num, 'name2': team2_num})

print('"Команда Волшебники данных решила задач: {}!"'.format(score1))
print('"Команда Мастера кода решила задач: {}!"'.format(score2))
print('"Волшебники данных решили задачи за {} с!"'.format(team1_time))
print('"Мастера кода решили задачи за {} c!"'.format(team2_time))

print(f'"Команды решили {score1} и {score2} задач."')
print(f'"Результат битвы: {challenge_results()}')
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунд на задачу!"')