机器人调度策略以及行动策略

def 机器人建桌规则(房间内有空位桌数量,当前时间):
    2:00-6:00:
        if 房间内有空位桌数量 < 1:
            建桌,数量=1-房间内有空位桌数量
    6: 00 - 9:00:
        if 房间内有空位桌数量 < 2:
            建桌,数量=2-房间内有空位桌数量
    10: 00 - 19:00:
        if 房间内有空位桌数量 < 3:
            建桌,数量=3-房间内有空位桌数量
    19: 00 - 23:00:
        if 房间内有空位桌数量 < 4:
            建桌,数量=4-房间内有空位桌数量
    23:00-2:00:
        if 房间内有空位桌数量 < 5:
            建桌,数量=5-房间内有空位桌数量
    
def 机器人入桌规则(当前桌总人数,当前桌机器人数):
    1人：进2人
    2人：进1人
    3人以上：不进

def 机器人离桌规则(当前桌游戏局数):
    离桌概率：当前桌游戏局数/100

def 机器人换桌规则(连输局数):
    换桌概率：连输居数/20

def 机器人休息规则(当日对局数):
    休息概率：当日对局数/1000
    休息时间：当日对局数/1000 小时

def 机器人下分规则(机器人身上积分,入桌标准):
    机器人被调用入桌或建桌时，进入下分判断
    判断身上积分是否高于入桌标准 * 5以上，如高于入桌标准 * 5以上，增加对应公式积分
    第一步，清除所有身上积分
    第二步，增加对应公式积分（此积分增加不增加VIP经验）
    对应公式积分：本房间入房标注积分 * 系数
    系数（1.5 - 4.0）随机
    机器人下分完成后，机器人进入等待中状态，并插入等待中队列第一位。

def 机器人补分规则(机器人身上积分,入桌标准):
    机器人被调用入桌或建桌时，进入补分判断
    判断身上积分是否低于入桌标准，如低于入桌标准，增加对应公式积分
    对应公式积分：本房间入房标注积分 * 系数
    系数（1.5 - 5.0）随机
    机器人补分完成后，机器人进入等待中状态，并插入等待中队列第一位。
    机器人初始积分：入房标准 * 1.5

def 机器人报废规则(总对局数):
    总对局数>100万,永久报废
    总对局数<100万,休息时间加成：总局数/100万

def 机器人总数控制规则(在线玩家人数):
    根据在线玩家人数按比例投放机器人

def vip计算公式(补充积分):
    vip经验=补充积分/10000/参数

