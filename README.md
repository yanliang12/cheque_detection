# tagging the images of bank cheque

Tagging the images which have the bank cheque 


<table>
  <thead>
    <tr>
      <th>Input</th>
      <th>Output</th>
    </tr>
  </thead>
  <tr>
    <td>
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg" height="300">
    </td>
    <td>
      <pre>
{
  'score': 0.7404399, 
  'tag': 'cheque'
}
</pre>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://www.ilwindia.com/wp-content/uploads/2019/08/Heriot-Watt-University-Dubai-1.jpg" height="300">
    </td>
    <td>
      <pre>
{
  'score': 1.0, 
  'tag': 'non_cheque'
}
</pre>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://m.media-amazon.com/images/G/01/AGS/SEA/SIV_3_Resized._SL1280_FMjpg_CB1541994278_.jpg" height="300">
    </td>
    <td>
      <pre>
{
  'score': 0.92342573, 
  'tag': 'non_cheque'
}
</pre>
    </td>
  </tr>
</table>


### Installation

to install the cheque detector model, you need Python 3.7.7 

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

to use the model to tag the image, download the test images by 

```bash
wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg
```

you can check how the image looks like

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg)

run the test code

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

![alt text](https://www.ilwindia.com/wp-content/uploads/2019/08/Heriot-Watt-University-Dubai-1.jpg)


and then run the code to do the detection

```python
cheque_tagging("Heriot-Watt-University-Dubai-1.jpg")
```

and you get the followig result because there is no cheque in the image

```python
{'score': 1.0, 'tag': 'non_cheque'}
```


