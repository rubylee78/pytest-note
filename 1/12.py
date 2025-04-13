import time

Ts=int(time.time())
Cs=Ts%60

Tm=Ts//60
Cm=Tm%60

Th=Tm//60
Ch=(Th+8)%24

print("現在的時間是",Ch,":",Cm,":",Cs)
