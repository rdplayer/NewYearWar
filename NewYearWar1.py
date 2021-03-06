import numpy as np
import random
import matplotlib.pyplot as plt

#模拟压注
def choice(player):
    for i in range(len(player)):
        player[i] = random.randint(1,4)


player=np.zeros(100,'int32')
total_win=np.zeros(100,'int32')
now_win=np.zeros(100,'int32')
total_loss=np.zeros(100,'int32')
now_loss=np.zeros(100,'int32')

for i in range(1000):
    n = random.randint(1,4)
    choice(player)
    for k in range(len(player)):
        if player[k] == n :
            now_win[k] += 1
            now_loss[k] = 0
            if now_win[k] > total_win[k] :
                total_win[k] = now_win[k]
        else:
            now_loss[k] += 1
            now_win[k] = 0
            if now_loss[k] > total_loss[k] :
                total_loss[k] = now_loss[k]

print(total_win)
print(total_loss)
x= np.arange(0,100,1)
y= sorted(total_win)
z= sorted(total_loss)

plt.figure(figsize=(8,8))
plt.subplot(211)
plt.plot(x,y, linestyle='-', marker='o',label="win",color="red",linewidth=1)
plt.ylabel('num of player')
plt.xlabel('num of win')
plt.title("NewYearWar")
plt.legend()
plt.subplot(212)
plt.plot(x,z, linestyle='-', marker='o',label="loss",color="blue",linewidth=1)
plt.ylabel('num of player')
plt.xlabel('num of loss')
#plt.title("NewYearWar")
plt.legend()

plt.savefig('img.jpg')
plt.show()