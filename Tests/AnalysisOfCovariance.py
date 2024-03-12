#analysisofCovariance
x=0
while x==0:
    try:
        from pingouin import ancova
        import pandas as pd, warnings
        warnings.simplefilter("ignore")
        print('\nAnalysis of covariance is like ANOVA, except in addition to the categorical predictors you also have continuous predictors as well.\n')
        file_name=input('Please insert here the excel file name: ')
        dep_var=input('Please insert the name of the continuous dependent variable: ')
        cont_var=input('Please insert the name of the continuous independent variable: ')
        cat_var= input('Please insert the name of the categorical independent variable: ')
        data=pd.read_excel(str(file_name)+'.xlsx')
        res=ancova(data=data, dv=str(dep_var), covar=str(cont_var), between=str(cat_var))
        print('')
        print(res)

        print('\np_value for "'+str(res.Source[0])+'" is: '+str(round(res['p-unc'][0],4))+'. While p_value for "'+str(res.Source[1])+'" is: '+str(round(res['p-unc'][1],4)))

        print('\nThe results indicate that after adjusting for "'+str(cont_var)+'", the column "'+str(dep_var)+'" significantly differ by the different values of "'+str(cat_var)+'".')
        x=1
    except Exception as e: 
        print(e)
        x=0
    input('\nPlease press Enter to kill me!')