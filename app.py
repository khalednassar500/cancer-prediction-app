from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model from the .pkl file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    
@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
  <head>
    <title>Cancer Prediction Model</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        max-width: 800px;
        border: 2px solid gray;
        margin: auto;
        background-color: #efefef;
        font-size: 1.2em;
      }

      header {
        background-color: #fff;    
        padding: 25px;
      }
      h1 {
        color: blue;
      }
      p {
        text-align: justify;
        font-size: 1.1em;
        line-height: 1.2em;
      }
      input {
        padding: 5px; font-size: 1em;
      }
      button {
        padding: 5px 10px;
        border: 0;
        box-shadow: 2px 2px 5px gray;
        font-size: 1em;
        font-weight: bold;
        cursor: pointer;
      }
      button:hover {
        color: blue;
      }

      label {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        border: 1px solid lightgray;
        margin: 10px 0;
      }
    </style>
  </head>
  <body>
    <header >
      <div >
        <h1 >Cancer Prediction Model</h1>
        <p>
          Colon cancer is the third most common cancer worldwide and early detection is crucial for successful treatment. 
          A colon cancer prediction model is a tool that uses input Genet data to predict the likelihood of a patient having colon cancer. 
          The model utilizes techniques such as logistic regression, random forest, or neural networks to make predictions. 
          By analyzing these input features, the model can provide a probability or binary classification of whether a patient has colon cancer or not. 
          While these models can be a useful tool for early detection, it's important to keep in mind the limitations of the model such as its potential for bias, its dependence on the quality and representativeness of the training data, and its generalizability to new unseen data. 
          Additionally, it's important to consider ethical considerations such as patient privacy and fair predictions when implementing the model in practice.
        </p>
        <hr>
        <h3>Enter the patient's Genetic data</h3>
        <form  method="post" action="/predict">
          <label for="gene1"> 
            <p>Gene 1 : -</p> 
            <input type="number" id="gene1" placeholder="Gene 1" name="genes[]" required  />
          </label>
          <label for="gene2"> 
            <p>Gene 2 : -</p> 
            <input type="number" id="gene2" placeholder="Gene 2" name="genes[]" required  />
          </label>
          <label for="gene3"> 
            <p>Gene 3 : -</p> 
            <input type="number" id="gene3" placeholder="Gene 3" name="genes[]" required  />
          </label>
          <label for="gene4"> 
            <p>Gene 4 : -</p> 
            <input type="number" id="gene4" placeholder="Gene 4" name="genes[]" required  />
          </label>
          <label for="gene5"> 
            <p>Gene 5 : -</p> 
            <input type="number" id="gene5" placeholder="Gene 5" name="genes[]" required  />
          </label>
          <label for="gene6"> 
            <p>Gene 6 : -</p> 
            <input type="number" id="gene6" placeholder="Gene 6" name="genes[]" required  />
          </label>
          <label for="gene7"> 
            <p>Gene 7 : -</p> 
            <input type="number" id="gene7" placeholder="Gene 7" name="genes[]" required  />
          </label>
          <label for="gene8"> 
            <p>Gene 8 : -</p> 
            <input type="number" id="gene8" placeholder="Gene 8" name="genes[]" required  />
          </label>
          <label for="gene9"> 
            <p>Gene 9 : -</p> 
            <input type="number" id="gene9" placeholder="Gene 9" name="genes[]" required  />
          </label>
          <label for="gene10"> 
            <p>Gene 10 : -</p> 
            <input type="number" id="gene10" placeholder="Gene 10" name="genes[]" required  />
          </label>
          <label for="gene11"> 
            <p>Gene 11 : -</p> 
            <input type="number" id="gene11" placeholder="Gene 11" name="genes[]" required  />
          </label>
          <label for="gene12"> 
            <p>Gene 12 : -</p> 
            <input type="number" id="gene12" placeholder="Gene 12" name="genes[]" required  />
          </label>
          <label for="gene13"> 
            <p>Gene 13 : -</p> 
            <input type="number" id="gene13" placeholder="Gene 13" name="genes[]" required  />
          </label>
          <label for="gene14"> 
            <p>Gene 14 : -</p> 
            <input type="number" id="gene14" placeholder="Gene 14" name="genes[]" required  />
          </label>
          <label for="gene15"> 
            <p>Gene 15 : -</p> 
            <input type="number" id="gene15" placeholder="Gene 15" name="genes[]" required  />
          </label>
          <label for="gene16"> 
            <p>Gene 16 : -</p> 
            <input type="number" id="gene16" placeholder="Gene 16" name="genes[]" required  />
          </label>
          <label for="gene17"> 
            <p>Gene 17 : -</p> 
            <input type="number" id="gene17" placeholder="Gene 17" name="genes[]" required  />
          </label>
          <label for="gene18"> 
            <p>Gene 18 : -</p> 
            <input type="number" id="gene18" placeholder="Gene 18" name="genes[]" required  />
          </label>
          <label for="gene19"> 
            <p>Gene 19 : -</p> 
            <input type="number" id="gene19" placeholder="Gene 19" name="genes[]" required  />
          </label>
          <label for="gene20"> 
            <p>Gene 20 : -</p> 
            <input type="number" id="gene20" placeholder="Gene 20" name="genes[]" required  />
          </label>
          <br>
          <br>
          <button type="submit">Predict</button>
        </form>
        
      </div>
    </header>
  </body>
</html>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.getlist('genes[]')
    # Make a prediction using the model
    print('==================')
    print(data)
    print('==================')
    
    data = [np.array(data)]#np.array(data).reshape(-1,1)
    prediction = model.predict(data)
    
    print(type(prediction))
    a = prediction
    b = 'Negative'
    if  a == 1:
        b = 'Positive'

    return ''' <!DOCTYPE html>
<html>
  <head>
    <title>Cancer Prediction Model</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        background-color: #efefef;
        font-size: 1.2em;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
      }
      header {
        max-width: 800px;
        background-color: #fff;
        border: 2px solid gray;
        padding: 25px;
      }
      p {
        text-align: justify;
        font-size: 1.1em;
        line-height: 1.2em;
      }
      span {
        font-size: 1.1em;
        font-weight: bold;
        color: blue;
      }
    </style>
  </head>
  <body>
    <header >
      <p>Based on the genetic data you entered, the prognosis for colon cancer for this patient is ( <span>''' + '{}'.format(b) +  '''</span> )</p>
    </header>
  </body>
</html>'''

if __name__ == '__main__':
    app.run()