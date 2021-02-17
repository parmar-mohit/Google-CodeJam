def work(string,i):
    blocks = string.split(str(i))
    string = ""
    for data in blocks:
        if data != "":
            string += "({})".format(work(data,i+1))
        string += str(i)

    return string[0:-1]

t = int(input())

for n in range(0,t):
    s = input()
    print("Case #{}: {}".format(n+1,work(s,0)))