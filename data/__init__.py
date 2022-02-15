from .llff import LLFFDataset
from .blender import BlenderDataset
from .dtu_ft import DTU_ft
from .dtu import MVSDatasetDTU
from .dtu_src import MVSDatasetDTU_src

dataset_dict = {'dtu': MVSDatasetDTU,
                'dtu_src':MVSDatasetDTU_src,
                'llff':LLFFDataset,
                'blender': BlenderDataset,
                'dtu_ft': DTU_ft}