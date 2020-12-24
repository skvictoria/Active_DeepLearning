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


#### https://medium.com/analytics-vidhya/training-an-object-detection-model-with-tensorflow-api-using-google-colab-4f9a688d5e8b <- very useful!
