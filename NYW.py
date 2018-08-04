#终极版新年大战
import numpy as np
import random
import matplotlib.pyplot as plt
import copy
#模拟压注
def choice(player):
    for i in range(len(player)):
        player[i] = random.randint(1,4)
#模拟压注金额
def money(player):
    for i in range(len(player)):
        player[i] = 1000 * random.randint(1,10)
#模拟倍数
def base(player):
    for i in range(len(player)):
        player[i] = random.randint(1,4)
#模拟VIP等级
def vip(player):
    for i in range(len(player)):
        player[i] = i%10
#痛苦指数
def pain_index(n,player,now_win,now_loss):

    for k in range(len(player)):
        if player[k] == n:
            now_win[k] += 1
            now_loss[k] = 0
        else:
            now_loss[k] += 1
            now_win[k] = 0
    return now_win.sum()

player=np.zeros(100,'int32')
vip=vip(player)

total_win=np.zeros(100,'int32')
now_win=np.zeros(100,'int32')
total_loss=np.zeros(100,'int32')
now_loss=np.zeros(100,'int32')
pain=np.zeros(4,'int32')
for i in range(1000):
    choice(player)
    for j in range(1,5):
        win = copy.deepcopy(now_win)
        loss = copy.deepcopy(now_loss)
        pain[j-1] = pain_index(j,player,win,loss)

    #n = random.randint(1,4)
    n = np.argmin(pain) + 1

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
    # print(now_win.sum())
    # print(-now_loss.sum())




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

#plt.savefig('img2win.jpg')
plt.show()