from multipledispatch import dispatch

class rectangle:
    @dispatch() 
    def func(self):
        self.a = 3
        self.s = 2

    @dispatch(float, float) 
    def func(self, a, s):
        self.a = a 
        self.s = s

    @dispatch(float, int) 
    def func(self, x, a):
        self.a = x 
        self.s = a

    @dispatch(int, float) 
    def func(self, a, s):
        self.a = a 
        self.s = s

    def area(self):
        print(self.a * self.s)  # Corrected area calculation
    
x = rectangle() 
x.func()
x.area()
