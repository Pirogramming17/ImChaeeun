import random

num = 0


def brGame(player, num):
    if player == "computer":
        x = random.randint(1, 3)
    elif player == "player":
        while(1):
            try:
                x = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
                if x < 1 or x > 3:
                    print('1,2,3 중 하나를 입력하세요')
                    continue
                else:
                    break
            except:
                print("정수를 입력하세요")
    for i in range(x):
        num += 1
        print(player, num)
        if num == 31:
            return num
    return num


while(1):
    num = brGame("computer", num)
    if num == 31:
        print("player win!")
        break

    num = brGame("player", num)
    if num == 31:
        print("computer win!")
        break
