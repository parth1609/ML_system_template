# import torch

# class ModelService:
#     def __init__(self, model_path: str):
#         self.model = torch.load(model_path, map_location="cpu")
#         self.model.eval()

#     def predict(self, inputs):
#         with torch.no_grad():
#             return self.model(inputs).tolist()
