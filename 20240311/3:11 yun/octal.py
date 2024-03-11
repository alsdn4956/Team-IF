# 2진수 -> 8진수 변환
num_bin = '110101' #65
print(f"Binary number = {num_bin}")

BIT = 3
num_bin = num_bin[::-1]
num_oct = []

bit = 0
while bit < len(num_bin):
    exp, sum_ = 0, 0
    while exp < BIT:
        if bit >= len(num_bin):
            break
        sum_ += (2**exp) *int(num_bin[bit])
        exp += 1
        bit += 1
    
    num_oct.append(sum_)

str_oct = "".join(map(str, num_oct[::-1]))
print(f"Octal number = {str_oct}")