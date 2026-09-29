#reviewer for midterms

age = int(input("AGE ---> "))
rev = float(input("REVENUE ---> "))
cc = int(input("CREDIT SCORE ---> "))
yrs = float(input("YEARS OF BUSINESS ---> "))
has_defaults = bool(input("FILE FOR BANKRUPTCY ---> "))
collateral = input("COLLATERAL NAME ---> ")
c_value = float(input("COLLATERAL VALUE ---> "))


max_loan = 0
base_fee = 0

if age >= 21 and has_defaults == False and yrs >= 2.0:
    print("BASELINE PASSED")
    if cc >= 720: #TIER 1
        print("CREDIT SCORE CONSIDERED HIGH")
        max_loan = rev * 3
        if rev >= 50000:
            print("ABOVE 50K REVENUE ")
            base_fee = max_loan * 0.15
            print("BASE FEE IS SET TO ",base_fee)
        else:
            print("REVENUE BELOW 50K")
            base_fee= max_loan* 0.025
            print("BASE FEE IS SET TO ",base_fee)

        #COLLATERAL
        if c_value >= max_loan:
            print("COLLATERAL ",collateral," with a value of ",c_value, " is ACCEPTED")
        else:
            print("REJECTED: INSUFFICIENT COLLATERAL VALUE FOR ",collateral)

        #SURCHARGE
        if c_value % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE, TOTAL BASE FEE IS ",base_fee)
        else:
            print("COLLATERAL VALUE DIVISIBLE BY 5000")

    elif cc <= 620 and cc < 720: #TIER 2
        print("Credit score within range of 620 to 720")
        max_loan = rev * 1.5
        if yrs >= 5.0:
            base_fee = max_loan * 0.02
            print("Years in business greater than 5 years base fee is ",base_fee)
        else:
            base_fee = max_loan * 0.035
            print("Years in business lower than 5 years base fee is ",base_fee)

        #COLLATERAL
        if c_value >= max_loan:
            print("COLLATERAL ",collateral," with a value of ",c_value, " is ACCEPTED")
        else:
            print("REJECTED: INSUFFICIENT COLLATERAL VALUE FOR ",collateral)
        
        #SURCHARGE
        if c_value % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE, TOTAL BASE FEE IS ",base_fee)
        else:
            print("COLLATERAL VALUE DIVISIBLE BY 5000")

    elif cc < 620: #TIER 3
        print("Credit score too low")
    else:
        print("INVALID")

else:
    print("BASELINE FAILED")