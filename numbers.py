# triangle area 1/2 * base * height

base = 9
height = 3

area_of_triangle = (1/2)*base*height #13.5
print(area_of_triangle) # type: ignore

# round method to make decimal points in round digits like round(number to be round, how many decimal points)
rounded = round(area_of_triangle, 0) # 13.5 converted to 14
print(rounded)

# python do multiplication first
10+2*3 # 16

# if you want addition first then use ()
(10+2) * 3 # 36