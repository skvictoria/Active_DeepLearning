import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#Loading the saved_model(change the path according to your directory names)
import tensorflow as tf
import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils


PATH_TO_SAVED_MODEL="/content/drive/MyDrive/models/research/object_detection/test_directory/saved_model"
print('Loading model...', end='')# Load saved model and build the detection function
detect_fn=tf.saved_model.load(PATH_TO_SAVED_MODEL)

print('Done!')

#Loading the label_map
category_index=label_map_util.create_category_index_from_labelmap("/content/drive/MyDrive/models/research/object_detection/data/mscoco_label_map.pbtxt",use_display_name=True)

#category_index=label_map_util.create_category_index_from_labelmap([path_to_label_map],use_display_name=True)

#Loading the image
img=['/content/drive/MyDrive/models/research/object_detection/test_images/20200302_143518.JPG']
print(img)#list containing paths of all the images

def load_image_into_numpy_array(path):
    return np.array(Image.open(path))

for image_path in img:
  print('Running inference for {}... '.format(image_path), end='')
image_np=load_image_into_numpy_array(image_path)
input_tensor=tf.convert_to_tensor(image_np)
input_tensor=input_tensor[tf.newaxis, ...]
detections=detect_fn(input_tensor)
num_detections=int(detections.pop('num_detections'))
detections={key:value[0,:num_detections].numpy()
                for key,value in detections.items()}
detections['num_detections']=num_detections
detections['detection_classes']= detections['detection_classes'].astype(np.int64)
image_np_with_detections=image_np.copy()
viz_utils.visualize_boxes_and_labels_on_image_array(
      image_np_with_detections,
      detections['detection_boxes'],
      detections['detection_classes'],
      detections['detection_scores'],
      category_index,
      use_normalized_coordinates=True,
      max_boxes_to_draw=100,     
      min_score_thresh=.5,      
      agnostic_mode=False)

%matplotlib inline
plt.figure()
plt.imshow(image_np_with_detections)
print('Done')
plt.show()
