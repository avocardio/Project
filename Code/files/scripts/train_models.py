# train pipelines

# imports
import argparse

from resnet50 import ResNet50
from preprocessing import preprocessing

# setting up CLI
parser = argparse.ArgumentParser(description = "Training models")
parser.add_argument("-r", "--resnet", action = "store_true", help = "starts training for resnet")
parser.add_argument("-c", "--convnext", action = "store_true", help = "starts training for convnext")
parser.add_argument("-p", "--preprocessed", action = "store_true", help = "uses preprocessed data")

MODEL_FRAGMENTS = '../../../Data/Models/'

args = parser.parse_args()

if args.resnet and args.preprocessed:
    train_data, _, valid_data = preprocessing()
    print("\nStarting training for ResNet50:")
    model = ResNet50(num_classes=400)
    model.build(input_shape=(None, 224, 224, 3))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_data, epochs=10, validation_data=valid_data)
    model.save(MODEL_FRAGMENTS + 'resnet50')
    
if args.convnext:
    print("training function for convnext")
