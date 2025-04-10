from plotly.graph_objs import Bar, Layout
from plotly import offline 

import matplotlib.pyplot as plt 
from die import Dies

die_1 = Dies()
die_2 = Dies()
sides = die_2.sides+die_1.sides
x_values = list(range(1,sides+1))
# result = [] 
# for i in range(100000):
#     result.append(die_1.roll()*die_2.roll())

result = [die_1.roll()+die_2.roll() for i in range(10000)]

# frequency = []
# for value in x_values:             
#     frequency.append(result.count(value))

frequency = [result.count(value) for value in x_values]

data = Bar(x = x_values, y = frequency)

#dtick means value diff in axis 
x_axis_config = {'title':'Result','dtick' : 1}
y_axis_config = {'title':'Frequency of Result'}

my_layout = Layout(title = 'Result of rolling a 12 sided dies for 1000 times', xaxis= x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout':my_layout},filename = 'tutorial/pyplot/d6.html')




fig,ax = plt.subplots()
ax.plot(x_values,frequency,c = (0,0,0))
ax.set_title("Result of rolling a 12 sided dies for 10000 times" , fontsize = 25)
ax.set_xlabel("Result" , fontsize = 20)
ax.set_ylabel(f"Frequency of {sides} faced dies " , fontsize = 20)
ax.tick_params(axis = 'both', which = 'major', labelsize = 12)

plt.show()