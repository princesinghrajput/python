'''import maths

print(maths.a)
'''

#! To import particular modules from packages

from maths import simple

# print(simple.add(10,20))

#! We can also do like  this to import multiple modules from a packages

from maths import (
    simple,
    complex
)

print(simple.add(10,20))
print(complex.square(10))