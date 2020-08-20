# tagging the images of bank cheque

Tagging the images which have the bank cheque. The output has a tag of cheque or non-cheque, and a confidence score between 0 and 1.

<table>
  <thead>
    <tr>
      <th>Input</th>
      <th>Output</th>
    </tr>
  </thead>
  <tr>
    <td>
      <img src="https://github.com/gaoyuanliang/cheque_detection/raw/master/WeChat%20Screenshot_20200820081723.png" width="400">
    </td>
    <td>
      <pre>
{
  'tag': 'cheque', 
  'score': 0.7404399
}
</pre>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/gaoyuanliang/cheque_detection/raw/master/WeChat%20Screenshot_20200820081825.png" width="400">
    </td>
    <td>
      <pre>
{
  'tag': 'non_cheque', 
  'score': 0.7928494
}
</pre>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/gaoyuanliang/cheque_detection/raw/master/WeChat%20Screenshot_20200820082216.png" width="400">
    </td>
    <td>
      <pre>
{
  'tag': 'non_cheque', 
  'score': 1.0
}
</pre>
    </td>
  </tr>
</table>


### Installation

to install the cheque tagger model, you need Python 3.7.7. Then you can download the code and pre-trained models as follows

```bash
git clone https://github.com/gaoyuanliang/cheque_detection.git

cd cheque_detection

pip3 install -r requirements.txt

wget https://github.com/fchollet/deep-learning-models/releases/download/v0.4/xception_weights_tf_dim_ordering_tf_kernels_notop.h5
```

download the pretrain model of cheque detection from the following url

```bash
https://drive.google.com/file/d/1bvmDMn9h9CULtYp56Ql9UiyGZnMdzxiE/view?usp=sharing
```

### Using

**Test with a positive case**

to use the model to tag the image, download the an image of cheque by 

```bash
wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg
```

you can check how the image looks like

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg" height="200">

then run the test code

```python
from  cheque_tagging import cheque_tagging

cheque_tagging("1200px-Sample_cheque.jpeg")
```

you will see

```python
{'score': 0.7404399, 'tag': 'cheque'}
```

**Test with a negative case**

as a negative example, you can downloand a non-cheque image, say, my lovely campus photo, by 

```bash
wget https://www.ilwindia.com/wp-content/uploads/2019/08/Heriot-Watt-University-Dubai-1.jpg
```

which looks like 

<img src="https://www.ilwindia.com/wp-content/uploads/2019/08/Heriot-Watt-University-Dubai-1.jpg" height="200">

and then run the code to do the tagging

```python
cheque_tagging("Heriot-Watt-University-Dubai-1.jpg")
```

and you get the followig result because there is no cheque in the image

```python
{'score': 1.0, 'tag': 'non_cheque'}
```

### Training of the model

I trained this model from a data set of 536 cheque images and 38996 non-cheque images. This data set is collected by myself. The training is conducted over a GPU of Ali Cloud. The epoch number is 20, and the accuracy over the training set is 0.9984.

If you need access to my training data set, or want to know more about the training details, please contact me by gaoyuanliang@outlook.com 

I am actively looking for data science/AI related job. If you have such oppertunity, thank you so much for contact me. I am ready for interview any time.
