import random

omikuji = random.randint(1,10)

if int(omikuji) == 1:
    print("おみくじは" + str(omikuji) + "なので大吉です")
elif int(omikuji) == 2:
    print("おみくじは" + str(omikuji) + "なので中吉です")
elif int(omikuji) <= 5:
    print("おみくじは" + str(omikuji) + "なので小吉です")
elif int(omikuji) <= 7:
    print("おみくじは" + str(omikuji) + "なので凶です")
else:
    print("おみくじは" + str(omikuji) + "なので大凶です")
