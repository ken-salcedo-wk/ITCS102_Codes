# age
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has collateral (boolean)

#INPUTS
age = int(input("enter your age -->  "))
is_employed = bool(input("are you currently employed (true/false) -->  "))
credit_score = float(input("credit score -->  "))
annual_income = float(input("what is your annual salary -->  "))
has_collateral = bool(input("do you have any collateral (true/false) -->  "))

base_rate = 0.0

#OUTPUTS
print("------------------------")
print("age --> ", age)
print("currently employed --> ", is_employed)
print("credit score --> ", credit_score)
print("annual salary --> ", annual_income)
print("do you have collateral? --> ", has_collateral)
print("------------------------")

if has_collateral == True:
    print("you have collateral")
else:
    print("you have no collateral")

if age >= 21 and is_employed == True:
    print("accepted baseline criteria")
    if credit_score >= 750: #tier1
        print("you have a high credit score")
        if annual_income >= 100000:
            print("you have a high salary")
            base_rate = 4.5
            print("your base rate is --> ", base_rate)
        else:
            base_rate = 5.0
            print("your base rate is --> ", base_rate)
    elif credit_score >= 600 and credit_score < 750: #tier2
        print("your credit score is less than 750")
        if has_collateral == True:
            print("you have a collateral")
            base_rate = 7.0
            print("your base rate is --> ", base_rate)
        elif annual_income <= 40000:
            print("low annual income")
            base_rate = 9.5
            print("your base rate is --> ", base_rate)
        else:
            base_rate = 8.0
            print("your base rate is --> ", base_rate)
    elif credit_score <= 600: #tier3
        print("Rejected: Credit score too low")
    else:
        print("invalid details")
else:
    print("Rejected: fails baseline criteria")
