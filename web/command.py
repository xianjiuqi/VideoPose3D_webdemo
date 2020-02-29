import os
prepare_data = "python ../VideoPose3D/data/prepare_data_2d_custom_copy.py -i ../data_io/detectron_out -o myvideos"
to3d = "python ../VideoPose3D/run_copy.py -d custom -k myvideos -arc 3,3,3,3,3 -c checkpoint --evaluate pretrained_h36m_detectron_coco.bin --render --viz-subject upload --viz-action custom --viz-camera 0 --viz-video ../data_io/videos/upload.mp4 --viz-export joints3d/upload3d"
os.system(prepare_data)
os.system(to3d)
print("render done")
#os.system("mv ")