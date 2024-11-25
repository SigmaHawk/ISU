import random
import math

# Area calculations
def circle_area():
    try:
        r = float(input("What's the radius? "))
        if r <= 0:
            print("Hey, radius needs to be positive!")
            return
        area = math.pi * r * r
        print(f"The circle's area is {area:.2f}")
    except:
        print("Oops! Please enter a valid number")

def rectangle_area():
    try:
        w = float(input("Width? "))
        h = float(input("Height? "))
        if w <= 0 or h <= 0:
            print("Width and height must be positive!")
            return
        area = w * h
        print(f"The rectangle's area is {area}")
    except:
        print("Something went wrong - make sure to enter valid numbers!")

def triangle_area():
    try:
        b = float(input("Base? "))
        h = float(input("Height? "))
        if b <= 0 or h <= 0:
            print("Numbers must be positive!")
            return
        area = (b * h) / 2
        print(f"Triangle area = {area}")
    except:
        print("Please enter valid numbers!")

# Volume calculations
def sphere_volume():
    try:
        r = float(input("Radius of sphere? "))
        if r <= 0:
            print("Radius must be positive!")
            return
        r_cubed = r * r * r
        volume = (4/3) * math.pi * r_cubed
        print(f"Sphere volume = {volume:.2f}")
    except:
        print("Please enter a valid number!")

def cube_volume():
    try:
        side = float(input("Length of cube side? "))
        if side <= 0:
            print("Side length must be positive!")
            return
        vol = side * side * side
        print(f"Cube volume = {vol}")
    except:
        print("Enter a valid number please!")

def rectangular_prism_volume():
    try:
        l = float(input("Length? "))
        w = float(input("Width? "))
        h = float(input("Height? "))
        if l <= 0 or w <= 0 or h <= 0:
            print("All measurements must be positive!")
            return
        volume = l * w * h
        print(f"Rectangular prism volume = {volume}")
    except:
        print("Please enter valid numbers!")

def triangular_prism_volume():
    try:
        b = float(input("Base of triangle? "))
        h = float(input("Height of triangle? "))
        l = float(input("Length of prism? "))
        if b <= 0 or h <= 0 or l <= 0:
            print("All measurements must be positive!")
            return
        triangle_area = (b * h) / 2
        volume = triangle_area * l
        print(f"Triangular prism volume = {volume}")
    except:
        print("Please enter valid numbers!")

def cylinder_volume():
    try:
        r = float(input("Radius of cylinder? "))
        h = float(input("Height of cylinder? "))
        if r <= 0 or h <= 0:
            print("Measurements must be positive!")
            return
        circle_area = math.pi * r * r
        volume = circle_area * h
        print(f"Cylinder volume = {volume:.2f}")
    except:
        print("Please enter valid numbers!")

# Surface Area calculations
def sphere_surface():
    try:
        r = float(input("Radius of sphere? "))
        if r <= 0:
            print("Radius must be positive!")
            return
        surface = 4 * math.pi * r * r
        print(f"Sphere surface area = {surface:.2f}")
    except:
        print("Please enter a valid number!")

def cube_surface():
    try:
        side = float(input("Length of cube side? "))
        if side <= 0:
            print("Side must be positive!")
            return
        face_area = side * side
        surface = 6 * face_area
        print(f"Cube surface area = {surface}")
    except:
        print("Enter a valid number!")

def rectangular_prism_surface():
    try:
        l = float(input("Length? "))
        w = float(input("Width? "))
        h = float(input("Height? "))
        if l <= 0 or w <= 0 or h <= 0:
            print("All measurements must be positive!")
            return
        surface = 2 * (l*w + l*h + w*h)
        print(f"Rectangular prism surface area = {surface}")
    except:
        print("Please enter valid numbers!")

def triangular_prism_surface():
    try:
        b = float(input("Base of triangle? "))
        h = float(input("Height of triangle? "))
        l = float(input("Length of prism? "))
        if b <= 0 or h <= 0 or l <= 0:
            print("All measurements must be positive!")
            return
        triangle_area = (b * h) / 2
        rectangle_area = l * (b + h + (b**2 + h**2)**0.5)  # length * perimeter of triangle
        surface = 2 * triangle_area + rectangle_area
        print(f"Triangular prism surface area = {surface:.2f}")
    except:
        print("Please enter valid numbers!")

def cylinder_surface():
    try:
        r = float(input("Radius of cylinder? "))
        h = float(input("Height of cylinder? "))
        if r <= 0 or h <= 0:
            print("Measurements must be positive!")
            return
        circle_area = math.pi * r * r
        side_area = 2 * math.pi * r * h
        total = 2 * circle_area + side_area
        print(f"Cylinder surface area = {total:.2f}")
    except:
        print("Please enter valid numbers!")

def area_calculator():
    while True:
        print("\n=== Area Calculator ===")
        print("1) Circle")
        print("2) Rectangle")
        print("3) Triangle")
        print("4) Back to main menu")
        
        choice = input("\nChoose a shape (1-4): ")
        
        if choice == "1":
            circle_area()
        elif choice == "2":
            rectangle_area()
        elif choice == "3":
            triangle_area()
        elif choice == "4":
            break
        else:
            print("Please pick a valid option!")

def volume_calculator():
    while True:
        print("\n=== Volume Calculator ===")
        print("1) Sphere")
        print("2) Cube")
        print("3) Rectangular Prism")
        print("4) Triangular Prism")
        print("5) Cylinder")
        print("6) Back to main menu")
        
        choice = input("\nChoose a shape (1-6): ")
        
        if choice == "1":
            sphere_volume()
        elif choice == "2":
            cube_volume()
        elif choice == "3":
            rectangular_prism_volume()
        elif choice == "4":
            triangular_prism_volume()
        elif choice == "5":
            cylinder_volume()
        elif choice == "6":
            break
        else:
            print("Please pick a valid option!")

def surface_area_calculator():
    while True:
        print("\n=== Surface Area Calculator ===")
        print("1) Sphere")
        print("2) Cube")
        print("3) Rectangular Prism")
        print("4) Triangular Prism")
        print("5) Cylinder")
        print("6) Back to main menu")
        
        choice = input("\nChoose a shape (1-6): ")
        
        if choice == "1":
            sphere_surface()
        elif choice == "2":
            cube_surface()
        elif choice == "3":
            rectangular_prism_surface()
        elif choice == "4":
            triangular_prism_surface()
        elif choice == "5":
            cylinder_surface()
        elif choice == "6":
            break
        else:
            print("Please pick a valid option!")

def take_quiz():
    print("\n--- Quick Geometry Quiz! ---")
    score = 0
    
    questions = [
        {
            "question": "What's the volume of a rectangular prism with length 3, width 2, and height 4?",
            "answer": 24
        },
        {
            "question": "What's the surface area of a cube with side length 2?",
            "answer": 24
        },
        {
            "question": "What's the area of a triangle with base 6 and height 4?",
            "answer": 12
        }
    ]
    
    for q in questions:
        print("\n" + q["question"])
        try:
            user_answer = float(input("Your answer: "))
            if abs(user_answer - q["answer"]) < 0.1:
                print("Correct! 🎉")
                score += 1
            else:
                print(f"Not quite - the answer was {q['answer']}")
        except:
            print("Please enter a number!")
            continue
    
    print(f"\nYou got {score} out of {len(questions)} correct!")
    if score == len(questions):
        print("Perfect! You're a geometry master!")
    elif score >= len(questions)/2:
        print("Pretty good! Keep practicing!")
    else:
        print("These are tricky - keep trying!")

def main():
    while True:
        print("\nGeometry Calculator")
        print("1) Calculate Area(2D)")
        print("2) Calculate Volume(3D)")
        print("3) Calculate Surface Area(3D)")
        print("4) Take a Quiz")
        print("5) Quit")
        
        choice = input("\nWhat would you like to do? (1-5): ")
        
        if choice == "1":
            area_calculator()
        elif choice == "2":
            volume_calculator()
        elif choice == "3":
            surface_area_calculator()
        elif choice == "4":
            take_quiz()
        elif choice == "5":
            print("Thanks for using my calculator! Bye!")
            break
        else:
            print("Please pick a valid option!")

if __name__ == "__main__":
    main()