#
# (a) Write a script to compute and print the surface area of a sphere with radius 10. 
# The surface area is given by 4πr² where r is the radius and π is 3.14. 
# Your script should include in-code comments as necessary to allow a reviewer of the program 
# to understand the objective and functioning of it. Comments in Python begin with the # character.
#
import math
class SurfaceAreaCalc:

    def calculate_surface_area():
        # Prompt the user to enter the radius of the sphere
        radius = float(input("Enter the radius of the sphere (m): "))
    
        # Compute the surface area of the sphere using the formula 4πr²
        surface_area = 4 * math.pi * radius ** 2
    
        # Print the computed surface area
        print(f"The surface area of a sphere with radius {radius} is: {surface_area:.2f}m²")

    # Call the function to execute the calculation
    calculate_surface_area()