←
←
# given a fixed initial deposit, 
# find the lowest rate of return r 
# that allows you to save enough for a down payment in exactly 3 years, 
# using bisection search.

# House cost: $800,000
# Down payment: 25% → target = $200,000
# Time horizon: 36 months
# Acceptable range: within $100 of the target (exclusive)
# initial_deposit — cast as float

# amount_saved = initial_deposit × (1 + r/12) ^ months

# If initial_deposit >= down_payment - $100 → r = 0.0
# If no valid r exists within 0%–100% → r = None (not the string "None")


initial_deposit = input("Your initial_deposit($): ")
down_payment = float(200000)
months = int(36)

while True:
    try:
        float(initial_deposit)
        break
    except ValueError:
        initial_deposit = input("Your initial_deposit($): ")
    
initial_deposit = abs(float(initial_deposit))





r = float(1)
r_min = 0.0
r_max = 1.0
r_mid = (r_min + r_max) / 2
amount_saved = float(initial_deposit*(1+r_mid/12)**months)
amount_saved_pre = float()
amount_saved_1 = float(initial_deposit*( 1+ 1/12)**months)


def r_value(r_mid, r, amount_saved_pre):
    if amount_saved > down_payment + 100:
        if amount_saved_pre < amount_saved:
            r = float(2*r_mid - r)
            return r
        else:
            return r
    else:
        if amount_saved_pre > amount_saved:
            r = float(2*r_mid - r)
            return r
        else:
            return r



 # down_payment - 100 < amount_saved < down_payment + 100
if initial_deposit >= down_payment - 100:
    r = 0.0

elif amount_saved_1 < down_payment - 100:
    r = None
else:
    while amount_saved < down_payment - 100 or amount_saved > down_payment + 100:
        r = r_value(r_mid, r, amount_saved_pre)
        r_mid = (r + r_mid) / 2
        amount_saved = float(initial_deposit*(1+r_mid/12)**months)
        amount_saved_pre = float(initial_deposit*(1+(2*r_mid-r)/12)**months)
        if amount_saved < down_payment + 100 and amount_saved > down_payment - 100:
            r = r_mid
            break
print(r)

                


