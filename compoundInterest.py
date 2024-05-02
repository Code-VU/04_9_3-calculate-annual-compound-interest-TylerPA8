def calculateCompoundInterest():    
    # This first 3 lines are provided for yougetACompoundInterest()
    # This first 3 lines are provided for you    
    print("Compound Interest: "+ compoundInterestCaculator())
    print('---')
    print("Compound Interest: "+ compoundInterestCaculator())
    print('---')
    print("Compound Interest: " + compoundInterestCaculator())
    return

def compoundInterestCaculator():
    client_one_principal = float(input("Principle (amount):"))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
    amount = client_one_principal * ( 1 + client_one_rate/100)**client_one_time

    interest = amount - client_one_principal
    interest = round(interest,2)
    return (str(interest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()