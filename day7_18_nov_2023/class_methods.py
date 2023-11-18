# In python there are two types of methods in a class
# Instance Methods : Requires object of class
# Static Methods : Does not require object of class, instead class name is used
# Static methods : Common for every object & can be defined using @staticmethod

class ClassMethods:
    def instance_method(self):
        print("This is an instance method. Hence this is being called using class object")

    @staticmethod
    def static_method():
        # For static methods 'self' keyword is treated as the normal variable instead of class name
        print("This is a static method, being called by class name")


cm = ClassMethods()
cm.instance_method()
ClassMethods.static_method()