while True:
    m, a, b = map(int,input(). split())
    if m==0 and a==0 and b==0:
        break
    t = round((m/a - m/b)*3600)
    hour = t//3600
    t -= hour*3600
    min = t//60
    sec = t%60
    print(hour, end=':')
    if min<10:
        print('0%d' % min, end=':')
    else:
        print(min, end=':')
    if sec<10:
        print('0%d' % sec)
    else:
        print(sec)

