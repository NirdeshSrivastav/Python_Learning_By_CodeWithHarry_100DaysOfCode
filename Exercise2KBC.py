print("Hello and welcome to Kon Banega crorepati.")

qlist = ["Which is the Capital of India\n1- Lucknow\n2- New Delhi\n3- Bangaluru\n4- Mai Nahi Btaunga..",
         "Which is a programming language\n1- Hindi\n2- Spanish\n3- Python\n4- Mai Nahi Btaunga..",
         "Who is the Prime Minister of india\n1- Rahul Gandhi\n2- Yogi Aadityanath\n3- Narendra Modi\n4- Mai Nahi Btaunga.."]
answers = ["New Delhi", "Python", "Narendra Modi"]

money = 0
for i in qlist:
    print(i)
    ans = input("Enter your option number - ")
    if ans in answers:
        print("Right Answer..")
        money = money + 100000
    else:
        print("Wronge Answer")

print("You have earned = Rs.", money)
