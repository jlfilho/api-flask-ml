import numpy as np
import pandas as pd
from flask import Flask, jsonify
import pickle
from flask import request
import os

## ultimo bloco de código:
## carregando o modelo para o código
with open("./utils/model_dtree.pickle","rb") as f:
    #Carrega o arquivo model.pickle em modo read binary
    modelo_carregado = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def primeiro_endpoint_get():
  return "Tudo Funcionando Corretamente !", 200

@app.route("/cifose",methods=["POST"])
def cifose():
  feature_cifose = request.json['feature_cifose']
  # print(feature_cifose)
  feature_cifose = np.array(feature_cifose)
  panda_df = pd.DataFrame(data = feature_cifose,  
                        columns = ["Age","Number","Start"])
  # print(panda_df)
  pred = modelo_carregado.predict(panda_df)
  print("cifose:", pred)
  return (f"cifose: {pred}", 200)

if __name__ == "__main__":
  debug = True # com essa opção como True, ao salvar, o "site" recarrega automaticamente.
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=debug)