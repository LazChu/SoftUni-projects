packet_pens = int(input())
packet_markers = int(input())
litres_detergent= int(input())
discount_percentage= int(input())
pens_price=5.8
markers_price=7.2
detergent_price=1.2
total_price=packet_pens*pens_price+packet_markers*markers_price+\
    litres_detergent*detergent_price
discount= total_price*discount_percentage/100
total_sum = total_price-discount
print(total_sum)
