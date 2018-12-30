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