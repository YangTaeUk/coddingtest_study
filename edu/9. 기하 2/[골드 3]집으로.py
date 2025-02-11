

x,y,d,t = map(float, input().split())

def time_check(x,y,d,t):
    dist = (x**2+y**2)**0.5
    only_walk = dist
    only_jump = 0
    jump_then_walk = 0
    if dist >= d:
        only_jump = (dist // d) * t + min(t, (dist % d))
    else:
        only_jump = min(t + (d - dist), 2 * t)

    jumps = int(dist // d)
    jump_then_walk = jumps * t + (dist - jumps * d)

    return min(only_walk, only_jump, jump_then_walk)

print("{:.9f}".format(time_check(x,y,d,t)))
#print(round(, 9))