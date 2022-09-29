import torch
import torchvision
from .add_gcn import ADD_GCN
from .tdrg import TDRG
model_dict = {'ADD_GCN': ADD_GCN, 'TDRG': TDRG}

def get_model(num_classes, args):
    if args.model_name in ('ADD_GCN'):
        res101 = torchvision.models.resnet101(pretrained=True)
        model = model_dict[args.model_name](res101, num_classes)
        return model

    elif args.model_name == 'TDRG':
        res101 = torchvision.models.resnet101(pretrained=True)
        model = model_dict[args.model_name](res101, num_classes)
        return model