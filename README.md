<h1>Monkey Breed Prediction Website</h1>


<p align="center">
<a href="#about-memo">About</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
<a href="#tecnologies-rocket">Technologies</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
<a href="#how-to-contribute-">How to Contribute</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
<a href="#license-scroll">License</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
</p>


## Note :memo:

2 Files has not been uploaded on GitHub Due to their large size.These Files Are =>
- Model(https://drive.google.com/file/d/1CpwUtzJjgV2r8MTK4AgaGx_XuR8Cjhpi/view?usp=sharing);
- Tensorflow Dependency(https://drive.google.com/file/d/1WnBBtb6vtaycBADmEU9ppx2vKYiyK0w7/view?usp=sharing);

## Instruction :pen:

- Create 'models' folder inside 'monkey' and paste the model there;
- Paste the TF Dependency in \Monkey\Lib\site-packages\tensorflow\python.

## About :memo:

This Project is a website to predict monkey breeds.There are a total of 10 breeds of monkeys.<br/>
 The Dataset has been taken from Kaggle.<br/>
 The size of the images was around 400x300 pixels and had around 1400 images.<br/>
Link = https://www.kaggle.com/slothkong/10-monkey-species<br/>
The predictions has been made using concepts of Deep Learning.<br/>
I have made use of Tensorflow Library.<br/>
Transfer Learning has proven to be a strong tool for classification purposes.Sophisticated deep learning models have millions of parameters (weights) and training them from scratch often requires large amounts of data of computing resources. Transfer learning is a technique that shortcuts much of this by taking a piece of a model that has already been trained on a related task and reusing it in a new model.<br/>
I have made use of Xception Model.<br/>
Xception by Google, stands for Extreme version of Inception, is reviewed. With a modified depthwise separable convolution, it is even better than Inception-v3 for both ImageNet ILSVRC and JFT datasets.<br/>
I have not trained the layers again apart from input and output layers.<br/>
The Output of Xception model has been furthur passed through a Flatten , Dense , Dropout and Dense Layer to remove Overfitting.<br/>
Apart from this to deal with Overfitting , I have preprocessed the images like rotation , width shift , height shift and horizontal flip.<br/>
The model was trained for 100 epochs and was able to achieve 91.62% train accuracy and 91.91% train accuracy.<br/>
The model was then saved and downloaded.<br/>

## Apresentation of Project :sparkles:

<p align="center"> HOME PAGE
<image src="https://github.com/faiz-hasan11/MonkeyBreedPredictionWebsite/blob/master/HomePage.png" />
</p><br>
<p align="center"> PREDICTION PAGE
<image src="https://github.com/faiz-hasan11/MonkeyBreedPredictionWebsite/blob/master/PredictionPage.png" />
</p>


---

## Technologies :rocket:

- <a href="https://www.djangoproject.com/">Django</a>
- <a href="https://www.tensorflow.org/">Tensorflow</a>

## How to Run 🤔
After cloning or downloading this github repo on the local system. 
Create a Virual Environment on the Desktop.
```bash
virtualenv VirtualEnvironmentName
```
Now copy the repository inside your virtual environment.
Activate the virtual environment.
```bash
~/desktop/VirtualEnvironmentName/Scripts/activate
```
Move inside the virtual environment.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.
```bash
pip install -r requirements.txt
```

Change directory to HeartDiseasePrediction.
Run the following command
```bash
python manage.py runserver
```
An IP address will be shown, copy it and run it on a web browser.

## License :scroll:

> This project is under the MIT license. See the archive [LICENSE](LICENSE) for more details.

---

##### Made by 'Your name'(nickname) :wave:
