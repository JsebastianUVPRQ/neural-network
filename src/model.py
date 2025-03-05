from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Concatenate, Dense, Dropout

class RecommenderNet(Model):
    def __init__(self, num_users, num_movies, embedding_dim, dense_units, dropout_rate):
        super().__init__()
        self.user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim)
        self.movie_embedding = Embedding(input_dim=num_movies, output_dim=embedding_dim)
        
        self.flatten = Flatten()
        self.concat = Concatenate()
        
        self.dense_layers = []
        for units in dense_units:
            self.dense_layers.append(Dense(units, activation="relu"))
            self.dense_layers.append(Dropout(dropout_rate))
        
        self.output_layer = Dense(1, activation="linear")  # Predicción de calificación

    def call(self, inputs):
        user_vector = self.flatten(self.user_embedding(inputs[:, 0]))
        movie_vector = self.flatten(self.movie_embedding(inputs[:, 1]))
        x = self.concat([user_vector, movie_vector])
        for layer in self.dense_layers:
            x = layer(x)
        return self.output_layer(x)