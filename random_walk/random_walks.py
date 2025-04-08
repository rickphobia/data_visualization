from random import choice

class RandomWalk:
    def __init__(self,walk_count = '5000'):
        self.walk_count = walk_count

        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        while len(self.x_values) < self.walk_count:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step ==0 and y_step == 0:
                continue 

            x= self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step 

            self.x_values.append(x)
            self.y_values.append(y)
            

            
    def get_step(self): 
            dir= choice([1,-1])
            movement  = choice(list(range(0,8)))
            step = dir*movement
            return step 
            

        