import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":


    x_data = np.array([-2., -1., 1., 2.])
    y_data = np.array([[4.], [5.], [1.], [8.]])
    A = np.vander(x_data)
    p = np.linalg.solve(A,y_data)

    plt.plot(x_data,y_data,"r*")
    x_new = np.linspace(x_data[0] - 1, x_data[len(x_data) - 1] + 1)
    y_new = np.polyval(p, x_new)
    plt.plot(x_new, y_new, 'b--')
    plt.grid(color='pink', linestyle='solid', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Poly interp with Vandermonde')
    plt.legend(['data', 'Poly interp'])
    plt.show()

