def plotRegression(file_name):
    input_file = open(file_name, 'r')
    x = []
    y = []
    x_total = 0
    y_total = 0
    x_squared_total = 0
    num_of_points = 0
    
    for line in input_file:
        sequence = line.split()
        x_val = int(sequence[0])
        y_val = int(sequence[1])
        
        x.append(x_val)
        y.append(y_val)
        x_total += x_val
        y_total += y_val
        x_squared_total += x_val ** 2
        num_of_points += 1
    
    x_mean = x_total / num_of_points
    y_mean = y_total / num_of_points
    
    slope = ((x_total * y_total) - (num_of_points * x_mean * y_mean)) / ((x_squared_total) - (num_of_points * (x_mean ** 2)))
    line_turt = y_mean - (slope * x_mean)
    
    # Print the calculated values
    print("x:", x)
    print("y:", y)
    print("x_mean:", x_mean)
    print("y_mean:", y_mean)
    print("slope:", slope)
    print("line_turt:", line_turt)
plotRegression("Carteasian Plotter/test.txt")