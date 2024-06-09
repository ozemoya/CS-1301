#Myles Miller - This program is for calculating properties and finding out what triangle is whic
# Step 1: Accept side lengths
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Ensure c is the longest side
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Step 2: Calculate the perimeter
perimeter = a + b + c

# Step 3: Calculate the area using Heron's formula
s = perimeter / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Step 4: Determine the type of triangle
if a**2 + b**2 == c**2:
    triangle_type = "Right Triangle"
elif a**2 + b**2 > c**2:
    triangle_type = "Acute Triangle"
else:
    triangle_type = "Obtuse Triangle"

# Display the results
print(f"Perimeter of the triangle: {perimeter}")
print(f"Area of the triangle: {area}")
print(f"The triangle is an {triangle_type}")

