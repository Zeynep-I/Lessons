def gosmak():
    netije = san1 + san2
    print(f"Netije: {netije}")
def ayyrmak():
    netije = san1 - san2
    print(f"Netije: {netije}")
def kopeltmek():
    netije = san1 * san2
    print(f"Netije: {netije}")

def bolmek():
    netije = san1 / san2
    print(f"Netije: {netije}")
while True:
    san1 = int(input("1 - nji sany girizin: "))
    san2 = int(input("2 - nji sany girizin: "))
    funksiya = input("Funksiyany saylan: +, -, *,/\nFunksiya:")
    if funksiya == "+":
        gosmak()
    elif funksiya == "-":
        ayyrmak()
    elif funksiya == "*":
        kopeltmek()
    elif funksiya == "/":
        bolmek()
    else:
        print("Nadogry funksiya")