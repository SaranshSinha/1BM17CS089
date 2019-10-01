class callDetail:
    def __init__(self):
        self.caller=0
        self.reciever=0
        self.dur=0
        self.type=""

    def enter_val(self,c,r,d,t):
        self.caller=c
        self.reciever=r
        self.dur=d
        self.type=t

    def disp(self):
        print(self.caller,"\t",self.reciever,"\t ",self.dur,"\t",self.type)
        print()


class util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call):
        self.list_of_call_objects=list_of_call
        for s in self.list_of_call_objects:
         t=s.split(",")
         ob=callDetail()
         ob.enter_val(int(t[0]),int(t[1]),int(t[2]),t[3])
         ob.disp()

call1='9410390669,7895644935,10,std'
call2='9412141618,01352766628,5,isd'
call3='7350836793,9997894282,15,roaming'
list1=[call1,call2,call3]
print("CALLER\t\tRECIEVER   DURATION \tTYPE")
util().parse_customer(list1)
                
        
