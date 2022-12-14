import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

def DataCuration():
    daysList = [118,151,121,96,110,117,132,104,125,118,125,123,110,127,131,99,126,144,136,126,91,130,62,112,99,161,78,124,119,124,128,131,113,88,75,111,97,112,101,101,91,110,100,130,111,107,105,89,126,108,97,94,83,106,98,101,108,99,88,115,102,116,115,82,110,81,96,125,104,105,124,103,106,96,107,98,65,115,91,94,101,121,105,97,105,96,82,116,114,92,98,101,104,96,109,122,114,81,85,92,114,111,95,126,105,108,117,112,113,120,65,98,91,108,113,110,105,97,105,107,88,115,123,118,99,93,96,54,111,85,107,89,87,97,93,88,99,108,94,74,119,102,47,82,53,115,21,89,80,101,95,66,106,97,87,109,57,87,117,91,62,65,94,86,70,76,85]
    csvf = open('hw5.csv','w')
    writer = csv.writer(csvf)
    header = ['years', 'days']
    writer.writerow(header)
    
    for i in range(167):
        row = [i + 1855, daysList[i]]
        writer.writerow(row)
def VisualizeData():
    x = []
    y = []
    with open(sys.argv[1], 'r') as f:
        reader = csv.reader(f, delimiter=',')
        count = -1
        for row in reader:
            count += 1
            if(count == 0):
                continue
            x.append(int(row[0]))
            y.append(int(row[1]))
    plt.plot(x,y)
    plt.xlabel('Year')
    plt.ylabel('Number of frozen days')
    plt.savefig("plot.jpg")

def LinearRegression():
    x = []
    y = []
    with open(sys.argv[1], 'r') as f:
        reader = csv.reader(f, delimiter=',')
        count = -1
        for row in reader:
            count += 1
            if(count == 0):
                continue
            x.append(int(row[0]))
            y.append(int(row[1]))
    X = []
    for xi in x:
        part = [1,xi]
        X.append(part)
    X = np.array(X)
    print("Q3a: ")
    print(X)
    Y = []
    for yi in y:
        Y.append(yi)
    Y = np.array(Y)
    print("Q3b: ")
    print(Y)
    Z = np.dot(np.transpose(X), X)
    print("Q3c: ")
    print(Z)
    I = np.linalg.inv(Z)
    print("Q3d: ")
    print(I) 
    PI = np.dot(I, np.transpose(X))
    print("Q3e: ")
    print(PI)
    hat_beta = np.dot(PI, Y)
    print("Q3f: ")
    print(hat_beta)
    return hat_beta
def Prediction(hat_beta):
    y_test = hat_beta[0] + hat_beta[1] * 2021
    print("Q4: " + str(y_test))
def ModelInterpreatation(hat_beta):
    h = hat_beta[1]
    sym = ''  
    if(h < 0):
        sym = '<'
    elif(h == 0):
        sym == '='
    else:
        sym = '>'
    print("Q5a: ")
    print(sym)
    print("Q5b: Through the answer printed in prediction : y_test = 483.665815 - 0.196965793 * x_test. Through the interpretation of the sign of beta_1 which is -0.196965793 which is less than 0 (the sign : <), the linear regression from the model interpretation means the number of day mendota freeze is predicted to be decreasing as year (which is x_test) passed. This sign means how the day of mendota freeze increased or decreased (if the sign is >, increased, and if the sign is <, mendota ice decreased).	")

def ModelLimitation(hat_beta):
    x_star = -hat_beta[0]/hat_beta[1]
    print('Q6a: ')
    print(x_star)
    print('Q6b: First of all, the x* produce the data of 2455.5828057138465 which means that the number of days that the mendota ice freezes is less than 0 which never freezes after the year has passed about 2455. However, in my opinion based on the model interpretation, although the linear regression formula shows the day of mendota freezes would go less than 0, because the graph plot from Q2 shows that the number of frozen days are dynamically changing which means that it is hard to predict that the number of frozen days will no longer freeze after the zero.')
        

    
    # for line in lines:
    #     x.append(line[0])
if __name__ == "__main__":
    DataCuration()
    hat_beta = LinearRegression()
    Prediction(hat_beta)
    ModelInterpreatation(hat_beta)
    ModelLimitation(hat_beta)


    
    
