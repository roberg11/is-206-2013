##def valid_day(day):
##    int_day = int(day)
##    if int_day >= 1 and int_day <= 31:
##        return int_day

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day
        

print valid_day('0') #=> None    
print valid_day('1') #=> 1
print valid_day('15') #=> 15
print valid_day('500') #=> None
print valid_day('foo') #=> None
