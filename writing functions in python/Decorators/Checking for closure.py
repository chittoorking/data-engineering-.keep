# You're teaching your niece how to program in Python, and she is working on returning nested functions. 
# She thinks she has written the code correctly, but she is worried that the returned function won't have the necessary information when called.
# Show her that all of the nonlocal variables she needs are in the new function's closure.

# Instructions
# Use an attribute of the my_func() function to show that it has a closure that is not None.

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)

# output:
# True

# Show that there are two variables in the closure.
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)

# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)

# output:
# True
# True

# Get the values of the variables in the closure so you can show that they are equal to [2, 17], the arguments passed to return_a_func().
# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])

# True
