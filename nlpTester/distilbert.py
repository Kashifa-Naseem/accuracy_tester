import pandas

def predictandsave(model, msg, cat):
    text = [i for i in msg]
    cat = [i for i in cat]
    predic = [model.predict(i) for i in msg]
    result = ['Pass' if cat[i].lower()==predic[i].lower() else 'Fail' for i in range(len(cat))]
    df = pandas.DataFrame()
    df['Text'] = text
    df['Expected_Category'] = cat
    df['Prediction'] = predic
    df['Result'] = result
    cor = df['Result'].value_counts()['Pass']
    acc = cor/len(result)
    print('accuracy: {}'.format(acc))
    return df.to_csv('Predictions.csv')

            
    