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





r = float()
epsilon = 100
r_min = 0.0
r_max = 1
r_mid = (r_min + r_max)/2
amount_saved = float(initial_deposit*(1+r_mid/12)**months)

if initial_deposit >= (down_payment - 100):
    r = 0.0
else:
    if amount_saved < down_payment + float(100) and amount_saved > down_payment - 100:
        while amount_saved > down_payment - float(100):
            r_max = r_mid
            r_mid = (r_min + r_mid)/2
            amount_saved = float(initial_deposit*(1+r_mid/12)**months)
            if abs(amount_saved - down_payment) < 100:
                r = r_mid
                break
            else:
                if amount_saved < down_payment - float(100):
                    while amount_saved < down_payment - float(100):
                        r_min = r_mid
                        r_mid = (r_max + r_mid)/2
                        amount_saved = float(initial_deposit*(1+r_mid/12)**months)
                    if abs(amount_saved - down_payment) < 100:
                        r = r_mid
                        break
                else:
                    continue
            
    
    elif amount_saved < down_payment - float(100):
            while amount_saved < down_payment - float(100):
                r_min = r_mid
                r_mid = (r_max + r_mid)/2
                amount_saved = float(initial_deposit*(1+r_mid/12)**months)
                if abs(r_min - r_mid) < 100: # 这个还是有问题 ❌ 
                    r = None
                    break
                else:
                    if amount_saved > down_payment - float(100):
                        while amount_saved > down_payment - float(100):
                            r_min = r_mid
                            r_mid = (r_max + r_mid)/2
                            amount_saved = float(initial_deposit*(1+r_mid/12)**months)
                        if abs(amount_saved - down_payment) < 100:
                            r = r_mid
                            break
                    else:
                        continue
        

    # amount_saved > down_payment + 100

    else:
        while amount_saved > down_payment - float(100):
            r_max = r_mid
            r_mid = (r_min + r_mid)/2
            amount_saved = float(initial_deposit*(1+r_mid/12)**months)
            if abs(amount_saved - down_payment) < 100:
                r = r_mid
                break
            # amount_saved < down_payment - float(100):
            else:
                if amount_saved < (down_payment - float(100)):
                    while amount_saved < (down_payment - float(100)):
                        r_min = r_mid
                        r_mid = (r_max + r_mid)/2
                        amount_saved = float(initial_deposit*(1+r_mid/12)**months)
                    if abs(amount_saved - down_payment) < 100:
                        r = r_mid
                        break
                else:
                    continue

            
            


                    


print(r)
            


