ht=float(input("Enter the height(cm):"))
wt=float(input("Enter the Weight(kg):"))
h=ht/100
bmi=wt/(h**2)
if(bmi<=16):
        print(bmi,"\nSevere Thinness")
elif(16<bmi<=17):
        print(bmi,"\nMild Thinness")
elif(17<bmi<=18.5):
        print(bmi,"\nModerate Thinness")
elif(18.5<bmi<=25):
        print(bmi,"\nNormal")
elif(25<bmi<=30):
        print(bmi,"\nOverWeight")
elif(30<bmi<=35):
        print(bmi,"\nObese Class I")
elif(35<bmi<=40):
        print(bmi,"\nObese Class II")
elif(bmi>40):
        print(bmi,"\nObese Class III")
