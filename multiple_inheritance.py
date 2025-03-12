'''
#one sub class can inherit or derived from
#more then one class as base class
#x-->z
#y-->
#p-->z

class x:
    fixed_assests=1000000
    def x_method(self):
        print("x method:",self.fixed_assests)


class y:
    y_fixed_assests = 2000000

    def y_method(self):
        print("y method:", self.y_fixed_assests)


class p:
    p_fixed_assests = 3000000

    def p_method(self):
        print("p method:", self.p_fixed_assests)

class v:
    v_fixed_assests=4000000
    def v_method(self):
        print("v method",self.v_fixed_assests)


class z(x,y,p,v):
    z_bank_bal=500000
    def z_method(self):
        print("z method:",self.z_bank_bal)
'''


class a:
    def a_method(self):
        print("value of b:",self.a_method)


class b(a):
    def ba_method(self):
        print("value of ba",self.ba_method)


class c(a):
    def ca_method(self):
        print("value of ca",self.ca_method)


class d(a):
    def da_method(self):
        print("value of da",self.da_method)


class e(a):
    def ea_method(self):
        print("value of ea",self.ea_method)


class b1(b):
    def b1b_method(self):
        print("value of b1b",self.b1b_method)


class b2(b):
    def b2b_method(self):
        print("value of b2b",self.b2b_method)


class d1(a):
    def d1a_method(self):
        print("value of d1a",self.d1a_method)


class d2(b):
    def d2b_method(self):
        print("value of d2b",self.d2b_method)

class e1(e):
    def e1e_method(self):
        print("value of e1e",self.e1e_method)


class e2(e):
    def e2e_method(self):
        print("value of e2a",self.e2e_method)


class e21(e2):
    def e21e2_method(self):
        print("value of e21e2",self.e21e2_method)


obj=b1()
obj.b1b_method()
obj.ba_method()




