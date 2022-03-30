score = (int(input('score : ')))

if score>=90 :
    grade = 'A'
elif score>=80 :
    grade = 'B'
elif score>=70 :
    grade = 'C'
else :
    grade = 'F'

print (f'점수 : {score}, 평가 : {grade}')