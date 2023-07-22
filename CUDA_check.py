import torch

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available!")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU instead.")

# Initialize a random tensor on the selected device
x = torch.randn(3, 3).to(device)
y = torch.matmul(x, x)

# Move the resulting tensor back to the CPU (if necessary)
if device.type == "cuda":
    y = y.to("cpu")

print(y)
torch.cuda.set_device(1)
print(torch.cuda.current_device())