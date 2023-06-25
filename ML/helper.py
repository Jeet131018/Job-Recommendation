import joblib
from my_tokenizer import LemmaTokenizer
import numpy as np

logistic = joblib.load('./ML/models/logistic_regression_model.pkl')
vectorizer = joblib.load('./ML/models/tfidf_vectorizer.pkl')
enc = joblib.load('./ML/models/label_encoder.pkl')

def getRecommend(des):
    tdata = vectorizer.transform([des])
    actual_pred = logistic.predict(tdata)
    predicted_titles = enc.inverse_transform(actual_pred)
    tpred = logistic.predict_proba(tdata)
    alt1=""
    alt2=""
    for i in tpred:
        class_preds = np.argsort(i)
        #print(class_preds)
        for i in [-1, -2]:
            if class_preds[i] == actual_pred:
                class_preds=np.delete(class_preds,i)
        top_classes = class_preds[-2:]
            
        #print(f"top class={top_classes}")
        class_names = enc.inverse_transform(top_classes)
        alt1=class_names[0]
        alt2=class_names[1]
        return [predicted_titles[0],alt1,alt2]
    
    
    
des = "Fresher with projects in flutter and majorly developed apps for ios"
jobs=getRecommend(des)
print(jobs)
