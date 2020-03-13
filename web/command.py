import os
os.chdir("/workspace/Detectron-master")
infer_keypoints = "python tools/infer_video.py \
    --cfg configs/12_2017_baselines/e2e_keypoint_rcnn_R-101-FPN_s1x.yaml \
    --output-dir ../data_io/detectron_out \
    --image-ext mp4 \
	--wts https://dl.fbaipublicfiles.com/detectron/37698009/12_2017_baselines/e2e_keypoint_rcnn_R-101-FPN_s1x.yaml.08_45_57.YkrJgP6O/output/train/keypoints_coco_2014_train:keypoints_coco_2014_valminusminival/generalized_rcnn/model_final.pkl \
    ../data_io/videos"
os.system(infer_keypoints)
os.chdir("/workspace/web")
prepare_data = "python ../VideoPose3D-master/data/prepare_data_2d_custom_copy.py -i ../data_io/detectron_out -o myvideos"
to3d = "python ../VideoPose3D-master/run_copy.py -d custom -k myvideos -arc 3,3,3,3,3 -c checkpoint --evaluate pretrained_h36m_detectron_coco.bin --render --viz-subject upload.mp4 --viz-action custom --viz-camera 0 --viz-video ../data_io/videos/upload.mp4 --viz-export joints3d/upload3d"
os.system(prepare_data)
os.system(to3d)
#os.chdir("/workspace/VideoPose3D_webdemo/")
#clear intermediate files
print("render done")
