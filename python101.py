# Define counter to track triples

counter = 0

for c in range(1, 48):
    for b in range(1, c):
        for a in range(1, b):
            if a * a + b * b == c * c:
                print('{:3d},{:3d},{:3d}'.format(a, b, c))
                counter = counter + 1

print("\nTotal count of  Pythagorean triples:  " + str(counter))
