# Active_DeepLearning

## Azure Blob Storage
## VOTT labeling tool


## tensorflow/models/research 
- research 폴더에서

  > protoc object_detection/protos/*.proto --python_out=.
  
  > export PYTHONPATH=$PYTHONPATH:pwd:pwd/slim
  
  > export PYTHONPATH=$PYTHONPATH:/path/to/models
  
  > python setup.py build
  
  > python setup.py install
  
- research/object_detection/builders 경로에서

  > python model_builder_test.py

## tensorflow/models/research/object_detection
- in object_detection folder

## tensorflow/models/research/object_detection
> PIPELINE_CONFIG_PATH=/home/john/project/repos/models/research/object_detection/samples/configs/faster_rcnn_resnet50_coco.config

> MODEL_DIR=/dhome/john/DLstorage/result

> NUM_TRAIN_STEPS=10000000

> python object_detection/model_main.py --pipeline_config_path=${PIPELINE_CONFIG_PATH} --model_dir=${MODEL_DIR} --num_train_steps=${NUM_TRAIN_STEPS} --alsologtostderr

> python legacy/train.py --pipeline_config_path=/home/john/project/repos/models/research/object_detection/samples/configs/faster_rcnn_resnet101_coco.config --train_dir=/home/john/DLstorage/result --logtostderr --worker_replicas=1 --num_clones=1 --ps_tasks=1

(example)
  > python generate_tfrecord.py --big_csv_input=/home/john/project/repos/models/research/object_detection/images/csvlowbiglabeling/train_bigger.csv --low_csv_input=/home/john/project/repos/models/research/object_detection/images/csvlowbiglabeling/train_lower.csv --image_dir=/home/john/project/repos/models/research/object_detection/images/train --output_path=/home/john/project/repos/models/research/object_detection/train.record

#### https://medium.com/analytics-vidhya/training-an-object-detection-model-with-tensorflow-api-using-google-colab-4f9a688d5e8b <- very useful!

#### https://medium.com/@shubham.borikar/train-tensorflow-object-detection-api-on-custom-dataset-839ebb93dddc <- very useful!

