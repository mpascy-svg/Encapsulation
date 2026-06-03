# 1) Create a class named `myClass`.
class myClass:
    __privateVar = 27  # Private class variable

    def __privMeth(self):  # Private method
        print("I'm inside class myClass")

    def hello(self):  # Public method
        print("as private variable value",myClass.__privateVar) 
               # Accessing the private variable   
# 2) Inside the class, create a private class variable 

    
# (The double underscore makes it name-mangled, so it cannot be accessed directly outside the class.)

# 3) Define a private method `__privMeth(self)`:

# a) This method prints "I'm inside class myClass".

# (It is also name-mangled because of the double underscore.)

# 4) Define a public method `hello(self)`:

# a) Print the value of the private variable using `myClass.__privateVar`.

# 5) Create an object `foo` of the class `myClass`.
foo = myClass()
# 6) Call the public method `foo.hello()` to display the private variable value.
foo.hello()

# 7) Attempt to access the private method using `foo.__privMeth`.
foo.__privMeth()

# (This will not work directly because `__privMeth` is private/name-mangled.)
foo._myClass__privMeth()  # Accessing the private method using name mangling