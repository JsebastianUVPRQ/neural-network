import yaml
import tensorflow as tf
from data_loader import load_data
from model import RecommenderNet
from tensorflow.keras.callbacks import ReduceLROnPlateau, ModelCheckpoint

# Cargar configuración
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Cargar datos
train, test, num_users, num_movies = load_data(config)

# Preparar datasets
def df_to_dataset(df, shuffle=True, batch_size=64):
    dataset = tf.data.Dataset.from_tensor_slices((
        df[["user", "movie"]].values,
        df["rating"].values
    ))
    if shuffle:
        dataset = dataset.shuffle(buffer_size=10000)
    return dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)

train_ds = df_to_dataset(train, batch_size=config["training"]["batch_size"])
test_ds = df_to_dataset(test, shuffle=False, batch_size=config["training"]["batch_size"])

# Inicializar modelo
model = RecommenderNet(
    num_users=num_users,
    num_movies=num_movies,
    embedding_dim=config["model"]["embedding_dim"],
    dense_units=config["model"]["dense_units"],
    dropout_rate=config["model"]["dropout_rate"]
)

# Compilar
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=config["model"]["learning_rate"]),
    loss="mse",
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

# Callbacks
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=config["training"]["early_stopping_patience"],
        restore_best_weights=True
    ),
    tf.keras.callbacks.TensorBoard(log_dir="logs")
]

# Entrenar
history = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=config["training"]["epochs"],
    callbacks=callbacks
)

# Guardar modelo
model.save("trained_model")
