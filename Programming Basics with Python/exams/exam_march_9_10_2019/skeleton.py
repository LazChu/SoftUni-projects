minutes = int(input())
seconds = int(input())
length_trace_in_meters = float(input())
seconds_for_100_meters = int(input())

control_in_seconds = minutes * 60 + seconds
delay_times = length_trace_in_meters / 120
total_delay = delay_times * 2.5
athlete_time = (length_trace_in_meters / 100) * seconds_for_100_meters - total_delay
if athlete_time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {athlete_time:.3f}.")
else:
    diff = abs(athlete_time - control_in_seconds)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")