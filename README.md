# Deep_learning (Transfer learning)
Testing custom dataset with pre-trained ssd_mobilenetv1

# Pre-requisites
Follow installation instruction of tensorflow: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md

Clone this repository into /models/research/objection_detection/

# Directory Structure
This repository contains:
  1. Label-Image:  To extract, Annotate and convert into tfrecord fileformat.
  2. models: Contains trained checkpoints, evaluated checkpoints, input configuration file, and frozen graph of trained model.
  3. data: Contains all records file and sbs_label_map file.
  4. results: Contains evaluated images.
  5. Commands_for_evalTrain:  This file contains terminal commands to put model on training, evaluation and visualizing it on tensorboard. (Note: Chnage path according to your username)
  
 # Implementation
 Use terminal commands given in commands_for_evalTrain file to train, evaluate or visualize trained model on tensorboard
 Provide path to input configuration file(ssd_mobilenet_v1_coco.config) as in your local pc
  

