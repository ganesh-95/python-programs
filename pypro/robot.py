import math
pos  = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "up":
        pos[0] += steps

    elif direction  == "down":
        pos[0] -= steps
    elif direction == "left":
        pos[1] -= steps
    elif direction == "right":
        pos[1] += steps

    else:
        pass

print int(round(math.sqrt(pos[1]**2 + pos[0]**2)))



