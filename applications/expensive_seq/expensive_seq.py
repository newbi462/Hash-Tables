speed = {}
def expensive_seq(x, y, z):
    # Implement me
    key = str(x) + str(y) + str(z)
    try:
        cashed_v = speed[key]
        #print(speed)
        return cashed_v
    except KeyError:
        if x <= 0:
            v = y + z
            speed[key] = v
            return v
        if x >  0:
            v = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
            speed[key] = v
            return v

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
