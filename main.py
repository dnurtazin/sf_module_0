import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,100)    # загадали число
def score_game(core):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
           
    count = 0
    max_val = 100
    min_val = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict:
            min_val = predict
            predict = int (min_val  + ((max_val - min_val)/2))
        elif number < predict:
            max_val = predict
            predict = int (max_val - ((max_val-min_val)/2))
    return(count) # выход из цикла, если угадали
# Проверяем
score_game(game_core_v3)
