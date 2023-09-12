# __new__() method
class Method:
    def __new__(cls):
        print("Creating an instance by __new__ method")
        return super(Method, cls).__new__(cls)

    def __init__(self):
        print("Init method is called here")


Method()


class SingletonClass:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)
