# game.py
'''
 掷骰子

 1. 欢迎进入xxxx游戏
 2. 输入用户名，默认用户是没有币
 3. 提示用户充值买币（100块钱30币，充值必须是100的倍数，充值不成功可以再次充值）
 4. 玩一局游戏扣除2个币，猜大小（系统用随机数模拟骰子产生值）
 5. 只要猜对了奖励1个币，可以继续玩（想不想继续玩，也可以没有金币自动退出）

'''
import random

def func2():

	print('*'*30)
	print('欢迎进入澳门赌场')
	print('*'*30)

	username = input('请输入顾客大名:')
	money = 0
	answer = input('确定进入游戏吗(y/n)?')

	if answer=='y':
		# 判断游戏币是否充足
		# 做到反复充值
		while money<2:
			n = int(input('金币不足，请充值(100块钱30币，充值必须是100的倍数):'))
			# 充值金额判断
			if n%100==0 and n>0:
				money=(n//100)*30

		print('当前剩余游戏币是:{},玩一局游戏扣除2个币'.format(money))

		print('进入游戏...........')

		while True:  # False

			# 模拟骰子 产生骰子的值
			t1 = random.randint(1,6)
			t2 = random.randint(1,6)
			# 两个骰子的值大于6 --->大, 否则就是小

			money-=2 # 扣除金币

			print('系统洗牌完毕，请猜大小:')
			guess = input('输入大或者输入小:')

			# 判断: 大小

			if ( (t1+t2)>6 and guess=='大' ) or ((t1+t2)<=6 and guess=='小'):
				print('恭喜{}! 本局游戏获奖励1个游戏币！'.format(username))
				money +=1
			else:
				print('很遗憾！骰子是:{}和{}，本局游戏输啦┭┮﹏┭┮'.format(t1,t2))


			answer = input('剩余游戏币{}，是否继续再来一局游戏，要扣除2枚游戏币？(y/n)'.format(money))

			if answer!='y' or money < 2:
				print('退出游戏啦！！！！！')
				break


def func1():
	# 随机产生QQ号码 5~10位，0不能开头
	qq = []
	for i in range(0, 10):
		ran = random.randint(0, 9)
		if i == 0 and ran == 0:
			continue
		qq.append(str(ran))
	#qq = [str(i) for i in qq]
	#print(qq)
	str1 = ''
	str1 = str1.join(qq)

	return str1
print(func1())