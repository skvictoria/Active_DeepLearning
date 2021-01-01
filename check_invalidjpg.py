import tensorflow as tf
import glob, os.path

for i, image_name in enumerate(glob.glob(os.path.join('/home/john/DLstorage/repos/models/research/object_detection/images/val','*.jpg'))):
  print(i, image_name)
  with tf.Graph().as_default():
    image_contents = tf.read_file(image_name)
    image = tf.image.decode_jpeg(image_contents, channels = 3)
    
    with tf.Session() as sess:
      sess.run(tf.global_variables_initalizer())
      tmp = sess.run(image)
