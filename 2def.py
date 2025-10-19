def main(l):
    
    result = cubeVolume(l)
    return result

def cubeVolume(sideLength):
    return sideLength * sideLength * sideLength

length=float(input("Enter the side length: "))
print(main(length))
