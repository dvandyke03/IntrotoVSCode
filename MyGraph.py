import matplotlib.pyplot as plt
import numpy as np

#create a virtual environment
    #python3-m venv___________ (name of virtual environment)
#activate your VE
    #source myvenv/bin/activate
#install 3rd party library
    #pip3 install matplotlib

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
