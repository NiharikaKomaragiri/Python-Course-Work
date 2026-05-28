# encapsulation
class insta:
    def __init__(self, username, password, cf):
        self.username = username
        self.__password = password
        self._cf = cf

    def getpassword(self):
        return self.__password

    def setpassword(self, new_password):
        self.__password = new_password

    @property
    def accesscf(self):
        return self._cf

    @accesscf.setter
    def accesscf(self, new_cf):
        self._cf.append(new_cf)


niharika = insta('niharika', 'niharika@255', ['lohi', 'vijay', 'nivi'])

print("Before Username:", niharika.username)
niharika.username = 'niha'
print("After Username:", niharika.username)

print("Before password:", niharika.getpassword())
niharika.setpassword('niha@2004')
print("After password:", niharika.getpassword())

print("Before close friends:", niharika.accesscf)
niharika.accesscf = 'madhu'
print("After close friends:", niharika.accesscf)

OUTPUT
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/oops -2.py
Before Username: niharika
After Username: niha
Before password: niharika@255
After password: niha@2004
Before close friends: ['lohi', 'vijay', 'nivi']
After close friends: ['lohi', 'vijay', 'nivi', 'madhu']

