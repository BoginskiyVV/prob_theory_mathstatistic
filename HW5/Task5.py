# Семинар 5 "Тестирование гипотез"
# Задачи 2,3 решать вручную

import numpy as np
import math
import scipy.stats as stats 

'''
Задача 1. Когда используется критерий Стьюдента, а когда Z –критерий?
'''
print('Критерий Стьюдента используется, если: \n'
      '- неизвестна сигма генеральной совокупности \n'
      '- соблюдаются условия применимости параметрических тестов\n'
      '- равенство дисперсий\n'
      'Z критерий используется: \n'
      '- нормально распределенная генеральная совокупность\n'
      '- известна сигма генеральной совокупности')
print('=========================================================================')

'''
Задача 2. Проведите тест гипотезы. Утверждается, что шарики для подшипников, 
изготовленные автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, если 
в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм, 
а дисперсия известна и равна 4 кв. мм.
'''

n = 100
var = 4
alpha = 0.05
M0 = 17
Mn = 17.5

# Известна дисперсия -> критерий Z
# H0 = M0, H1 > Mn

def hypotest(n, var, alpha, M0, Mn):
    Zt = stats.norm.ppf(1-alpha)
#     print(round(Zt, 4))
    sigma = math.sqrt(var)
    Zn = (Mn-M0)/sigma*math.sqrt(n)
#     print(round(Zn, 4))
    if Zn < Zt:
        print('Верна гипотеза Н0')
    else:
        print('Верна гипотеза Н1')  

hypotest(n, var, alpha, M0, Mn)
print('=========================================================================')


'''
Задача 3. Проведите тест гипотезы. Продавец утверждает, что средний вес 
пачки печенья составляет 200 г. Из партии извлечена выборка из 10 пачек. 
Вес каждой пачки составляет: 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально. Верно ли утверждение продавца, 
если учитывать, что доверительная вероятность равна 99%? (Провести двусторонний тест)
'''
#  Дисперсия не известна -> критерий t
# H0 = 200, H1 != 200

alpha1 = 1-0.99
selection = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
H0 = 200

mean_selection = np.mean(selection)
# print(np.mean(selection))
D = sum((selection - mean_selection)**2) / (len(selection) - 1)
# print(D)
sigma = np.sqrt(D)
# print(sigma)
t = (mean_selection - H0) / sigma * np.sqrt(len(selection))
print(abs(t))
# t = 1.0651 < t табличное ~ 2.821 => H0
print('Утверждение продавца верно')
print('=========================================================================')



'''Задачу 4 решать с помощью функции. Есть ли статистически значимые различия 
между средним ростом дочерей и матерей?
Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163
'''
# H0 = mothers, H1 != mothers

mothers =([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
adult_daughters = ([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])

print(stats.ttest_rel(mothers, adult_daughters))
print('pvalue > alfa и значение меньше табличного => верна H0 гипотеза, статистически значимых различий нет')
print('=========================================================================')

