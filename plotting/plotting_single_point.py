import matplotlib.pyplot as plt 

print(plt.style.available)
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
y_value =[]
func = input('Whats ur f(x)')
for i in range(1,10):
    num = func.replace('x', '*i')
    y_value.append(eval(num))

#scatter
#c = y_value is to colors the initial values with lighter color, then cmap.plt.cm.{colours} is to plot gradient
ax.scatter(range(1,10),y_value,s= 150,c= y_value, cmap=plt.cm.Blues)
ax.set_title(func)
ax.set_xlabel('x',fontsize = 17)
ax.set_ylabel('f(x)',fontsize = 17)
ax.tick_params(axis='both', which ='major', labelsize= 15)


# saving the images, first argument is directory, second argument is whitespace 
plt.savefig(f'images/scatter_{func}.png', bbox_inches = 'tight')

