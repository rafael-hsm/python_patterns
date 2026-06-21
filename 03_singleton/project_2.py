class SanityCheck:
 
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(SanityCheck, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__initialized:
            self.__server = []
            self.__initialized = True

    def check_server(self, srv):
        print(f'Check the {self.__server[srv]}')
    

    def add_server(self):
        self.__server.append('Server 1')
        self.__server.append('Server 2')
        self.__server.append('Server 3')
        self.__server.append('Server 4')

    def change_server(self):
        self.__server.pop()
        self.__server.append('Server 5')

sc1 = SanityCheck()

sc2 = SanityCheck()

sc1.add_server()
print('Cronogram of check servers A....')
for srv in range(4):
    sc1.check_server(srv)

print(dir(sc1))
sc2.change_server()
print('Cronogram of check servers B....')
for srv in range(4):
    sc2.check_server(srv)

