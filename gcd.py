def gcd_sub(a, b):
  while a!= 0 and b!=0:
    if a >b: a = a-b     # a가 b보다 큰 경우 a = a-b
    else: b = b-a
  return a + b

# ex) gcd(a, a-1)은 최악의 경우 a번 반복


def gcd_mod(a,b):        # 2log2a
  while a!=0 and b!=0:
    if a > b: a = a%b
    else: b = b%a
  return a+b

# 나머지 gcd알고리즘에서는 두 수가 서로소일 때 루프 횟수가 최대가 됨


def gcd_rec(a,b):
  if a==b or b==0: return a+b
  elif a>b: return gcd(a%b, b)
  else: return gcd(b%a, a)      # gcd_rec(b%a, a) == gcd_rec(a, b%a)
