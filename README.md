# Colon Cancer Prediction App

This is a web application that uses a machine learning model to predict the likelihood of a patient having cancer based on gene expression data. The model was trained on a dataset of gene expression data from cancer patients, and uses a Random Forest algorithm to make predictions. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Flask
- Pickle
- Numpy

### Installing

1. Clone the repository
```
git clone https://github.com/khalednassar500/cancer-prediction-app.git
```
2. Navigate to the project directory
```
cd cancer-prediction-app
```

3. Run the app
```
python3 app.py
```
4. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000/) in your browser to use the app

## Using the App

- The app has a simple user interface with a form for entering gene expression data for a patient. 
- The user can enter the expression levels for 20 genes, and submit the form to get a prediction of whether the patient has cancer. 
- The prediction is displayed on the screen as either "Positive" or "Negative".

## Built With

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - The web framework used
- [Pickle](https://docs.python.org/3/library/pickle.html) - Used to load the trained machine learning model
- [Numpy](https://numpy.org/) - Used for handling arrays of gene expression data

## Authors

- **Khaled Nassar** - *Business fair* - [github.com/khalednassar500](https://github.com/khalednassar500/)

## Acknowledgments
- My friends from the university who contributed to the creation of the machine learning model
