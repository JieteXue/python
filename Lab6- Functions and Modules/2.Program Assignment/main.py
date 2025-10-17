import geometry
shape=input("Choose a shape (rectangle or circle):")
if shape=="rectangle":
    length=float(input("Enter the length:"))
    width=float(input("Enter the width:"))
    print("The area is",geometry.rectangle_area(length,width))
else:
    radius=float(input("Enter the radius:"))
    print("The area is",geometry.circle_area(radius))