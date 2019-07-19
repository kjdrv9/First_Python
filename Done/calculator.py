def toNum(self):
    try:
        self = int(self)
        return self
    except ValueError:
        self = float(self)
        return self


n1, a, n2 = input("계산할 식을 입력하시오\n").split()

n1 = toNum(n1)
n2 = toNum(n2)
if a == '+':
    op = n1 + n2
elif a == '-':
    op = n1 - n2
elif a == '*':
    op = n1 * n2
elif a == '/':
    op = n1 / n2
else:
    op = 'unknown'


print(n1, a, n2, '=', op)
