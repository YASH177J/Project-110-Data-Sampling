import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()
print("\n")
print("Polpulation mean:",statistics.mean(data))
print("Polpulation std:",statistics.stdev(data))
print("\n")

def randomSetofMeans(counter):
    datalist = []
    for i in range(0,counter):
        randIndex = random.randint(0,len(data)-1)
        value = data[randIndex]
        datalist.append(value)
    
    mean= statistics.mean(datalist)
    return mean

def show_fig(meanList):
    df = meanList
    mean = statistics.mean(meanList)
    fig = ff.create_distplot([df], ["Average"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,12],mode="markers+lines",name="Mean"))
    fig.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setOfMeans = randomSetofMeans(100)
        meanlist.append(setOfMeans)
    show_fig(meanlist)
    mean = statistics.mean(meanlist)
    print("Mean of sampling Distribution : ",mean)

setup()

def std_deviation():
    meanlist = []
    for i in range(0,1000):
        setOfMeans = randomSetofMeans(100)
        meanlist.append(setOfMeans)
    std = statistics.stdev(meanlist)
    print("Standard Deviation of Sampling Disrtibution is:",std)
    print("\n")

std_deviation()

#SD of the sampling mean =  SD Population / sqrt (number of data in each sample)
#sd of sampling mean = 3.935/ sqrt(100)
#sd  of the sampling mean= 0.3935