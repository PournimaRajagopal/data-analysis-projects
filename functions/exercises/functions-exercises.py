# Part 1 A -- Make a Line
def make_line(size):
   line = ""
   for i in range(size):
      line += "#"
   return line

print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ""
    for i in range(size):
        square += make_line(size) + "\n"
    return square

print(make_square(5))



# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
    rectangle = ""
    for i in range(height):
        rectangle += make_line(width) + "\n"
    return rectangle

print(make_rectangle(7, 3))



# Part 2 A -- Make a Stairs
def make_stairs(steps):
    stairs = ""
    for i in range(1, steps + 1):
        stairs += make_line(i) + "\n"
    return stairs

print(make_stairs(5))




# Part 2 B -- Make Space-Line 
def make_space_line(total_length, hash_count):
    spaces_count = total_length - hash_count
    line = ("#" * hash_count) + (" " * spaces_count)
    return line

print(make_space_line(10, 4))




# Part 2 C -- Make Isosceles Triangle
def make_isosceles_triangle(height):
    triangle = ""
    for i in range(1, height + 1):
        # Create each line with hashes centered
        line = " " * (height - i) + "#" * (2 * i - 1)
        triangle += line + "\n"
    return triangle

print(make_isosceles_triangle(5))




# Part 3 -- Make a Diamond
def make_diamond(height):
    diamond = ""
    
    # Top half of the diamond
    for i in range(1, height + 1):
        line = " " * (height - i) + "#" * (2 * i - 1)
        diamond += line + "\n"
    
    # Bottom half of the diamond
    for i in range(height - 1, 0, -1):
        line = " " * (height - i) + "#" * (2 * i - 1)
        diamond += line + "\n"
    
    return diamond
print(make_diamond(5))