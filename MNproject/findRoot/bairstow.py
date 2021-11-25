import cmath
import random

dumpStr = ""  
def bairstow(a,r,s,g,roots):
	
	if(g<1):
		return None
	if((g==1) and (a[1] != 0)):
		roots.append(float(-a[0])/float(a[1]))
		return None
	if(g==2):
		D = (a[1]**2.0)-(4.0)*(a[2])*(a[0])
		X1 = (-a[1] - cmath.sqrt(D))/(2.0*a[2])
		X2 = (-a[1] + cmath.sqrt(D))/(2.0*a[2])
		roots.append(X1)
		roots.append(X2)
		return None
	n = len(a)
	b = [0]*len(a)
	c = [0]*len(a)
	b[n-1] = a[n-1]
	b[n-2] = a[n-2] + r*b[n-1]
	i = n - 3
	while(i>=0):
		b[i] = a[i] + r*b[i+1] + s*b[i+2]
		i = i - 1
	c[n-1] = b[n-1]
	c[n-2] = b[n-2] + r*c[n-1]
	i = n - 3
	while(i>=0):
		c[i] = b[i] + r*c[i+1] + s*c[i+2]
		i = i - 1
	Din = ( (c[2]*c[2]) - (c[3]*c[1]) )**(-1.0)

	r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
	global dumpStr
	dumpStr += f"""(deltaR: {(Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))}\n"""
	s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))
	dumpStr += f"""(deltaS: {(Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))}\n"""

	if(abs(b[0]) > 1E-14 or abs(b[1]) > 1E-14):
		return bairstow(a,r,s,g,roots)
	if (g>=3):
		Dis = ((-r)**(2.0))-((4.0)*(1.0)*(-s))
		X1 = (r - (cmath.sqrt(Dis)))/(2.0)
		X2 = (r + (cmath.sqrt(Dis)))/(2.0)
		roots.append(X1)
		roots.append(X2)
		return bairstow(b[2:],r,s,g-2,roots)	

# k = 0	#str
# g = 5	#grado de la ecuacion
# roots = []
# a = [1,-3.5,2.75,2.125,-3.875,1.25]	#coeficientes
# r = random.random()
# s = random.random()
# bairstow(a,r,s,g,roots)
# print("\nFound Roots => \n")
# for r in roots:
# 	print("R" + str(k) + " = " + str(r))
# 	k += 1

def bairstowMain(COEFICIENTES,r=None,s=None):
	global dumpStr
	dumpStr = ""
	if not COEFICIENTES:
		return "Necesitas llenar el aprametro Coeficientes!\n"
		#COEFICIENTES = [1, -3.5 ,2.75 ,2.125 ,-3.875 ,1.25]	#coeficientes
	g = 3 	#grado de la ecuacion
	if not r or not s:
		r = random.random()
		s = random.random()
	roots = []	
	bairstow(COEFICIENTES,r,s,g,roots)
	k=0
	mystr = ""
	for r in roots:
		mystr += ("R" + str(k) + " = " + str(r)+"\n")
		k += 1
	mystr += "\n\n"+dumpStr
	return mystr	

if __name__ == "__main__":
	COEFICIENTES = [1, -3, 3 , -1]
	mystr = bairstowMain(COEFICIENTES,r=0,s=0)	
	print(mystr)
