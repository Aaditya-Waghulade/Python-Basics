def calculate_total(exp):
    total=0
    for item in exp:
        total = total+item
    return total

aadi = [6500,30000,25000,40000]

vrushabh  = [12000,30000,50000,2]

aadi_total = calculate_total(aadi)
vrushabh_total = calculate_total(vrushabh)

print("Aadi total is:",aadi_total)
print("Vrushabh total is: ",vrushabh_total)