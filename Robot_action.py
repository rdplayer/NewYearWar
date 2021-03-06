
机器人行动策略：
三公：
    经典场（无需策略）：
        庄家：无操作
        闲家：随机下注（下注1:50%,下注2:30%,下注3:20%）
    抢庄场：
        抢庄：根据2张手牌决定抢庄倍数（暂时随机：不抢30%，2倍25%，3倍20%，4倍15%，5倍10%，后期模型训练）
        抢庄结束：
            庄家：无操作
            闲家：根据2张手牌决定压住倍数（暂时随机：5倍30%，10倍25%，15倍20%，20倍15%，25倍10%，后期模型训练）

新年大战百人场：
    根据身上积分选择下注金额（最大可下注金额=身上积分/4）
    下注（4个位置都可以下注,目前随机下注）



控牌策略：
1.不同底注房间都有一个机器人净分池，根据池的净分判断是否触发控牌概率，根据概率进行触发。（该功能针对吸分与吐分触发值与随机性触发）
触发吐分：单个机器人控牌触发概率=房间总池净分范围/正3000万（对应不同底注房间）
触发吸分：单个机器人控牌触发概率=房间总池净分范围/负3000万（对应不同底注房间）
可配置内容：房间总池净分范围，单个机器人控牌触发概率

2.根据本房间玩家队列进行控牌（该功能针对用户的随机控牌与强制控牌）
当触发控牌时，寻找队列中的玩家进行吐分与吸分（周日23:59:59清除本周所有用户净分值得，重新计算）
触发吐分：玩家控牌触发概率=队列用户本周净分范围/正2000万（对应不同底注房间）
触发吸分：玩家控牌触发概率=队列用户本周净分范围/负2000万（对应不同底注房间）
可配置内容：用户净分范围，玩家控牌触发概率

3.玩家强补功能
3-1.连续对局输控牌方式：针对必须本周净分为负的用户控牌，在2的基础上累加概率
触发吸分：玩家控牌触发概率增加=（连输次数-2）/10
可配置内容：连数次数，玩家控牌概率增加值可配置
3-2.连续对局多天输分控牌方式：每天至少输50万积分以上，在2的基础上累加概率
触发吸分：玩家控牌触发概率增加=（连输天数-1）/10
可配置内容：连数天数，玩家控牌概率增加值可配置
3-3.充值后游戏内触发吸分概率增加（当日）
触发吸分概率增加（当日）=100/当日充值金额，最高30%

4.控牌流程
4.1.每次开局后，先随机发牌，确定抢庄与押注结束后开始计算输赢换牌。（如经典场无抢庄概念，抢庄场需要等发完2张牌后抢庄结束发第三张牌）
4.1.1抢庄为发完2张牌后抢庄与押注，之后发第3张牌，控牌需要在押注结束后计算输赢控制发第3张牌
4.1.2.经典玩法为押注完毕后发3张牌，因此在押注完毕后计算输赢控制发3张牌
4.2.判断步骤一、先计算本局机器人是否触发控牌，如果机器人触发控牌，则判断是吐分还是吸分
4.2.1.吸分状态则进行换牌
4.2.1.1.如牌桌有1个机器人触发吸分控牌时，把本局最大的一把牌换给到机器人（庄家机器人优先）
4.2.1.2.如牌桌有2个（含2个）以上机器人时，把本局最大的一把牌优先换给庄家机器人，其他机器人不换牌
4.2.1.3.如牌桌有2个（含2个）以上机器人时，无坐庄机器人时，按照本桌机器人数量换给对应依次最大的牌
4.2.2.吐分状态则不换牌
4.3.判断步骤二、再计算玩家是否触发控牌，如果玩家触发控牌，则判断吐分还是吸分
4.3.1.吸分状态则进行换牌
4.2.1.1.如牌桌有1个玩家触发吸分控牌时，把本局最大的一把牌换给此玩家（无论是否坐庄）
4.2.1.2.如牌桌有2个（含2个）以上玩家触发吸分控牌时，把本局最大的一把牌换给本周净负分最高的玩家，其他吸分玩家牌不换（无论是否坐庄）
4.2.2.吐分状态则进行换牌
4.2.1.1.如牌桌有1个玩家人触发吐分控牌时，把本局最小的一把牌换给此玩家（无论是否坐庄）
4.2.1.2.如牌桌有2个（含2个）以上人触发吐分控牌时，把本局最小的一把牌换给本周净正分最高的玩家，其他吐分玩家牌不换（无论是否坐庄）
4.4.判断步骤三、再计算充值触发赢分概率换牌
4.4.1.如牌桌有1个玩家触发赢分概率换牌，把本局最大的一把牌还给此玩家（无论是否坐庄）
4.4.2.如牌桌有2个（含2个）以上人触发赢分概率换牌时，把本局最大的一把牌换给本周净负分最高的玩家，其他触发赢分概率玩家牌不换（无论是否坐庄）
4.4.服务端完成以上换牌后，前端进行游戏正常发牌。
4.4.1.无论三公、决战、拼十、拼罗松、十三水，都在确定庄家是机器人或玩家后，再进行最后的换牌。
