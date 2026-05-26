from fastapi import FastAPI
import joblib
import pandas as pd
from api.schemas import SalesInput 
from pathlib import Path

app = FastAPI()

# Load the trained model
BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "models" / "xgboost_sales_forecast.pkl"
model = joblib.load(model_path)

@app.post('/predict')
def predict_sales(data: SalesInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)

    return {
        "predicted_sales": float(prediction[0])
    }
