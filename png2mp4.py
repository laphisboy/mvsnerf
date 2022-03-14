import imageio
import os
import glob
import argparse
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    ## single scene and view_type only
    # parser.add_argument('--scene', type=str,
    #                     choices=['ship','mic','chair','lego','drums','ficus','materials','hotdog'])

    # parser.add_argument('--view_type', type=str,
    #                     choices=['nearest','dense','sparse','random','far','fixed-nearest','fixed-sparse'])             

    # parser.add_argument('--ckpt', type=str)

    # parser.add_argument('--num_src_views', type=int)



    ## can process multiple scene, viewtype, ckpts
    parser.add_argument('--scenes', nargs='+', default=[])

    parser.add_argument('--view_types', nargs='+', default=[])           

    parser.add_argument('--ckpts', nargs='+', default=[])

    parser.add_argument('--source', type=str, default='train')

    parser.add_argument('--target', type=str, default='test')

    parser.add_argument('--is_gif', type=bool, default=False)

    args = parser.parse_args()

    # ckpt = args.ckpt
    # num_src_views = args.num_src_views
    source = args.source
    target = args.target
    # view_type = args.view_type

    # scene = args.scene


    for ckpt in args.ckpts:
        
        num_src_views = re.findall('[0-9]+', ckpt)[0]

        for view_type in args.view_types:

            for scene in args.scenes:

                base_path = f'/mnt/hdd/youngsun/mvsnerf_timing/results/{ckpt[:-4]}/blender-{num_src_views}-{view_type}-{source}-{target}'
                scene_path = os.path.join(base_path, scene) + '*.png'

                file_list = glob.glob(scene_path)
                file_list.sort()

                save_path = f'/mnt/hdd/youngsun/mvsnerf_timing/results_video/{ckpt[:-4]}/blender-{num_src_views}-{view_type}-{source}-{target}/'
                os.makedirs(save_path, exist_ok=True)
                
                if args.is_gif:
                    save_video_path = os.path.join(save_path, scene) + '.gif'

                    images = []

                    for file_path in file_list:
                        images.append(imageio.imread(file_path))
                    
                    imageio.mimsave(save_video_path, images)

                else:
                    save_video_path = os.path.join(save_path, scene) + '.mp4'

                    writer = imageio.get_writer(save_video_path, fps=15)

                    for im in file_list:
                        writer.append_data(imageio.imread(im))
                    writer.close()