import joblib
from my_tokenizer import LemmaTokenizer

logistic = joblib.load('./ML/models/logistic_regression_model.pkl')
vectorizer = joblib.load('./ML/models/tfidf_vectorizer.pkl')
enc = joblib.load('./ML/models/label_encoder.pkl')

tdata = vectorizer.transform(["Fresher with projects in flutter and majorly developed apps for ios"])
actual_pred = logistic.predict(tdata)
predicted_titles = enc.inverse_transform(actual_pred)
print(f"Predicted Job is:{predicted_titles}")