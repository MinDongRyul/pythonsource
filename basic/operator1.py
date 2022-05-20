# 연산자
# 산술연산자 : +, -, *, /(실수), //(정수), %, **
a, b = 5, 3
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

print()
s1, s2, s3 = "100", "100.123", "99999999"
print(s1+s2+s3) # + : 연결 -> 100100.12399999999
print(float(s1) + float(s2) + float(s3))
print(int(s1) + 1) # TypeError: can only concatenate str (not "int") to str

# 복합대입 연산자 : +=, -=, *=, /=, //=, %=, **=
a = 10
a += 5
print("a",a)
a == 5
print("a",a)
a *= 5
print("a",a)
a /= 5
print("a",a)
a //= 5
print("a",a)
a %= 5
print("a",a)
a **= 5
print("a",a)

# 실습 : 777,777원
# 화폐교환 : 5만원 / 1만원 / 5천원 / 1천원
a1 = 777777
a2 = a1 // 50000 # 5만원권 갯수
a1 = a1 - (50000 * a2)
a3 = a1 // 10000 # 1만원권 갯수
a1 = a1 - (10000 * a3)
a4 = a1 // 5000 # 5천원권 갯수
a1 = a1 - (5000 * a4)
a5 = a1 // 1000 # 1천원권 갯수
a1 = a1 - (1000 * a5) # 잔액

print("5만원권 갯수 : ",a2)
print("1만원권 갯수 : ",a3)
print("5천원권 갯수 : ",a4)
print("1천원권 갯수 : ",a5)
print("잔돈 : ",a1)

# 관계 연산자 : ==, !=, >, <, >=, <=
a, b = 10, 0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 논리 연산자 : and, or, not
print(100 > 60 and 60 > 15)
# print(100 > 60 && 60 > 15) 사용 불가
print(100 > 60 or 60 < 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(!True) 사용 불가

# 비트연산자
print(10 & 7)
print(10 | 7)
print((100 > 60) & (60 > 15))
