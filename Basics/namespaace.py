
var = 10
def simple_fun():
    var = 11
    #print(var)
    def iner_f():
        var = 12
        print(var)
    iner_f()

simple_fun()
