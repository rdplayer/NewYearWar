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
one_win=np.zeros(shape=[100,50],dtype=np.int)
one_loss=np.zeros(shape=[100,50],dtype=np.int)
for i in range(1000):
    n = random.randint(1,4)
    choice(player)
    for k in range(len(player)):
        if player[k] == n :
            now_win[k] += 1
            one_loss[k][now_loss[k]] += 1
            now_loss[k] = 0
            if now_win[k] > total_win[k] :
                total_win[k] = now_win[k]
        else:
            now_loss[k] += 1
            one_win[k][now_win[k]] += 1
            now_win[k] = 0
            if now_loss[k] > total_loss[k] :
                total_loss[k] = now_loss[k]

playerID = 2
print(one_win[playerID])
print(one_loss[playerID])

win= sorted(total_win)
loss= sorted(total_loss)
x= np.arange(1,11,0.2)
y=one_win[playerID]
z=one_loss[playerID]


plt.figure(figsize=(8,8))
plt.subplot(211)
plt.plot(x,y, linestyle='-', marker='o',label="win",color="red",linewidth=1)
plt.ylabel('num of player')
plt.xlabel('num of win')
plt.title("NewYearWar")
plt.xlim(0,10)
plt.legend()
plt.subplot(212)
plt.plot(x,z, linestyle='-', marker='o',label="loss",color="blue",linewidth=1)
plt.ylabel('num of player')
plt.xlabel('num of loss')
#plt.title("NewYearWar")
plt.xlim(0,10)
plt.legend()

#plt.savefig('img1.jpg')
plt.show()