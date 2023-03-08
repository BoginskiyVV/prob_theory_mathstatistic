# Урок 3. EDA (exploratory data analysis) или Разведочный анализ

import numpy as np
from math import factorial

'''1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 
30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без использования статистических 
методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную 
и несмещенную оценки дисперсий для данной выборки.'''
print('----------------------------------------------------------------------------------------------------')
salary = np.array ([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

def arithmetic_mean(salary):
    return sum(salary)/len(salary)

AM = arithmetic_mean(salary)
print(f'Среднее арифметическое = {round(AM, 4)}')

def mean_square_deviation(salary):
    square_deviation = (salary - AM)**2
    return (sum(square_deviation)/len(square_deviation))**(1/2)

MSD = mean_square_deviation(salary)
print(f'Среднее квадратичное отклонение = {round(MSD, 4)}')

def biased_estimate_variance(salary):
    square_deviation = (salary - AM)**2
    return sum(square_deviation)/len(square_deviation)

BEV = biased_estimate_variance(salary)
print(f'Смещённая оценка дисперсии = {round(BEV, 4)}')

def unbiased_estimate_variance(salary):
    square_deviation = (salary - AM)**2
    return sum(square_deviation)/(len(square_deviation)-1)

UEV = unbiased_estimate_variance(salary)
print(f'Несмещённая оценка дисперсии = {round(UEV, 4)}')

# print(np.mean(salary))
# print(np.std(salary))
# print(np.var(salary))
# print(np.var(salary, ddof=1))
print('----------------------------------------------------------------------------------------------------')


'''2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, 
из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
Какова вероятность того, что 3 мяча белые?'''

'''1. 1->0 белых мячей, 2->3 белых мяча
   2. 1->1 белый мяч, 2->2 белых мяча
   3. 1->2 белых мяча, 2->1 белый мяч (далее БМ)'''

def comb(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

P1 = (comb(3, 2)/comb(8, 2)*(comb(5, 3)*comb(7, 1)/comb(12, 4)))
print(f'Вероятность, что из 1-ой корзины вытащили 0 БМ, а из 2-ой корзины вытащили 3 БМ P1 = {round(P1, 4)}')

P2 = (comb(5, 1)*comb(3, 1)*comb(5, 2)*comb(7, 2))/(comb(8, 2)*comb(12, 4))
print(f'Вероятность, что из 1-ой корзины вытащили 1 БМ, а из 2-ой корзины вытащили 2 БМ P2 = {round(P2, 4)}')

P3 = (comb(5, 2)*comb(5, 1)*comb(7, 3))/(comb(8, 2)*comb(12, 4))
print(f'Вероятность, что из 1-ой корзины вытащили 2 БМ, а из 2-ой корзины вытащили 1 БМ P3 = {round(P3, 4)}')

PA = P1 + P2 + P3
print(f'Веротность того, что вытащат 3 белых мяча P(A) = {round(PA, 4)}')
print(f'или P(A) = {round(PA * 100, 2)} %')
print('----------------------------------------------------------------------------------------------------')


'''3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. Вероятность 
попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность 
того, что выстрел произведен: a) первым спортсменом б) вторым спортсменом в) третьим спортсменом.'''

'''
А -> цель поражена
B1 -> выстрелил 1-ый 
B2 -> выстрелил 2-ой
B3 -> выстрелил 3-ий
P(B1)=P(B2)=P(B3) ==> PB = 1/3
'''
PB = 1/3
PA = PB*0.9 + PB*0.8 + PB*0.6
print(f'Полная вероятность наступленения события РА = {round(PA, 4)}')

PAB1 = round(PB * 0.9 / PA, 4)
PAB2 = round(PB * 0.8 / PA, 4)
PAB3 = round(PB * 0.6 / PA, 4)
print(f'Вероятность, что выстрелил 1-ый спортсмен PAB1 = {round(PAB1 * 100, 4)} %')
print(f'Вероятность, что выстрелил 2-ой спортсмен PAB2 = {round(PAB2 * 100, 4)} %')
print(f'Вероятность, что выстрелил 3-ий спортсмен PAB3 = {round(PAB3 * 100, 4)} %')
print('----------------------------------------------------------------------------------------------------')


'''4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов 
поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую 
сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B 
в). на факультете C?'''

'''
Факультет А - n студентов
Факультет В - n студентов
Факультет С - 2*n студентов
Группа событий = 1
0,25 + 0,25 + 0,5 = 1
'''
PA1 = 0.25*0.8 + 0.25*0.7 + 0.5*0.9
print(f'Полная вероятность наступления события РА1 = {round(PA1, 4)}')
PA1A = 0.25*0.8 / PA1
PA1B = 0.25*0.7 / PA1
PA1C = 0.5*0.9 / PA1
print(f'Вероятность, что студент учится на факультете А - {round(PA1A * 100, 2)} %')
print(f'Вероятность, что студент учится на факультете B - {round(PA1B * 100, 2)} %')
print(f'Вероятность, что студент учится на факультете C - {round(PA1C * 100, 2)} %')
print('----------------------------------------------------------------------------------------------------')


'''5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц.
равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут 
из строя: а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?'''

C1 = 0.1                                                        # сломана 1-я деталь
C2 = 1-0.1                                                      # не сломана 1-я деталь  
C3 = 0.2                                                        # сломана 2-я деталь 
C4 = 1-0.2                                                      # не сломана 2-ая деталь 
C5 = 0.25                                                       # сломана 3-я деталь
C6 = 1-0.25                                                     # не сломана 3-я деталь 
С7 = C1*C3*C5                                                   # сломаны все детали
C8 = C1*C3*C6 + C1*C4*C5 + C2*C3*C5                             # сломаны 2 детали
C9 = 1 - (C2*C4*C6)                                             # сломана хотя бы одна деталь 
C10 = C1*C4*C6 + C3*C2*C6 + C5*C2*C4                            # сломана 1 деталь
C11 = C8 + C10

print(f'Вероятность, что из стоя выйдут все детали - {round(С7*100, 2)} %')
print(f'Вероятность, что из стоя выйдут 2 детали - {round(C8*100, 2)} %')
print(f'Вероятность, что из стоя выйдет хотя бы одна деталь - {round(C9*100, 2)} %')
print(f'Вероятность, что из стоя выйдет от 1-ой до 2-х деталей - {round(C11*100, 2)} %')