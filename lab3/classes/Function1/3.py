def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return f"rabbits {rabbits}, chicken {chickens} "


print(solve(35, 94))  