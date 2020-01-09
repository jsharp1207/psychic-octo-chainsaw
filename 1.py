onetwothree = int(input("enter a string of three numbers ranging from 001 - 999:\n"))
if 1 <= onetwothree <= 999:
    (one) = (onetwothree/100)%10
    (two) = (onetwothree/10)%10
    (three) = (onetwothree)%10
    print(str(int(three)) + str(int(two)) + str(int(one)))
else:
    print("pls follow instructions next time, closing")
    exit()
