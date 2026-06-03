# 1) Create a class named `Point`.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # Store x in the instance variable self.x
        self.y = y  # Store y in the instance variable self.y

    def __str__(self):
        return f"({self.x}, {self.y})"  # Return a string representation of the point
# 2) Define the constructor method `__init__(self, x=0, y=0)`:

# a) Accept two optional parameters, x and y, both defaulting to 0.

# b) Store x in the instance variable `self.x`.

# c) Store y in the instance variable `self.y`.

# 3) Define the special method `__str__(self)`:

# a) This method is automatically called when the object is printed.

# b) Return a string representation of the point in coordinate format.

# c) Use the values stored in `self.x` and `self.y`.

# d) Example return value: "(2, 3)".

# 4) Create an object `p1` of the Point class:

# a) Pass the values 2 and 3 to the constructor.

# b) The object will have:

# - self.x = 2

# - self.y = 3

# 5) Print the object using `print(p1)`:
p=Point(2, 3)
print(p)
# a) Python automatically calls `p1.__str__()`.
r
# b) The returned string is displayed on the screen.

# c) Output:

# (2, 3)