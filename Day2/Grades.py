per = int(input("Enter Tour Percentage :"))
if per > 90 and per < 100 :
    print("Outstanding You got grade A")
elif per > 80 and per < 90 :
    print("Excellent You got grade B")
elif per > 70 and per < 80 :
    print("Nice You got grade C")
elif per > 60 and per < 70 :
    print("Good You got grade D")
else :
    print("You Got Average Grade E")
