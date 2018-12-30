'''
FORMULA:
N=m+(m/n)-1
Where N->Population Maximum
m->sample maximum or highest observed serial number
n-sample size
'''

def EstimatedPopulation(observed_set):
    N=max(observed_set)+( max(observed_set)/len(observed_set) )-1
    return N
# Problem 1- German Tanks
print (EstimatedPopulation([1,31,43,79,115]))

# Problem 2- Citti Hoppa Buses in Nairobi CBD
print (EstimatedPopulation([663,816,458,772,584,229,717,882,422]))

#problem 3- How many students have passed through a secondary school?
print (EstimatedPopulation([1936,1852,1741,2050,2154,2758,1909,1734,1818,2064,3040,2020,1560,5060,4788]))