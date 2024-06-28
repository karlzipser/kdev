import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import json
import requests

#model = models.resnet18(pretrained=True)
#torchvision.models.vit_b_16(weights=torchvision.models.ViT_B_16_Weights)
model = torchvision.models.vit_b_16(weights=torchvision.models.ViT_B_16_Weights)#models.models.vit_b_16(pretrained=True)
model.eval()
from sampleimages import imgs
g=imgs.mtum
g=cv2.resize(g,(224,224))
a=na([g.transpose(2,0,1)])
b=torch.from_numpy(a).float()
random_noise_image = b#torch.rand(1, 3, 224, 224)

if False:
	# Normalize the image in the same way the model was trained
	normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
	normalized_image = normalize(random_noise_image[0])
normalized_image=random_noise_image[0]/255

input_image = normalized_image.unsqueeze(0)

with torch.no_grad():
    output = model(input_image)

LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"

response = requests.get(LABELS_URL)
labels = response.json()
so(opjD('imagenetlabels'),labels)

_, predicted_idx = torch.max(output, 1)

predicted_label = labels[predicted_idx.item()]

print(f"Predicted label: {predicted_label}",predicted_idx)
#plot(output[0,:].detach().cpu().numpy())

probabilities = torch.nn.functional.softmax(output[0], dim=0)
confidence, predicted_idx = torch.max(probabilities, 0)
predicted_label = labels[predicted_idx.item()]

print(predicted_label, confidence.item())
clf()
plot(probabilities.detach().cpu().numpy())
