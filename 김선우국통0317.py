# -*- coding: utf-8 -*-
"""김선우국통0317.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IZdWBHgELo7sb0wi2GbSMvcUR15ZKwU3

P.92 이차원 리스트~
"""

kor_score=[13,55,87,44,77]
math_score=[23,11,100,99,33]
eng_score=[34,67,88,66,100]

midterm_score=[kor_score,math_score,eng_score]

print(id(math_score[0]))
print(id(midterm_score[1][0]))

math_score[0]=1000 
# 값을 재할당하면 id로 확인할 위치의 값이 달라짐    
# 파이썬은 리스트를 저장할때 값 자체가 아니라 값이 위치한 메모리 주소를 저장함                                            
print(id(math_score[0]))

a=300
b=300
print(a is b)
print(a == b)
# ==은 값을 비교하는 연산이고, is는 메모리의 주소를 비교하는 연산
# -5부터 256까지는 특정 메모리 주소에 저장하여 is 쓰더라도 같더라고 나옴

a=["color",1,0.2]
b=["color",11,2.2]
color = ['yellow','blue','green','black','purple']

print(a+b)
print(a*2)

a[0]=color #문자열 대신 리스트를 넣은것
print(a)

a =[5,4,3,2,1]
b = [1,2,3,4,5]

b=a
print(b)
print(id(a))
print(id(b))

a.sort()
print(b)

# b=a를 입력하는 순간 두 변수가 같은 메모리 주소를 저장한다.
#  같은 리스트 값을 가르키고 있으므로 하나의 값이 바뀌더라도 둘 다 바뀜

print(a is b)

b.sort(reverse=True)
print(a)

# c=[]
# c=a.sort() sort는 정렬만 해주지, 그 자체로 값을 할당하지는 않음.
# print(c)  

# 98쪽 참고

fruit1=['grape','sourGrape','melon']
fruit2=['orange','banana']


print(fruit1+fruit2)

if True:
    print('참인 경우 실행되는 문장')
else:
    print('거짓인 경우 실행되는 문장')

if 0:
    print('참인 경우 실행되는 문장')
else:
    print('거짓인 경우 실행되는 문장')

print((3>5)<10)

# 3>5가 0으로 치환됨

score=int(input('score:'))

if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade='F'
print(grade)

year=int(input('태어난 년도?:'))
age = 2023-year+1

if age<=26 and age>=20:
    print('대학생')

elif age>=17:
    print('고등학생')

elif age>=14:
    print('중학생')

elif age>=8:
    print('초등학생')

else:
    print('학생이 아닙니다.')

for i in [1,2,3]:
    print(i)

for i in range(1,13,2): #시작,미만,step
    print(i,'pyhon')

text=['bts','봉준호','손흥민','김선우']
for i in text:
    print(i,'let\'s go')

for i in 'python':
    print(i,'let\'s go')

i=1
while i<10:
    print(i)
    i+=1

    #초기값, 조건문, 무한루프 점검하기.

number=int(input('구구단 몇단을 계산할까요:'))

print('구구단 %d단을 계산한다.'%number)
for i in range(9):
    print(number*(i+1))

sentence='i love you'
reverse=''
for char in sentence:
    reverse=char+reverse

print(reverse)