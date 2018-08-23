# -*-coding:utf-8-*-
w=input('weight:')
h=input('height')
weight=float(w)
height=float(h)
bmi=weight/(height*height)
if bmi<18.5:
    print('过轻%.2f'%bmi)
elif bmi<25:
    print('正常%.2f' %bmi)
elif bmi<28:
    print('偏胖%.2f' %bmi)
elif bmi<32:
    print('肥胖%.2f'%bmi)
else:
    print('严重肥胖%.2f'%bmi)