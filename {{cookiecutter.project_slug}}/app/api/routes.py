from fastapi import APIRouter, HTTPException
from ..services.inference import ModelService
from typing import List

router = APIRouter()
# Using a JSON config file instead of PyTorch model
model_service = ModelService("app/models/model_config.json")

@router.post("/predict")
async def predict(data: List[float]):
    """
    Make a prediction using the model service.
    
    Args:
        data: List of numerical values for prediction
        
    Returns:
        dict: Prediction result with model info
    """
    try:
        result = model_service.predict(data)
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
