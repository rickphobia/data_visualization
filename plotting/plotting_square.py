import matplotlib.pyplot as plt 
x_values= list(range(1,10))
y_values = [i**2 for i in x_values]



fig, ax = plt.subplots()
ax.plot(y_values)
plt.show()