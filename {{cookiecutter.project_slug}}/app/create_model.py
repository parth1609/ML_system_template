# import torch
# import torch.nn as nn
# import os

# # Create a simple model for testing
# class SimpleModel(nn.Module):
#     def __init__(self):
#         super(SimpleModel, self).__init__()
#         self.linear = nn.Linear(10, 1)  # Simple linear model
        
#     def forward(self, x):
#         return self.linear(x)

# # Create and save the model
# model = SimpleModel()

# # Create models directory if it doesn't exist
# os.makedirs("app/models", exist_ok=True)

# Save the model
# torch.save(model, "app/models/model.pt")
# print("Model saved to app/models/model.pt")
