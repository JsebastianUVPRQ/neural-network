import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences


def add_metadata(df, movies_metadata):
    df = df.merge(movies_metadata, on="movie_id", how="left")
    df["release_year"] = pd.to_datetime(df["release_date"]).dt.year
    df["genre_count"] = df["genres"].apply(lambda x: len(x.split("|")))
    return df


def load_data(config):
    """Carga y preprocesa los datos."""
    df = pd.read_csv(config["data"]["path"])
    
    # Codificación de usuarios y películas a índices numéricos
    user_ids = df["user_id"].unique().tolist()
    movie_ids = df["movie_id"].unique().tolist()
    user2idx = {v: k for k, v in enumerate(user_ids)}
    movie2idx = {v: k for k, v in enumerate(movie_ids)}
    
    df["user"] = df["user_id"].map(user2idx)
    df["movie"] = df["movie_id"].map(movie2idx)
    
    # Split en entrenamiento y prueba
    train, test = train_test_split(
        df,
        test_size=config["data"]["test_size"],
        random_state=config["data"]["random_state"]
    )
    
    return train, test, len(user_ids), len(movie_ids)
