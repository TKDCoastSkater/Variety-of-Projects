def plotRegression(file_name):
    import turtle
    input_file = open(file_name, 'r')  # Modify the filename accordingly
    x = []
    y = []
    x_total = 0
    y_total = 0
    sum_xy = 0
    sum_x_squared = 0
    num_of_points = 0
    
    for line in input_file:
        sequence = line.split()
        x_val = int(sequence[0])
        y_val = int(sequence[1])
        
        x.append(x_val)
        y.append(y_val)
        x_total += x_val
        y_total += y_val
        sum_xy += x_val * y_val
        sum_x_squared += x_val ** 2
        num_of_points += 1
    
    x_mean = x_total / num_of_points
    y_mean = y_total / num_of_points 
    
    slope = (num_of_points * sum_xy - x_total * y_total) / (num_of_points * sum_x_squared - x_total ** 2)
    
    turtle.setworldcoordinates(min(x) - 5, min(y) - 5, max(x) + 5, max(y) + 5)
    turtle.speed(0)
    turtle.penup()
    turtle.pencolor("blue")
    
    for i in range(num_of_points):
        turtle.goto(x[i], y[i])
        turtle.dot(5)
    
    
    turtle.penup()
    turtle.pencolor("red")
    turtle.goto(min(x), y_mean + slope * (min(x) - x_mean))
    turtle.pendown()
    turtle.goto(max(x), y_mean + slope * (max(x) - x_mean))

    
    turtle.done()

plotRegression("C:/Users/Coast/Documents/Python/Begining Projects/Carteasian Plotter/test.txt")