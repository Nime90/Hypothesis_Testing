#Correlation
x=0
while x==0:
    try:
        from scipy.stats import pearsonr
        import pandas as pd
        print('A correlation is useful when you want to see the relationship between two (or more) normally distributed interval variables\n')
        file_name=input('Please insert here the excel file name: ')
        col1=input('Please insert the name of the first variable: ')
        col2=input('Please insert the name of the second variable: ')
        P_value=float(input('Please insert here your P_value: '))

        data=pd.read_excel(str(file_name)+'.xlsx')

        corr, p = pearsonr(data[str(col1)], data[str(col2)])
        prop=(corr*corr)*100

        if round(p,4)<round(P_value,4): res='is'
        else: res='IS NOT'

        print('\nThe Pearson correlation score between the two columns is '+str(round(corr,4))+'. Hence "'+str(col1)+'" shares about '+str(round(prop,2))+'%'+' of its variability with "'+str(col2)+'". ')
        print('\nSince the p_value is '+str(round(p,4))+' this correlation '+str(res)+' statistically significant!')
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')