########
from pavi import *

model = load_build_image_categorization_model(
	model_file = 'cheque.h5py')

def cheque_detection(input_file)
	output = {}
	img = image.load_img(input_fileinput_file, target_size=(224, 224))
	x = image.img_to_array(img)
	x = xception.preprocess_input(x)
	x = numpy.array([x])
	x = base_model_Xception.predict(x)
	y_score = model.predict(x)
	prediction = numpy.argmax(y_score)
	score = numpy.max(y_score)
	if prediction > 0:
		output["tag"] = 'cheque'
		output["score"] = score
	return output

########
