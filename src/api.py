from flask import Flask, request, jsonify
import tensorflow as tf
import pandas as pd
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import numpy as np

app = Flask(__name__)

# Cargar modelo y datos primero para evitar carga en cada request
model = tf.keras.models.load_model("trained_model")
movies = pd.read_csv("data/movies.csv")

# Crear mapeo de títulos a índices (debería venir del entrenamiento)
movie2idx = {title: idx for idx, title in enumerate(movies['title'])}  # Asumiendo columna 'title'

# Simular mapeo de usuarios (debería cargarse de datos reales)
# Esto es solo un ejemplo - deberías cargar desde un archivo
user2idx = {f"user_{i}": i for i in range(1000)}

# Métricas Prometheus
REQUEST_COUNT = Counter("request_count", "Total number of requests", ['endpoint', 'method'])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency", ['endpoint'])
ERROR_COUNT = Counter("request_errors", "Total request errors", ['error_type'])

@app.route("/predict", methods=["POST"])
def predict():
    """Endpoint para predicciones de recomendaciones"""
    REQUEST_COUNT.labels(endpoint='/predict', method='POST').inc()
    
    with REQUEST_LATENCY.labels(endpoint='/predict').time():
        try:
            data = request.get_json()
            
            # Validar entrada
            if not data or 'user_id' not in data or 'movie_title' not in data:
                ERROR_COUNT.labels(error_type='invalid_input').inc()
                return jsonify({"error": "Datos incompletos"}), 400
        except Exception as e:
            ERROR_COUNT.labels(error_type='json_parsing_error').inc()
            return jsonify({"error": f"Error al procesar JSON: {str(e)}"}), 400
                
            user_id = data['user_id']
            movie_title = data['movie_title']
            
            # Obtener índices
            try:
                user_idx = user2idx[user_id]
                movie_idx = movie2idx[movie_title]
            except KeyError as e:
                ERROR_COUNT.labels(error_type='invalid_id').inc()
                return jsonify({"error": f"ID no encontrado: {str(e)}"}), 404
            
            # Hacer predicción
            prediction = model.predict([np.array([user_idx]), np.array([movie_idx)])
            
            return jsonify({
                "user_id": user_id,
                "movie_title": movie_title,
                "predicted_rating": float(prediction[0][0])
            })
            
            except Exception as e:
                ERROR_COUNT.labels(error_type='server_error').inc()
                return jsonify({"error": f"Error interno: {str(e)}"}), 500

@app.route("/metrics")
def metrics():
    """Endpoint para monitoreo Prometheus"""
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # Debug=False en producción