def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)

non_inv=[k for k in range(216) if gcd(k,216)!=1 ]
print(non_inv)

'''
Output:
[0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 44, 45, 46, 48, 50, 51, 52, 54, 56, 57, 58, 60, 62, 63, 64, 66, 68, 69, 70, 72, 74, 75, 76, 78, 80, 81, 82, 84, 86, 87, 88, 90, 92, 93, 94, 96, 98, 99, 100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 116, 117, 118, 120, 122, 123, 124, 126, 128, 129, 130, 132, 134, 135, 136, 138, 140, 141, 142, 144, 146, 147, 148, 150, 152, 153, 154, 156, 158, 159, 160, 162, 164, 165, 166, 168, 170, 171, 172, 174, 176, 177, 178, 180, 182, 183, 184, 186, 188, 189, 190, 192, 194, 195, 196, 198, 200, 201, 202, 204, 206, 207, 208, 210, 212, 213, 214]
'''