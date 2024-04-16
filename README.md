# Code for project in Modeling with Machine Learning for CS
This project aims to automate the process of object removal and scene restoration in a way that is both efficient and visually convincing to human observers. In digital image-editing, removing images and filling in the affected areas to maintain the scene’s visual continuity is a cumbersome task as it is time consuming and requires technical skills.

### to use:

clone to your pc

install segment anything:

```cd segment-anything; pip install -e .```

download model checkpointgit reset --soft HEAD~2 https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth

additionally you need pytorch and torchvision: https://pytorch.org/get-started/locally/

