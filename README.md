README

This is a simple machine learning example using SVM (Support Vector Machine) for spam detector.

Performance: overall accuracy ~98%

* Requirement
    * python3
    * packages: pandas, scikit-learn(sklearn)

* Setup
```
pip3 install -r requirements.txt
```

* Usage
```
python3 spamDetector.py
```
 
* Train a model to detect spam for a training data file
```
python3 trainModel.py <train-data> <model-vec> <model-dat>
```

* Test the specified model
```
python3 testModel.py <model-vec> <model-dat>
```

* Reference:
    * https://blog.logrocket.com/email-spam-detector-python-machine-learning/
