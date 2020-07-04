########cheque_tagging.py########
from jessica_cv import *

model = load_build_image_categorization_model(
	model_file = 'cheque.h5py')

def cheque_tagging(input_file):
	output = {}
	img = image.load_img(input_file, target_size=(224, 224))
	x = image.img_to_array(img)
	x = xception.preprocess_input(x)
	x = numpy.array([x])
	x = base_model_Xception.predict(x)
	y_score = model.predict(x)
	prediction = numpy.argmax(y_score)
	score = numpy.max(y_score)
	if prediction > 0:
		output["tag"] = 'cheque'
	else:
		output["tag"] = 'non_cheque'
	output["score"] = score
	return output

'''
wget https://m.media-amazon.com/images/G/01/AGS/SEA/SIV_3_Resized._SL1280_FMjpg_CB1541994278_.jpg


cheque_tagging("SIV_3_Resized._SL1280_FMjpg_CB1541994278_.jpg")

{'score': 0.92342573, 'tag': 'non_cheque'}

'''


'''
wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sample_cheque.jpeg/1200px-Sample_cheque.jpeg


cheque_tagging("1200px-Sample_cheque.jpeg")

{'score': 0.7404399, 'tag': 'cheque'}

'''

########cheque_tagging.py########
