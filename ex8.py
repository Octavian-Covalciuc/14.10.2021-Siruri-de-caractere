sir1 = 'ABRA CA DABRA'
sir2 = 'ZAZA'
sir3 = 'A B C D E'
sir01 = [chr(ord(x) + 1) if 65 <= ord(x) < 90 else ' ' for x in sir1]
sir02 = ['A' if x == 'Z' else x for x in sir2]
sir03 = ['-' if x == ' ' else x for x in sir3]
print(''.join(sir01))
print(''.join(sir02))
print(''.join(sir03))
