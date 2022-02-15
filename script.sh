#!/bin/bash

CUDA_VISIBLE_DEVICES=1  python train_mvs_nerf_pl.py \
       	--expname firstrun-dtu \
	--num_epochs 2 --use_viewdirs \
	---dataset_name dtu \
       	--datadir data/mvs_training/dtu
