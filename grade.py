score = int(input("Score? "))

'''primeira versão com vários testes condicionais
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score <80:
    print("Grade: C")
elif score >=60 and score <70:
    print("Grade: D")
else:
    print("Grade: F")
'''
'''versão melhorada'''
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

    