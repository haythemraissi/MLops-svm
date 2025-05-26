from sklearn.svm import SVC
import joblib

def train_model(X_train, y_train):
    model = SVC(random_state=101)
    model.fit(X_train, y_train)
    return model

def save_model(model, scaler, model_path='models/svm_model.pkl', scaler_path='models/scaler.pkl'):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
