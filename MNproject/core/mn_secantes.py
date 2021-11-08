import math as m

def f(x):
    fx = lambda x: m.sin(x)- (1/m.sin(x)) +1
    return fx(x)

def secante(a,b):
    p1 = f(b)
    p2 = a-b
    p3 = f(a) - f(b)
    result = b - p1*p2/p3
    return result

def main():
    a = 2
    b = 3
    error = 10**-10
    current_error = error*2
    init = 0
    iterMax=13
    i=0
    while not current_error <= error:
        sig = secante(a,b)
        current_error = round(abs(sig-b)/sig,5)
        print("Iteracion#",(i+1),"\n")
        print(f"""a={round(a,8)} 
b={round(b,8)} 
f(a)={round(f(a),8)} 
f(b)={round(f(b),8)} 
siguiente b={round(sig,8)} 
error={current_error}\n""")
        a = b
        b = sig
        if(iterMax == 0):
            print("Numero Max de Iteraciones alcanzado ")
            break
        i+=1
main()