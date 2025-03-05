from pydantic import BaseModel, Field

class DataConfig(BaseModel):
    path: str
    test_size: float = Field(..., gt=0, lt=1)
    random_state: int

class ModelConfig(BaseModel):
    embedding_dim: int
    dense_units: list[int]
    dropout_rate: float = Field(..., ge=0, le=1)
    learning_rate: float = Field(..., gt=0)

class TrainingConfig(BaseModel):
    batch_size: int
    epochs: int
    early_stopping_patience: int

class AppConfig(BaseModel):
    data: DataConfig
    model: ModelConfig
    training: TrainingConfig

def validate_config(config):
    return AppConfig(**config)