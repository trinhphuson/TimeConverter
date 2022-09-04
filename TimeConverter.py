 # Seconds to minutes
def sectomin():
    sec = int(input("Type in your seconds: "))
    secpermin = 60
    mins = str(sec / secpermin)
    print(str(sec) + " seconds equals to " + mins + " minutes.") 
# Seconds to hours
def sectohrs():
    sec = int(input("Type in your seconds: "))
    secperhrs = 3600
    hrs = str(sec / secperhrs)
    print(str(sec) + " seconds equals to " + hrs + " hours.") 
# Seconds to days
def sectodays():
    sec = int(input("Type in your seconds: "))
    secperdays = 86400
    days = str(sec / secperdays)
    print(str(sec) + " seconds equals to " + days + " minutes.") 
# Minutes to seconds
def mintosec():
    min = int(input("Type in your minutes: "))
    secpermin = 60
    secs = str(min * secpermin)
    print(str(min) + " minutes equals to " + secs + " secondss.") 
# Minutes to hours
def mintohrs():
    min = int(input("Type in your minutes: "))
    minperhrs = 60
    hrs = str(min / minperhrs)
    print(str(min) + " minutes equals to " + hrs + " hours.") 
# Minutes to days
def mintodays():
    min = int(input("Type in your minutes: "))
    minperday = 1440
    days = str(min / minperday)
    print(str(min) + " minutes equals to " + days + " days.") 
# Hours to seconds
def hrstosec():
    hrs = int(input("Type in your hours: "))
    secsperhr = 3600
    sec = str(hrs * secsperhr)
    print(str(hrs) + " hours equals to " + sec + " seconds.")
# Hours to minutes
def hrstomins():
    hrs = int(input("Type in your hours: "))
    minsperhr = 60
    min = str(hrs * minsperhr)
    print(str(hrs) + " hours equals to " + min + " hours.")
# Hours to days
def hrstodays():
    hrs = int(input("Type in your hours: "))
    hrsperday = 24
    days = str(hrs / hrsperday)
    print(str(hrs) + " hours equals to " + days + " days.")
# Days to seconds
def daystosecs():
    days = int(input("Type in your days: "))
    secsperday = 86400
    sec = str(days * secsperday)
    print(str(days) + " days equals to " + sec + " seconds.")
# Days to minutes
def daystomins():
    days = int(input("Type in your days: "))
    minsperday = 1440
    min = str(days * minsperday)
    print(str(days) + " days equals to " + min + " minutes.")
# Days to hours
def daystohrs():
    days = int(input("Type in your days: "))
    hrsperday = 24
    hrs = str(days * hrsperday)
    print(str(days) + " days equals to " + hrs + " days.")
print("Welcome to the time converter!")
select = input('''
Please select a unit to convert from:
1. Seconds
2. Minutes
3. Hours
4. Days
''')
if select == "1":
    mode = input('''
Please select a unit to convert to:
1. Minutes
2. Hours
3. Days
''')
    if mode == "1":
        sectomin()
    elif mode == "2":
        sectohrs()
    elif mode == "3":
        sectodays()
if select == "2":
    mode = input('''
Please select a unit to convert to:
1. Seconds
2. Hours
3. Days
''')
    if mode == "1":
        mintosec()
    elif mode == "2":
        mintohrs()
    elif mode == "3":
        mintodays()
if select == "3":
    mode = input('''
Please select a unit to convert to:
1. Seconds
2. Minutes
3. Days
''')
    if mode == "1":
        hrstosec()
    elif mode == "2":
        hrstomins()
    elif mode == "3":
        hrstodays()
if select == "4":
    mode = input('''
Please select a unit to convert to:
1. Seconds
2. Minutes
3. Hours 
''')
    if mode == "1":
        daystosecs()
    elif mode == "2":
        daystomins()
    elif mode == "3":
        daystohrs()
input("Press Enter to exit.")
print("Have a nice day!")