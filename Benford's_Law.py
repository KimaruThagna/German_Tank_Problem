suspected_series=[23.65,124.34,8321.45,52346.22,8.45,5,6300]

def DigitFrequencyDistribution(suspected_series):
    #Obtain the first digit from the numbers in the series
    first_digit=[]
    for val in suspected_series:
        val=int(val)
        first_digit.append(int(str(val) [:1]) )
    return first_digit

print(DigitFrequencyDistribution(suspected_series))