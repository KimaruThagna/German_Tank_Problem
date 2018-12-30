'''
BEDFORD'S LAW
t states that in certain datasets the leading digit is distributed in a predictable
 but non-uniform manner. That is, observations with a lower first digit (1, 2, …)
 occur more often than those with a higher first digit (… 8, 9). This property arises in many situations
but is known to occur when the underlying measurements have a log-uniform distribution:
This can be applied to detect fradulent transactions.
If fradulent, the frequency distribution will be almost flat but not a smooth curve from a high 1 to a low 9

'''
import matplotlib.pyplot as plt
suspected_series=[23.65,124.34,8321.45,52346.22,8.45,5,6300]

def DigitFrequencyDistribution(suspected_series):
    #Obtain the first digit from the numbers in the series
    first_digit=[]
    for val in suspected_series:
        val=int(val)
        first_digit.append(int(str(val) [:1]) )
    # obtain the frequency distribution of the numbers
    freq_dist={}
    digit_list=[1,2,3,4,5,6,7,8,9]
    count=0
    for val in digit_list:
        for item in first_digit:
            if item==val:
                count+=1
        freq_dist[val]=count
        count=0

    return freq_dist,first_digit
# Plot the frequency distribution
print(DigitFrequencyDistribution(suspected_series))
freq,digit_list=DigitFrequencyDistribution(suspected_series)
plt.bar(list(freq.keys()),list(freq.values()))
plt.xticks(list(freq.keys()) )
plt.title('BEDFORDs DISTRIBUTION')
plt.show()