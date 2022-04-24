import plotly.express as px
import csv
with open ("cups of coffee vs hours of sleep.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x= "Coffee in ml", y= "sleep in hours", color= "week")
      fig.show()
      import plotly.express as px
import csv 
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x= "Coffee in ml", y="sleep in hours", color="week")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["cups of coffee"]))
            sleep_in_hours.append(float(row["hours of sleep"]))

    return{"x" : ice_cream_sales, "y" : cold_drink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between cups of coffe vs hours of sleep :-  \n--->", correlation[0,1])
    
data_path = "cups of coffee vs hours of sleep.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)