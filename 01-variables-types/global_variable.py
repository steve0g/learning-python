# Consider the following code:
# What will be the printed result?

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

# The result is Python is awesome because a variable defined inside a function only exists within that function.
# A function cannot modify a global variable if we redefine a variable of the same name inside it.

# Make the variable x belong to the global scope.
# Consider the following code: What will be the printed result?
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

# The result is Python is fantastic because we used the global keyword to modify the global variable x inside the function.