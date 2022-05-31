from math import *
import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlim([-10,10])
# ax.set_ylim([0,20])
# ax.set_title('Основы matplotlib')
# x = [-3, -2, -1, 0, 1, 2, 3]
# y = [9, 4, 1, 0, 1, 4, 9]
# ax.plot(x,y, color = 'black', linewidth = 3)
# ax.scatter([0,1,2,3,4], [1,3,8,12,27], color = 'blue', marker= '*')
# plt.show()
# with open('orwell_1984.txt', encoding='utf8') as text:
#     words_lengths = [len(word) for word in text.read().split()]
# longest_word_length = max(words_lengths)
#
# plt.hist(words_lengths, bins=longest_word_length)
# plt.title("Распределение")
# plt.ylabel("кол-во слов данной длины")
# plt.xlabel("длина слова")
# plt.show()
def temperature(x: float) -> float:
    return atan(-0.0012*x**3+0.4*x**2+0.616*x+6120)+0.65*sin(0.24*x+1.23)-0.27*cos(0.21*x-0.17)-sin(0.34*x+0.16)/(1+0.03*(x-370.5)**2)
x = list(range(1,1000))
y =[temperature(t) for t in x]
findX = 0
xChange = 0
for i in range(len(y)):
    if y[i] < 0 and findX == 0:
        xChange = x[i]
        findX = 1
plt.plot(x,y, color = 'black')
plt.scatter(xChange, 0, color = 'blue', marker= '*')
plt.show()