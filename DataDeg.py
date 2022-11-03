#Jacob Silveira
#CST-305
#Project 4 Degradation of Data Integrity

#Solutions to plot were first solved by hand as seen in document file
#Then results are plotted using Matplotlib

#libraries to import
import numpy as np
import matplotlib.pyplot as plt

#defining the answers from part 2 to graph 
def sol2_P1(t): #first solution
    return np.exp(-t/20)
def sol2_P2(t): #second solution 
    return -1*np.exp(-t/20)

#plotting results

# define the time points
t = np.linspace(-100,100,1000)
plt.plot(t,sol2_P1(t),'r-', label='First X(t) line') #first line will be red
plt.plot(t,sol2_P2(t),'b-', label='Second X(t) line') #second line will be blue 

#labeling graph axies 
plt.title('Part 2:')
plt.xlabel('t val')
plt.ylabel('y val')
plt.legend()

#Show graph 
plt.show()
