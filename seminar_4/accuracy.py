# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = int(input('Введите точность d: '))
pi = 3
sum =0
for i in range(2,10000000,4):

    pid =4/(i*(i+1)*(i+2)) - 4/((i+2)*(i+3)*(i+4))    
    sum += pid 
res_str = str(pi+sum)
res_round=res_str[:2+d]
print(res_round)
