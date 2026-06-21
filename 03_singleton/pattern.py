class Singleton(object):

    def __new__(cls):
        """Override the __new__ method to control the object creation process. 
        This method is called before __init__ and is responsible for returning a 
        new instance of the class."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Creating object {cls.instance}')
        return cls.instance
    

s1 = Singleton()
print(f'Instance 1: {id(s1)}')

s2 = Singleton()
print(f'Instance 2: {id(s2)}')
