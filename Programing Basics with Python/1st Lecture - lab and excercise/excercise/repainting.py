nylon_needed = int(input())
paint_needed = int(input())
paint_thinner = int(input())
work_hours = int(input())
nylon_price=1.50
paint_price=14.50
thinner_price=5.00
bags=0.40
nylon=(nylon_needed+2)*nylon_price
paint=(paint_needed+(paint_needed*0.10))*paint_price
thinner=paint_thinner*thinner_price
materials = nylon+paint+thinner+bags
hourly_paycheck = materials*0.30
paycheck = hourly_paycheck*work_hours
total_sum=paycheck+materials
print(total_sum)