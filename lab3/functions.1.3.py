def solve():
    numheads = 35
    numlegs= 94
    rabbits = int((numlegs - (2 * numheads)) / 2)
    chickens = int(numheads - rabbits)
    print(rabbits,chickens)
solve() 