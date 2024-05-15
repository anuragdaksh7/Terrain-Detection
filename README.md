# Terrain-Detection

## Feature
classifies the terrain into 4 categories on the basis of their appearence
- Sandy
- Rocky
- Marshy
- Grassy

also it has a seperate web app for testing the model

# model architecture
this model is a ResNet101 model which is fine tuned on the terrain dataset
layers -
- base model
- flatten layer
- dense layer 256 relu
- dense layer 128 relu
- dense layer 64 relu
- dropout layer softmax
- dense layer 4
