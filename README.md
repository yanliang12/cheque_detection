to install the cheque detector model 

> git clone https://github.com/gaoyuanliang/cheque_detection.git
>
> cd cheque_detection
>
> pip3 install -r requirements.txt
>
> wget https://github.com/fchollet/deep-learning-models/releases/download/v0.4/xception_weights_tf_dim_ordering_tf_kernels_notop.h5

download the pretrain model of cheque detection from the following url

> https://drive.google.com/file/d/1WZnNCKzgWVFJ9BCf2DE-V4u2wupoLDWa/view?usp=sharing

to use the model to tag the image

download the test images from 

> https://drive.google.com/file/d/1ybziWKSwoY1Pf6_lDWw7P8EJz4pZj_jB/view?usp=sharing

and 

> https://drive.google.com/file/d/1OKL4Dgwg3gRA8wV3latQPEo7nNwvq1uR/view?usp=sharing

run the test code

> from cheque_detection import cheque_detection
>
> print(cheque_detection("test_sample1.jpg"))
> 
> print(cheque_detection("test_sample2.jpg"))
