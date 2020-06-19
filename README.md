to install the cheque detector model, you need Python 3.7.7 

> git clone https://github.com/gaoyuanliang/cheque_detection.git
>
> cd cheque_detection
>
> pip3 install -r requirements.txt
>
> wget https://github.com/fchollet/deep-learning-models/releases/download/v0.4/xception_weights_tf_dim_ordering_tf_kernels_notop.h5

download the pretrain model of cheque detection from the following url

> https://drive.google.com/file/d/1bvmDMn9h9CULtYp56Ql9UiyGZnMdzxiE/view?usp=sharing

to use the model to tag the image

download the test images by 

> wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg

you can check how the image looks like

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg)

run the test code

> from cheque_detection import cheque_detection
>
> cheque_detection("1200px-Sample_cheque.jpeg")

you will see

> {'tag': 'cheque', 'score': 0.965304}

as a negative example, you can downloand a non-cheque image, say, my  campus photo, by 

> wget https://www.ilwindia.com/wp-content/uploads/2019/08/Heriot-Watt-University-Dubai-1.jpg

which looks like 

![alt text](https://www.ilwindia.com/wp-content/uploads/2019/08/Heriot-Watt-University-Dubai-1.jpg)


and then run the code to do the detection

> cheque_detection("Heriot-Watt-University-Dubai-1.jpg")

and you get the followig result because there is no cheque in the image

>  {}


