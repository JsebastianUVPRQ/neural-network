import yaml
from data_loader import load_data
from model import RecommenderNet
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard

class Pipeline:
    def __init__(self, config_path):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)
        self.train_data, self.test_data, self.num_users, self.num_movies = load_data(self.config)

    def build_model(self):
        return RecommenderNet(
            num_users=self.num_users,
            num_movies=self.num_movies,
            embedding_dim=self.config["model"]["embedding_dim"],
            dense_units=self.config["model"]["dense_units"],
            dropout_rate=self.config["model"]["dropout_rate"]
        )

    def train(self):
        model = self.build_model()
        model.compile(
            optimizer="adam",
            loss="mse",
            metrics=["RootMeanSquaredError"]
        )
        callbacks = [
            EarlyStopping(patience=self.config["training"]["early_stopping_patience"]),
            TensorBoard(log_dir="logs")
        ]
        history = model.fit(
            self.train_data,
            validation_data=self.test_data,
            epochs=self.config["training"]["epochs"],
            callbacks=callbacks
        )
        model.save("trained_model")
        return history