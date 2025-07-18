# The ultimate guide on installing PyTorch with CUDA support in all possible ways

Source: https://medium.com/decodingml/the-step-by-step-guide-on-how-to-install-pytorch-with-cuda-support-in-all-possible-ways-147b3f34085c

1. Init poetry:  
```bash
poetry init
```

2. Add PyPi as the main repository: 
```bash
poetry source add PyPi
```
3. Then, we add `https://download.pytorch.org/whl/cu118` as an optional repository under the name of “torch” (it can have any other name):

```bash
poetry source add --priority=supplemental torch https://download.pytorch.org/whl/cu126
```

4. Install torch with CUDA support from the “torch” repository:  
```bash
poetry add torch==2.6.0+cu126 --source torch
```