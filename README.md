# Code for project in Modeling with Machine Learning for CS
This project aims to automate the process of object removal and scene restoration in a way that is both efficient and visually convincing to human observers. In digital image-editing, removing images and filling in the affected areas to maintain the scene’s visual continuity is a cumbersome task as it is time consuming and requires technical skills.

### to use:

clone to your pc:
```git clone https://github.com/facebookresearch/segment-anything.git```

install segment anything:

```cd segment-anything; pip install -e .```

download model checkpoint https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth and move it into the top-level directory

additionally you need pytorch, torchvision and opencv: https://pytorch.org/get-started/locally/

```pip3 install torch torchvision torchaudio opencv-python```


### GAN-based generative inpainting
Install packages:
```pip3 install pyyaml tf_slim```

Follow the procedure specified in to downlod the required packages: 
```https://github.com/JiahuiYu/generative_inpainting```

Clone the repo:
```git clone https://github.com/JiahuiYu/generative_inpainting.git```

Download the pretrained Places2 model from:
https://drive.google.com/drive/folders/1y7Irxm3HSHGvp546hZdAZwuNmhLUVcjO?usp=sharing
and put it into the ```generative_inpainting/model_logs``` directory. Rename ```checkpoint.txt``` to ```checkpoint```

Clone the neuralgym package:
```git clone https://github.com/JiahuiYu/neuralgym.git```

Then from the terminal run: 
```cd neuralgym; pip install -e .```

