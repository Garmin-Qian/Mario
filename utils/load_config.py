import torch

if torch.cuda.is_available():
    # cache_dir = "/mnt/data/yule/.cache"
    cache_dir = "/home/qjm/.cache/huggingface/hub"
else:
    # cache_dir = "/Users/yule/.cache"
    cache_dir = "/home/qjm/.cache/huggingface/hub"
