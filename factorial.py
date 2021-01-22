class expr:
	def __init__(self,S,d = None):#converts string to parse tree if not
		if (d):
			self.expr = d
		else:
			(e,n) = self.parse(S)
			self.expr = e
	class Node:#returns node to the tree
		def __init__(self,d):
			self.left = None
			self.right = None
			self.data = d
		def toString(self):#the tree recombination coverts the left and the right string
			if (self.left and self.right):
				left = self.left.toString()
				right = self.right.toString()
				opr = self.data
				return "(" + left + " " + opr + " " + right + ")"
			else:
				return self.data
	def pstring(self):#prints the tree that is converted to the string
		st=self.expr.toString()
		print(st)
	def parse(self,S):#returns the parse tree
		l = len(S)
		if (S[0] == "("):
			(left,n) =  self.parse(S[1:l-2])
			opr = S[n+1]
			(right,m) = self.parse(S[n+2:l-1])
			expr = self.Node(opr)
			expr.left = left
			expr.right = right
			return (expr,n+m+3)
		elif S[0].isdigit():
			i = 0
			while ((i < l) and (S[i].isdigit() or (S[i] == "."))):
				i = i+1
			num = S[0:i]
			expr = self.Node(num)
			return (expr,i)
		elif S[0].isalpha():
			i = 0
			while ((i < l) and S[i].isalpha()):
				i = i+1
			var = S[0:i]
			expr = self.Node(var)
			return (expr,i)
		else:
			return Exception("Invalid input")
	def constant(self):#checks if node is a constant
		if self.expr.data[0].isdigit():
			return 1
		else:
			return 0
	def variable(self):#checks if node is a variable
		if self.expr.data[0].isalpha():
			return 1
		else:
			return 0
	def samevariable(self,x):#checks if the current node has the same variable 
		if (self.expr.data == x):
			return 1
		else:
			return 0
	def subtract(self):#checks if the node has the negative sign
		if self.expr.data== '-':
			return 1
		else:
			return 0
	def multiply(self):#checks for the multiplication sign
		if self.expr.data=='*':
			return 1
		else:
			return 0
	def divide(self):#checks for the division sign
		if (self.expr.data == '/'):
			return 1
		else:
			return 0		
	def sumu(self):#checks for the addition sign
		if (self.expr.data == '+'):
			return 1
		else:
			return 0
	def exponent(self):#checks for exponent
		if (self.expr.data == 'A'):
			return 1
		else:
			return 0		
	def addend(self):#returns left parse tree side
		left = self.expr.left
		return expr("",left)
	def augend(self):#returns left tree side
		right = self.expr.right
		return expr("",right)
	def makesum(self,e1,e2):#combines two nodes under the + sign
		e = self.Node("+")
		#Original
		#e.left = e1
		#e.right = e2
		#Modified
		e.left = e1.expr
		e.right = e2.expr
		return expr("",e)
	def makeprod(self,e1,e2):#combines two nodes under the * sign
		e=self.Node("*")
		e.left=e1.expr
		e.right=e2.expr
		return expr("",e)
	def makediff(self,e1,e2):#combines two nodes under the - sign
		e=self.Node("-")
		e.left=e1.expr
		e.right=e2.expr
		return expr("",e)
	def makediv(self,e1,e2):#combines two nodes under the / sign
		e=self.Node("/")
		e.left=e1.expr
		e.right=e2.expr
		return expr("",e)    
	def makelog(self,e1,e2):
		e=self.Node("* ln")
		e.left=e1.expr
		e.right=e2.expr
		return expr("",e)
	def derive(self,x):#used to differentiate the tree
		if self.constant():
			return expr("0.0")
		if self.variable():
			if self.samevariable(x):
				return expr("1.0")
			else:
				return expr("0.0")
		elif self.sumu():#differentiation under + operator
			e1 = self.addend()
			e2 = self.augend()
			d1=e1.derive(x)
			d2=e2.derive(x)
			if (e1.constant()==1 or (e1.variable()==1 and e1.samevariable(x)==0)):
				return d2
			if (e2.constant()==1 or (e2.variable()==1 and e2.samevariable(x)==0)):
				return d1
			else:
				return self.makesum(d1,d2)
		elif self.subtract():#differentiation under - operator
			e1 = self.addend()
			e2 = self.augend()
			d1=e1.derive(x)
			d2=e2.derive(x)
			if (e2.constant()==1 or (e2.variable()==1 and e2.samevariable()==0)):
				return d1
			else:
				return self.makediff(d1,d2)
		elif self.multiply():#differentiation under * operator
			e1 = self.addend()
			e2 = self.augend()
			d1=e1.derive(x)
			d2=e2.derive(x)
			return self.makesum(self.makeprod(e1,d2),self.makeprod(d1,e2))		    
		elif self.divide():#differentiation under / operator
			e1 = self.addend()
			e2 = self.augend()
			d1=e1.derive(x)
			d2=e2.derive(x)
			return self.makesum(self.makediff(self.makeprod(d1,e2),self.makeprod(e1,d2)),self.makeprod(e2,e2))
		elif self.exponent():
			e1.self.augend()
			e2.self.addend()
			d1=e1.derive(x)
			d2=e2.derive(x)
			return self.makeprod(self.makeexponent(e2,e1),selfmakesum(self.makelog(e1,d2),selfdiv(self.makeprod(e2,d1),e2)))
		else:
			raise Exception("DontKnow")
str1=input("input any expression: ")
e=expr(str1)
e.pstring()
f=e.derive('x')
f.pstring()

#referred from codes done in the class
#had discussions with some of my friends
#used some codes like classes that were wriiten by sir 