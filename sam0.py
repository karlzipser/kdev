#, a
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
sam = sam_model_registry["default"](checkpoint='/home/karl/Desktop/sam_vit_h_4b8939.pth')
sam.to('cuda:0')
mask_generator = SamAutomaticMaskGenerator(sam)
#,b
n=1
#, a
from sampleimages import imgs
img=imgs.sunny
img=rimread(opjD('street.jpg'));img=cv2.resize(img,(512,512))
masks = mask_generator.generate(img)
#, b
#, a

if True:
	results=[]
	for a in masks:
	    b=a['segmentation']
	    results.append(maskit(img,b.astype(u8)))
	figure(n,figsize=(18,18))
	sh(results,n);n+=1
#, b
#, a
allmasks=zeros((512,512))
for a in masks:
	allmasks+=a['segmentation'].astype(int)
allmasks[allmasks>0]=1
allmasks=allmasks.astype(u8)
nomasks=1-allmasks
figure(n,figsize=(18,18))
sh(maskit(img,allmasks),n);n+=1

#,b