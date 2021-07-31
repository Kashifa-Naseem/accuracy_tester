import pandas

def predictandsave(model, msg):
    predic = []
    text = []
    for i in msg:
        text.append(i)
        prediction = model.predict(i)
        predic.append(prediction)
    
    df = pandas.DataFrame()
    df['Text'] = text
    df['Prediction'] = predic

    return df.to_csv('Predictions.csv')

            
    