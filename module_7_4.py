# Напишем функции для вычисляемых данных

def tasks_total_def():
    return score_1 + score_2

def time_avg_def():
    return (team1_time + team2_time) / (score_1 + score_2)

def challenge_result_def():
    if (team1_time / score_1) < (team2_time / score_2):
        res = f'Победа команды {team2}'
    elif (team1_time / score_1) > (team2_time / score_2):
        res = f'Победа команды {team1}'
    else:
        res = 'Ничья'
    return res


team1 = 'Мастера кода'
team2 = 'Волшебники данных'

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

# Дефолтные данные

# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

# Вычисляемые данные

tasks_total = tasks_total_def()
time_avg = round(time_avg_def(), 1)
challenge_result = challenge_result_def()


# Использование %

print('В команде %s участников: %d!' % (team1,team1_num))
print('Итого сегодня в командах участников: %s и %d!' % (team1_num, team2_num))

# Использование format()

print('Команда {} решила задач: {}!'.format(team2, score_2))
print('{} решили задачи за {} с!'.format(team2, team2_time))

# Использование f-строк

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')