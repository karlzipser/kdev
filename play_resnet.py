import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import json
import requests

# Load the pretrained ResNet model
model = models.resnet18(pretrained=True)

# Set the model to evaluation mode
model.eval()
from sampleimages import imgs
g=imgs.sunny
g=cv2.resize(g,(224,224))
# Generate a random noise image
a=na([g.transpose(2,0,1)])
b=torch.from_numpy(a).float()
random_noise_image = b#torch.rand(1, 3, 224, 224)

if False:
	# Normalize the image in the same way the model was trained
	normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
	normalized_image = normalize(random_noise_image[0])
normalized_image=random_noise_image[0]/255

# Add a batch dimension
input_image = normalized_image.unsqueeze(0)

# Pass the random noise image through the model
with torch.no_grad():
    output = model(input_image)

# Download ImageNet class labels
LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
response = requests.get(LABELS_URL)
labels = response.json()

# Get the predicted class index
_, predicted_idx = torch.max(output, 1)

# Get the class label
predicted_label = labels[predicted_idx.item()]

# Print the predicted label
print(f"Predicted label: {predicted_label}",predicted_idx)
plot(output[0,:].detach().cpu().numpy())