import sys
print(sys.executable)
import torch
import numpy as np


def main():
  pytorch_model  = torch.hub.load('pytorch/vision:v0.6.0', 'squeezenet1_0', pretrained=True)
  pytorch_model.load_state_dict(torch.load('./models/squeeznet.ckpt'))
  print('Sucessfully loaded data')
  print(pytorch_model)

  pytorch_model.eval()
  #[batchsize,channels,h,w]
  dummy_input = np.zeros([32,3,224,224])
  tensor = torch.from_numpy(dummy_input)
  print('Exporting Model')
  torch.onnx.export(pytorch_model.double(), tensor, 'onnx_model.onnx', verbose=True)


if __name__ == '__main__':
  main()
