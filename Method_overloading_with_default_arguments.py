class test:
    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print("three argts: ",a+b+c)
        elif(a!=None and b!=None):
            print("two argts:",a+b)
        else:
            print("To perform sum min two operands and one operator is mandatory")


obj=test()
obj.sum(10,20,30)

