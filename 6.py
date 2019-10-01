class validate:
    def __init__(self):
        self.open_list = ["[","{","("] 
        self.close_list = ["]","}",")"]
        self.s=""
        self.stack = []


    def check(self,s):
        for i in s:
            if i in self.open_list: 
		    self.stack.append(i) 
	    elif i in self.close_list: 
		    pos = self.close_list.index(i) 
		    if ((len(self.stack) > 0) and(self.open_list[pos] == self.stack[len(self.stack)-1])): 
			self.stack.pop() 
		    else:
                        return "Unbalanced"
	 if len(self.stack) == 0: 
		return "Balanced"

while True:
    string =input("enter string")
    print(validate().check(string)) 


