# Approach 1
# import module1_with_class, module2_with_class
#
# x = module1_with_class.ClassX()
# x.function1_from_class_x()
# x.function2_from_class_x()
#
# y = module2_with_class.ClassY()
# y.function1_from_class_y()
# y.function2_from_class_y()


# # Approach 2
# from module2_with_class import *
# y = ClassY()
# y.function2_from_class_y()
# y.function1_from_class_y()
#
# from module1_with_class import *
# x = ClassX()
# x.function2_from_class_x()
# x.function1_from_class_x()

# Approach 3
from module1_with_class import ClassX
x = ClassX()
x.function1_from_class_x()
x.function2_from_class_x()

from module2_with_class import ClassY
y = ClassY()
y.function1_from_class_y()
y.function2_from_class_y()