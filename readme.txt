# Instalar virtualenv

pip install virtualenv

# Criar ambiente virtual,
py -3 -m venv venv

# Entrar no vitutal env

venv3\Scripts\activate

# Sair no vitutal env

deactivate

# Intalar dependencias

pip install -U Flask scikit-learn==1.2.2  pandas numpy

# Executrar api
python app.py

# Cliente

POST: localhost:5000/cifose

{
    "feature_cifose": [[71,3,5],
                       [128, 4, 5]]
}
