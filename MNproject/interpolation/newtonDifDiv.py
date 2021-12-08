import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

# matplotlib inline
def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial 
    at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

import plotly.graph_objects as go

def difDivMethod(X,Y):
    coorX = np.array(X)
    coorY = np.array(Y)
    coefs = divided_diff(coorX, coorY)[0,:]
    #ahora a probar el polinomio que esta en "coefs"
    newCoordX = np.arange(X[0],X[-1]+0.1,0.1)
    newCoordY = newton_poly(coefs,coorX,newCoordX)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=newCoordX, y=newCoordY))
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)

    context = {
        "coefs":coefs,
        "graph":graph
    }
    return context


if __name__ == "__main__":
    context = difDivMethod([-5, -1, 0, 2],[-2, 6, 1, 3])
    
    # x = np.array([-5, -1, 0, 2])
    # y = np.array([-2, 6, 1, 3])
    # # get the divided difference coef
    # a_s = divided_diff(x, y)[0, :]

    # # evaluate on new data points
    # x_new = np.arange(-5, 2.1, .1)
    # y_new = newton_poly(a_s, x, x_new)

    # plt.figure(figsize = (12, 8))
    # plt.plot(x, y, 'bo')
    # plt.plot(x_new, y_new)
    # plt.show()
