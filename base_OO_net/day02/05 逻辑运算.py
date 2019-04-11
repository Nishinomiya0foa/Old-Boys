# and or not
# 优先级 ()>not>and>or

# x or y: x非零, return x
print(1 or 3)
print(0 or 4)

# x and y: x非零, return y
print(1 and 2)
print(0 and 2)

#
print(0 or 4 and 3 or 2) # 3
print( 1 > 2 and 3 or 4 and 3 < 2)

# 非零->True; 0->False


# F or F or F
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# F or F or F
print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# F or F or F
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)

# T or F = T
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)

#
print(1 < 2 and 3 < 4 or 1>2)

# F or F
print(3>4 or 4<3 and 1==1)

# 0 or 3 or 7 or 6
print(0 or 4 and 3 or 7 or 9 and 6)