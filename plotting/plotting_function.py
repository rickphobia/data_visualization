import matplotlib.pyplot as plt 

print(plt.style.available)

func = input("Enter the f(x) in terms of x\n")
ini_range = int(input("Enter ur initial range"))
fin_range = int(input("Enter ur final range"))
func_x = [] 
for i in range(ini_range,fin_range):
    num = func.replace('x','*i')
    func_x.append(eval(num))

plt.style.use('bmh')
fig, ax= plt.subplots()
# fig is all the values connecting a line
# while ax is the points we are giving 

ax.plot(range(ini_range,fin_range),func_x,linewidth = 5)
#give initial input and output to let is run without any problem 

ax.set_title(f"{func}",fontsize = 30)
ax.set_xlabel("x", fontsize = 12)
ax.set_ylabel("f(x)", fontsize= 15)
ax.tick_params(axis='both', labelsize=10)
#settings the number on the axis 
plt.show()