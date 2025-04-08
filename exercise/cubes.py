import matplotlib.pyplot as plt 
fin_value = int(input('How many cubes do you wanna '))
x_values = list(range(1,fin_value+1))
y_values = [i**3 for i in x_values]

fig,ax = plt.subplots()

ax.set_title('x**3',fontsize = 30)
ax.set_xlabel('x',fontsize = 15)
ax.set_ylabel('f(x)',fontsize = 15)
ax.tick_params(axis = 'both', labelsize = 10)

ax.scatter(x_values,y_values, c = y_values, cmap= plt.cm.Blues, s=30)
ax.axis([1,fin_value+3,0,fin_value**3 +100])

plt.show()