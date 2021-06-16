s = input()
l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
for d in '1234567890':
    s=s.replace(d, ' ')
s.strip(' ')
while s.find('  ') != -1:
    s = s.replace('  ', ' ')
print(integ)
print(s)
def s1(s):
 s3=""
 s2=0
 spl=str(s).split()
 for i in spl:
    for i in spl[s2].split():
        a=''.join(spl[s2])
        if len(a)==1:
                s3=s3+a[0].upper()+' '
        else:
                s3=s3+a[0].upper()+a[1:-1]+a[-1].upper()+' '
        s2=s2+1
 return s3
print(s1(s))

largest_number = max(integ)
print(largest_number)
integ1 = []
i = 0
for i in range(len(integ)):
    if integ[i] != largest_number:
        integ1.append(integ[i]**i)
print(integ1)

