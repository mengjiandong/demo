import random
secret = random.randint(1, 100)
print('猜数字游戏 ！')
tries = 1
while tries <= 6:
    guess = int(input("1-100的整数,第%d次猜，请输入: " % (tries)))
    if guess == secret:
        print("恭喜答对了, 你只猜了%d次 , 就是这个%d " % (tries, secret))
        break
    elif guess > secret:
        print("不好意思，大了点")
    else:
        print("不好意思，小了点")
    tries += 1
else:
    print("哎呀，怎么也没猜中,再见")