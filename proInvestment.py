import math  # for using log function
def calculateEarning(initialMoney, interestRate):
    rate = interestRate/100  #converting 6% to 0.06
    # calculating amount after 1 year, 10 years, 20 years, 30 years 
    totalMoney1 = initialMoney * pow(1+rate , 1)
    totalMoney10 = initialMoney * pow(1+rate, 10)
    totalMoney20 = initialMoney * pow(1+rate , 20)
    totalMoney30 = initialMoney * pow(1+rate , 30)
    # printing the amount with 2 digits after decimal
    print(" \n After 1 year    :  ", round(totalMoney1,2))
    print(" After 10 year   :  ", round(totalMoney10,2))
    print(" After 20 year   :  ", round(totalMoney20,2))
    print(" After 30 year   :  ", round(totalMoney30,2))
    
    print("\n*******************************************************")
    # calculating years to which money will be doubled
    doubleMoney= initialMoney * 2
    years = math.log((doubleMoney / initialMoney)) / math.log(1+rate)
    print(" \n It wil take about : ", round(years,2), "years for your investment to double up")

print("        WELCOME TO PRO INVESTMENT \n")
# taking input of initial money and interest rate
initialMoney= int(input(" How much money do you want to invest ? : RM "))
interestRate= int(input(" \n What is the yearly interest rate (%) ? :  "))
print("\n=======================================================")
print("                INVESTMENT")
print("=======================================================")

# function calling with 2 parameters
calculateEarning(initialMoney, interestRate)