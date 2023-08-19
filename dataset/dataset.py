import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os


class UNet_dataset(Dataset):
    def __init__(self, image_dir, mask_dir, transforms= None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transfroms = transforms

    
    def __getitem__(self, index):
        image = Image.open(os.path.join(self.image_dir))
        