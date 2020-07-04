# tagging the images of cheque

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
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg" width="420">
    </td>
    <td>
      <pre>
{
'tag': 'cheque', 
'score': 0.965304
}</pre>
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
from cheque_detection import cheque_detection

cheque_detection("1200px-Sample_cheque.jpeg")
```

you will see

```python
{'tag': 'cheque', 'score': 0.965304}
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
cheque_detection("Heriot-Watt-University-Dubai-1.jpg")
```

and you get the followig result because there is no cheque in the image

```python
{}
```


