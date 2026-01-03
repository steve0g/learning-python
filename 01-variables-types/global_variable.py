# Consider the following code:
# What will be the printed result?

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

# The result is Python is awesome because a variable defined inside a function only exists within that function.
# A function cannot modify a global variable if we redefine a variable of the same name inside it.