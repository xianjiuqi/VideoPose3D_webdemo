# VideoPose3D_webdemo
Pose estimation is an increasingly popular topic in deep learning literature. The [VideoPose3D](https://github.com/facebookresearch/VideoPose3D) project by Facebook Research tackles the problem of infering human joint positions in 3D space from a 2D video. 

## Problem statement
The challenges with setting up computational environment prohibits general populations to experience the latest technology developed in human pose estimation task. The VideoPose3D project achieved amazing results, but not everyone can interact with it. Thus, we built a website that allows a user to upload a short video with one person in it and get back a 3D skeleton rendering with the same pose as the person in the video. The user can rotate the rendered skeleton and view it from different angles.

Process Flow:
video -> 2D joint positions -> 3D joint positions -> web rendering

Our website serves two purpose:
1. Give quick access to users who wish to qualitatively evaluate the model.
2. Build a pipline that is compatible with many existing and future models in terms of input and output, so that the website can be reused to demonstrate new, state-of-art models.

## Deliverables
- a demo website for VideoPose3D by Facebook Research
- a Docker image
- a Dockerfile

## Set Up
1. Your system must have a GPU and have nvidia-docker installed
2. Run `docker pull ` TODO
3. Run `nvidia-docker run -it -d -p 80:80 --name web4 videopose3d_webdemo:v3`
Now the website is served. In your browser enter `your-server-ip:80`

Here is a demo [video] for the rendered skeleton. 
