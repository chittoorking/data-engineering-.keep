# You and a group of friends are working on building an amazing new Python IDE (integrated development environment -- like PyCharm, Spyder, Eclipse, Visual Studio, etc.). 
# The team wants to add a feature that displays a tooltip with a function's docstring whenever the user starts typing the function name.
# That way, the user doesn't have to go elsewhere to look up the documentation for the function they are trying to use. 
# You've been asked to complete the build_tooltip() function that retrieves a docstring from an arbitrary function.

# You will be reusing the count_letter() function that you developed in the last exercise to show that we can properly extract its docstring.

# Instructions 
# Begin by getting the docstring for the function count_letter(). Use an attribute of the count_letter() function.

# Get the "count_letter" docstring by using an attribute of the function
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

# output:

# ############################
# Count the number of times `letter` appears in `content`.

#   Args:
#     content (str): The string to search.
#     letter (str): The letter to search for.

#   Returns:
#     int

#   Raises:
#     ValueError: If `letter` is not a one-character string.
  
# #########################

import inspect

# Inspect the count_letter() function to get its docstring
docstring =inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

# output:
## ##########################
# Count the number of times `letter` appears in `content`.

# Args:
#   content (str): The string to search.
#   letter (str): The letter to search for.

# Returns:
#   int

# Raises:
#   ValueError: If `letter` is not a one-character string.
# ############################

# Now create a build_tooltip() function that can extract the docstring from any function that we pass to it.

import inspect

def build_tooltip(function):
  """Create a tooltip for any function that shows the
  function's docstring.

  Args:
    function (callable): The function we want a tooltip for.

  Returns:
    str
  """
  # Get the docstring for the "function" argument by using inspect
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))

# ############################
# Count the number of times `letter` appears in `content`.

# Args:
#   content (str): The string to search.
#   letter (str): The letter to search for.

# Returns:
#   int

# Raises:
#   ValueError: If `letter` is not a one-character string.
# ############################
# ############################
# range(stop) -> range object
# range(start, stop[, step]) -> range object

# Return an object that produces a sequence of integers from start (inclusive)
# to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
# start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
# These are exactly the valid indices for a list of 4 elements.
# When step is given, it specifies the increment (or decrement).
# ############################
# ############################
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.
# ############################
