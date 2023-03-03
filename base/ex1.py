hours = input('How many time did you work?: ')
rate_per_hour = input('How much is your rate per hour?: ')

try:
    fh = float(hours)
    fr = float(rate_per_hour)
except:
    print('Please enter numeric number')
    quit() # 프로그램 종료

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr

print('Your total earn is ', xp)