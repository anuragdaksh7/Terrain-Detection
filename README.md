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

# installation
you can download pre trained model from "here" //link to be added later
```bash
git clone https://github.com/anuragdaksh7/Terrain-Detection.git
cd Terrain-Detection
cd frontend
npm install
pip install -r requirements.txt
flask run
```