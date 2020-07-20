#!/usr/bin/env python
# coding: utf-8

# In[28]:


'''Сначала устанавливаем любое random число, а потом вводим две переменных left=1 
    и right=100. Угадываемое число predict устанавливаем не как случайное число, 
    а как середину диапазона между left и right. После чего проверяем: 
    если number>predict, то сдвигаем левую границу, т.е. left=predict+1,
    если number<predict, то сдвигаем правую границу, т.е. right=predict-1, 
    если number = predict, то число угадано, выйти.'''
import numpy as np
def game_core_v4(number):
    left = 1
    right = 100
    count = 1
    predict = 50
     # предполагаемое число 
    while predict != number:
        count+=1
        predict = (left+right)//2
        if predict > number:
            right = predict - 1
        elif predict < number:
            left = predict + 1   
    return(count) # выход из цикла, если угадали

       
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# Проверяем
score_game(game_core_v4)       


# In[ ]:





# In[ ]:




