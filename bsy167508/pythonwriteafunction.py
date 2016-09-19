#writeafunction.py
#!/bin/python

def is_leap(year):
    leap = False
    if year%4==0:
        if year%100==0:
            if year%400!=0:
                leap = False
            else:
                leap = True
        else:
            leap = True
    print leap
            
year=int(raw_input().strip())
is_leap(year)
