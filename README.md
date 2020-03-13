# VideoPose3D_webdemo
Pose estimation is an increasingly popular topic in deep learning literature. The [VideoPose3D](https://github.com/facebookresearch/VideoPose3D) project by Facebook Research tackles the problem of infering human joint positions in 3D space from a 2D video. 

## Problem statement
The challenges with setting up computational environment prohibits general public to experience the latest technology developed in human pose estimation task. The VideoPose3D project achieved amazing results, but not everyone can interact with it. Thus, we built a website that allows a user to upload a short video with one person in it and get back a 3D skeleton rendering with the same pose as the person in the video. The user can rotate the rendered skeleton and view it from different angles.

#### Input & Output
video -> 2D joint positions -> 3D joint positions -> web rendering

Our website serves two purpose:
1. Give quick access to users who wish to qualitatively evaluate the model.
2. Build a pipeline that is compatible with many existing and future models in terms of input and output, so that the website can be reused to demonstrate new, state-of-art models.

## Deliverables
- a demo website for VideoPose3D by Facebook Research
- a Docker image
- a Dockerfile

## Set Up
1. Your system must have a GPU and have nvidia-docker installed
2. Run 
```
docker pull xianjiuqi/videopose3d_webdemo:v3-publish
``` 
3. Run 
```
nvidia-docker run -it --rm -p 80:80 --name pose3d xianjiuqi/videopose3d_webdemo:v3-publish
```
Now the website is served. In your browser enter `your-server-ip:80`.

4. Upload your video. (see below)

For the video to be uploaded, our website currently support:
1. `.mp4` format.
2. short and low resolution video (<10s and <3Mb ). This is not a hard requirement. But videos we tested at this size requires less than 2 minutes to process.
3. Demo videos that can be downloaded at [Google Drive](https://drive.google.com/drive/folders/1oie0jcFnaiaXKqHLPQoy1-hBgSO5lunG)

Here is a [video](https://youtu.be/ei55prz3Vyg) for the rendered skeleton of 'Golf.mp4', one of the demo videos above.

## Known Issues/Under Development
- When multiple users upload their video at the same time, rendering will fail for all of them. A queueing mechanism is under development.
- If you refresh the page after clicking 'upload' the rendering may not show.

## Reference
```
 @inproceedings{pavllo:videopose3d:2019,
  title={3D human pose estimation in video with temporal convolutions and semi-supervised training},
  author={Pavllo, Dario and Feichtenhofer, Christoph and Grangier, David and Auli, Michael},
  booktitle={Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2019}
}
```

## Links
[VideoPose3D](https://github.com/facebookresearch/VideoPose3D)
