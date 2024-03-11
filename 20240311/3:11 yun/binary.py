# 10진수 -> 2진수 변환 (횟수에 상관없이))
BASE = 2
num = 11
print(f"Decimal number = {num}")

if num == 0:
    print(f"Binary number = 0")
else:
    num_bin = []
    while num:
        num, r = num // BASE, num % BASE
        num_bin.append(r)
    
    str_bin = "".join(map(str, num_bin[::-1]))
    print(f"Binary number = {str_bin}")

# 2진수 -> 10진수 변환 
num_bin = "1011"
print(f"Binary number = {num_bin}")

num_dec = 0
num_bin = num_bin[::-1]
exp = 0
while exp < len(num_bin):
    num_dec += (2**exp) * int(num_bin[exp])
    exp += 1

print(f"Decimal number = {num_dec}")

# 2진수 -> 10진수 변환 upgrade _ 자료구조의 이해 : pop operate
num_bin = "1011"
print(f"Binary number = {num_bin}")
num_bin = list(num_bin)

num_dec, bit = 0, 0
while num_bin:
    num_dec += (2**bit) * int(num_bin.pop())
    bit += 1
    
print(f"Decimal number = {num_dec}")