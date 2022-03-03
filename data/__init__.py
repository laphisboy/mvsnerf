from .llff import LLFFDataset
from .blender import BlenderDataset
from .dtu_ft import DTU_ft
from .dtu import MVSDatasetDTU
from .dtu_src import MVSDatasetDTU_src
from .blender_src import BlenderDataset_src

dataset_dict = {'dtu': MVSDatasetDTU,
                'dtu_src':MVSDatasetDTU_src,
                'llff':LLFFDataset,
                'blender': BlenderDataset,
                'blender_src':BlenderDataset_src,
                'dtu_ft': DTU_ft}