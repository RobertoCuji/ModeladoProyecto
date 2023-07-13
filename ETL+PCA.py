from pymongo import MongoClient
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['Proyecto']  # nombre de la base de datos
collection = db['grupal']
print("Conexión establecida")

# Contar datos de mi colección
number_of_products = collection.count_documents({})
print(number_of_products, "elementos en la colección")

# Mineria de Datos
print("Minería de datos")
################################################################

