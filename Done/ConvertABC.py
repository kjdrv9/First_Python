def atoi(alp):
    return ("abcdefghijklmnopqrstuvwxyz".find(alp.lower())) + 1


def atostar(alp):
    temp = atoi(alp)
    result = []
    for i in range(temp // 5):
        result.append("*****\n")
    result.append('*' * (temp % 5))
    return result


def atohex(alp):
    temp = atoi(alp)
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if temp >= 16:
        return '0x1%c' % hex[temp % 16]
    else:
        return '0x%c' % hex[temp % 16]


print('''

    ###     ####    ##  ##   ##  ##    #####   #####    ######               ##    #####      ###  
   ## ##   ##  ##   ##  ##   ##  ##    ##      ##  ##     ##                ###    ##  ##    ## ## 
  ##      ##   ##   ### ##   ##  ##    ##      ##  ##     ##               ## ##   ##  ##    ##     
  ##      ##   ##   ######   ##  ##    ####    ######     ##              ##  ##   ######    ##     
  ##      ##   ##   ## ###    ####     ##      ## ##      ##              #######  ##   ##   ##     
  ##  ##  ##  ##    ##  ##     ##      ##      ##  ##     ##              ##   ##  ##   ##   ##  ## 
   ####    ####     ##  ##     #       #####   ##  ##     ##              ##   ##  ######     ####  
                                                                                                   
''')

ch = input("1. alphabet to int\n2. alphabet to star\n3. alphabet to hex\n\nInput Menu Number : ")
alp = input("Input Your Alphabet : ")
if ch == '1':
    print(atoi(alp))
elif ch == '2':
    print(''.join(atostar(alp)))
elif ch == '3':
    print(atohex(alp))
else:
    print("ERROR")
