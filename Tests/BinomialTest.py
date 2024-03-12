#Binomial Test
def BinomialTest(file_name,column,pr,P_value,tails):
    import pandas as pd 
    from scipy.stats import binom_test
    data=pd.read_excel(str(file_name)+'.xlsx')
    x=sum(data[column])
    n=len(data[column])
    p_v=binom_test(x, n, pr, alternative='greater')
    print('\nWe are now checking whether the proportion of successes (i.e. "1") on column "'+str(column)+'" differs significantly from "'+str(pr)+'"\n', '\nIn this case the  p-value is: '+str(round(float(p_v),4)*int(tails))+'.\n')
    if round(float(p_v),4)*int(tails) < P_value:
        message='The proportion of '+str(data[str(column)].unique()[1])+' in the variable "'+str(column)+'" for this particular sample is '+str(round((sum(data[str(column)])/len(data[str(column)]))*100,2))+'%'+', which is statistically significantly different from the hypothesized value of '+str(float(pr)*100)+'%'+'.\n'
    else:
        message='The proportion of '+str(data[str(column)].unique()[1])+' in the variable "'+str(column)+'" for this particular sample is '+str(round((sum(data[str(column)])/len(data[str(column)]))*100,2))+'%'+', which is NOT statistically significantly different from the hypothesized value of '+str(float(pr)*100)+'%'+'.\n'
    return message
##### input data from here ####
x=0
while x==0:
    try:
        print('A one sample binomial test allows us to test whether the proportion of successes on a two-level categorical dependent variable significantly differs from a hypothesized value.  For example, say we wish to test whether the proportion of "ones" in a column differs significantly from 50%, i.e. from 0.5.\n')
        file_name=input('Please insert here the excel file name: ')
        column=input('Please select the column you want to test: ')
        pr=float(input ('Please insert here the hypothesized proportion including decimals (e.g. 50% would be 0.50): '))
        P_value=float(input('Please insert here your P_value: '))
        tails=input('Please specify the number of tails to use in the analysis (select between 1 or 2): ')
        try:
            result=BinomialTest(file_name,column,pr,P_value,tails)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('Please press enter to kill me!')