country = input()
discipline = input()

if country == 'Russia':
    if discipline == 'ribbon':
        score = 9.100 + 9.400
    elif discipline == 'hoop':
        score = 9.300 + 9.800
    elif discipline == 'rope':
        score = 9.600 + 9.000
elif country == 'Bulgaria':
    if discipline == 'ribbon':
        score = 9.600 + 9.400
    elif discipline == 'hoop':
        score = 9.550 + 9.750
    elif discipline == 'rope':
        score = 9.500 + 9.400
elif country == 'Italy':
    if discipline == 'ribbon':
        score = 9.200+ 9.500
    elif discipline == 'hoop':
        score = 9.450 + 9.350
    elif discipline == 'rope':
        score = 9.700 + 9.150

score_needed = 20 - score
percent = (score_needed / 20) * 100
print(f"The team of {country} get {score:.3f} on {discipline}.")
print(f"{percent:.2f}%")
