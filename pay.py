hrs = input("enter hours: ")
rpg = input("enter rate per hour: ")
pay = float(hrs) * float(rpg)
print("PAY: ",pay)
def computepay():
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate_hour = input("Enter rate:")
    r = float(rate_hour)
    if h <= 40:
        print (h * r)
    else :
        print ((40 * r) + (h -40) * r * 1.5)
computepay()

try:
    inp = input("Enter a number between 0.0 and 1.0: ")
    score = float(inp)
    if (score >= 1.0):
        print("You didn't follow instructions")
        exit()
    elif (score >= 0.9):
        print("A")
    elif (score >= 0.8):
        print("B")
    elif (score >= 0.7):
        print("C")
    elif (score >= 0.6):
        print("D")
    else:
        print("F")
except:
    print("Please enter numerical numbers")
    exit()


##largest = None
##smallest = None
##while True:
##    try:
##        num = input("Enter a number: ")
##        if num == "done":
##            break
##        print (num)
##        num = int(num)
##        if largest is None or largest < num:
##            largest = num
##        elif smallest is None or smallest > num:
##             smallest = num
##    except ValueError:
##        print("Please, enter only numbers.")
##
##print ("Maximum", largest)
##print ("Minimum", smallest)
