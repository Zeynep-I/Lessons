A = [18, 42, 600, 214, 86, 320, 99, 52, 901]
iki_belgili = []
uc_belgili = []
mukdar_1 = 0
mukdar_2 = 0
for i in A:
    if i < 100:
        iki_belgili.append(i)
        mukdar_1 += 1
    elif  99 < i < 1000: 
        uc_belgili.append(i)
        mukdar_2 += 1
print(f"{iki_belgili} \n Mukdar: {mukdar_1} \n")
print(f"{uc_belgili} \n Mukdar: {mukdar_2} \n")