questions = ["1) What is the capital of Canada ?",
"2) What is the only flag that does not have four sides ?",
"3) How many bones do we have in an ear ?",
"4) Which is the only body part that is fully grown from birth? ",
"5) Name a shape that has ten sides? ",
"6) What is the capital of Turkey? ",
"7) How many hearts does an octopus have? ",
"8) In which year did humans first land on the Moon?",
"9) Which element has the chemical symbol 'O'?",
"10) Which of these is the smallest ocean in the world?"
]

answers = ["A)Toronto  B)Vancouver  C) Ottawa  D)Montreal",
"A)Nepal  B)Switzerland  C)Japan  D)Vatican city",
"A)1  B)2  C)3  D)4",
"A)Brain  B)Eyes  C)Heart  D)Liver",
"A)Octagon  B)Hexagon  C)Pentagon  D)Decagon",
"A)Bursa  B)Izmir  C)Istanbul  D)Ankara",
"A)1  B)2  C)3  D)4",
"A)1965  B)1969  C)1972  D)1980",
"A)Oxygen  B)Ozone  C)Oganesson  D)Osmium",
"A)Atlantic Ocean  B)Indian Ocean  C)Arctic Ocean  D)Pacific Ocean",
]

correct_ans = ["C","A","C","B","D","D","C","B","A","C"]

l = 0
for i in range(len(questions)):
    print(questions[i])
    print(answers[i])
    k = input("Your choice (A, B, C, D): ")
    if k == correct_ans[i]:
        l += 10
        print(f"Correct! +10 \nYour point: {l}\n")
    else:
        l -= 5
        print(f"Incorrect! -5 \nYour point: {l}\n")
print(f"Your final point: {l}")