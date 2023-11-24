import sys
sys.path.append("/Users/shripadkale/Documents/Python/Selenium_With_Python/BasicPython/day9_23_nov_2023/package_demo")


x, y = int(input("Enter First Number : ")), int(input("Enter Second Number : "))


import package_demo.first_module as fm
import package_demo.second_module as sm
fm.perform_power(x, y)


sm.compare_number(x, y)
sm.who_is_greater(x, y)

