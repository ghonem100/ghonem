class A(object): 
	def __init__(self, x): 
		self.x = x 
	
	def getX(self): 
		return self.X 


cond = True

class C(A if cond else object): 
	def isA(self): 
		return True

ca = C(1) 
print(ca.isA()) 

