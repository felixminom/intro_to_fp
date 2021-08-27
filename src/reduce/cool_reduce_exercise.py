# Here’s an example that combines map() and reduce()
# to calculate the total size of all the files
# that live in your home directory cumulatively
# this has to be run in your home directory
import functools
import operator
import os
import os.path

files = os.listdir(os.path.expanduser("~"))

size = functools.reduce(operator.add, map(os.path.getsize, files))
