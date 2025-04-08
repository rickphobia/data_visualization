from random_walk.random_walks import RandomWalk
import matplotlib.pyplot as plt
while True:
    rw = RandomWalk(50000)
    rw.walk()

    fig,ax  = plt.subplots(figsize = (15,9))
    point_number = range(rw.walk_count)
    ax.scatter (0,0, c = 'red', edgecolors= 'none', s = 100)
    # ax.plot(rw.x_values, rw.y_values, linewidth = 1 )
    #line 

    ax.scatter(rw.x_values, rw.y_values,c= point_number, cmap = plt.cm.Blues, s = 1 )
    #scatter

    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'green', edgecolors = 'none', s = 100)
    ax.set_title("Random Walks")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()

    quit == input("Continue or nah (y/n)")
    if quit == 'n':
        break