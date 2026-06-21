class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('The method __init__ foi chamado...')
        else:
            print(f'The instance was created: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

sl = Singleton()  # The class is instantiated, but the instance is not created yet

print(f'Instance object: {Singleton.get_instance()}')  # The instance is created and returned

s2 = Singleton()  # Instance already exists