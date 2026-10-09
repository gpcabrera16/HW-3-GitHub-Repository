d0=1
d1=2
d2=3
d3=4
d4=5
d5=6
d6=7
d7=8

d1+=2
d3+=2
d5+=2
d7+=2

def process_added_digit(digit):
    if digit > 9:
        return digit - 9
    else:
        return digit
    
d1=process_added_digit(d1)
d3=process_added_digit(d3)
d5=process_added_digit(d5)
d7=process_added_digit(d7)

s=d0+d1+d2+d3+d4+d5+d6+d7
checkdigit=s%4

print(checkdigit)