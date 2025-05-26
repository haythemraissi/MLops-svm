import joblib

def predict(example, model_path='models/svm_model.pkl', scaler_path='models/scaler.pkl'):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    scaled_example = scaler.transform([example])
    return model.predict(scaled_example)
