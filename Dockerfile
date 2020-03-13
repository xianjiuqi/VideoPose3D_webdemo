FROM pytorch/pytorch:nightly-devel-cuda9.2-cudnn7
RUN apt-get update && apt-get install -y \
        libgtk2.0-dev \
        wget \
        ffmpeg \
        vim
 
COPY . .       
RUN pip install -r requirements.txt


# WORKDIR /workspace/Detectron-master/checkpoint
# RUN wget https://dl.fbaipublicfiles.com/video-pose-3d/pretrained_h36m_detectron_coco.bin

WORKDIR /workspace/Detectron-master
RUN make

WORKDIR /workspace/cocoapi-master/PythonAPI
RUN make install

WORKDIR /workspace

