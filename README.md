# Waste-Seggregation

DataSet made manually. Made videos of the objects from different angles and changing the objects position.
Frames were extracted from the videos and the frames were converted to 128 by 128 pixels
csv file was made using the images and the model was trained on those images.


The model would detect images and predict if the image is of biodegradable object or non-biodegradable object.

A red triangle was made on the top of the plate of the dustbin. The model would detect it and would do nothing. The image of the red trinagle was also trained in the model.
When the red triangle was covered with objects, the model would predict if the object is biodegradable or not.

For more accuracy, a QR code can also be used in place of the red triangle.

2objects is a HDF5 file Keras model. It is used in final.py.

Extract the train1.rar to train5.rar files. They contains the images taken for training the model.

Make a folder named 'train' and merge all the photos. 

