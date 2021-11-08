import math as m
#     fx = lambda x: math.exp(-1*x) - x
#     dfx = lambda x: -1*math.exp(-1*x) -1
#     fx = lambda x: x**3 - 5*x
#     dfx = lambda x: 3*x**2 -5
#     fx = lambda x: x**3 +3*x**2 -1
#     dfx = lambda x: 3*x**2 + 6*x
#     fx = lambda x: m.sqrt((x-2)**2 + m.e**(2*x) )
#     dfx = lambda x: ( x- 2 + m.e**(2*x) ) / ( m.sqrt( (x-2)**2 + m.e**(2*x) ) )
def main():
    fx = lambda x: x+m.e**(2*x)-2
    dfx = lambda x: 1+m.e**(2*x)*2
    error = 10**-6
    init = 1
    tolera = abs(error*2)
    memory = 0
    iterMax=13
    i = 0
    while not tolera <= error:
        memory = init
        if dfx(init) == 0:
                print("Tabgente Horizontal")
                break
        init = init - fx(init)/dfx(init)
        # print(init)
        tolera = abs(init - memory)

        stri1 = f"""
xi = {round(memory,5)} 
xi+1 = {round(init,5)} 
f(xi) = {round(fx(init),8)} 
error = {round(abs((init - memory )/init)*100,2)}%"""   
        print("Iteracion #",(i+1)) 
        print(stri1+"\n")
        if abs(memory) == abs(init):
                print("Punto Oscilatorio!")
                break
        if(iterMax == 0):
                print("Excedimos el numero Max de iteraciones")
                break
        i+=1
        iterMax-=1
main()