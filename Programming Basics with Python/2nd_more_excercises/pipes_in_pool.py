volume_pool = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours_away = float(input())

pipe_1_debit = first_pipe * hours_away
pipe_2_debit = second_pipe * hours_away
water = pipe_1_debit + pipe_2_debit

if volume_pool >= water:
    pool_percentage = water * 100 / volume_pool
    pipe_1 = pipe_1_debit * 100 / water
    pipe_2 = pipe_2_debit * 100 / water
    print(f"The pool is {pool_percentage}% full. Pipe 1: {pipe_1:.2f}%. Pipe 2: {pipe_2:.2f}%.")

elif water > volume_pool:
    overflow = water - volume_pool
    print(f"For {hours_away} hours the pool overflows with {overflow:.2f} liters.")