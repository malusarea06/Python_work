class Demo:
    name = 'aniket'
    __nae = 'malusare'
    def __init__(self,a,b):
        self.name=a
        self.__nae=b
        print(Demo.name+" "+Demo.__nae)

    def fun(self,address):
        self.address = address


    def getAdd(self,address):
        self.address = address

    def getAddress(self):
        print(self.address)
        print(self.name)

    def __str__(self):
        return "From Str : a is %s  and b is %s"%(self.name,self.__nae)

    def __repr__(self):
        return "From return : a is %s and b is %s"%(self.name,self.__nae)



obj = Demo('1234','4321')
print(obj)
print([obj])
#obj.getAdd('Aundh')
#obj.getAddress()
#obj.fun('Pune')
#obj.getAddress()
#print(obj._Demo__nae)

