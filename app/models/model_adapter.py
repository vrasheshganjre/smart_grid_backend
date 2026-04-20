"""
Model adapter interface.
Provides a uniform contract for loading and running any trained model.
Concrete implementations (sklearn, PyTorch, ONNX, etc.) go in subclasses.
"""
from __future__ import annotations

from typing import Any, Protocol
import numpy as np
import pandas as pd

from app.core.config import settings


class ModelProtocol(Protocol):
    """
    Structural protocol that any concrete model wrapper must satisfy.
    Use this for type hints and tests.
    """

    def load(self, path: str) -> None: ...
    def predict(self, features: pd.DataFrame) -> np.ndarray: ...


class ModelAdapter:
    """
    Default model adapter stub.

    TODO:
        - Pick the model serialisation format (pickle, joblib, ONNX, TorchScript …).
        - Implement load() to deserialise the artefact from settings.MODEL_PATH.
        - Implement predict() to run inference and return a numpy array.
        - Add input validation (expected feature names and shapes).
    """

    def __init__(self) -> None:
        self.model: Any = None

    def load(self, path: str | None = None) -> None:
        """
        Load model artefact from disk.

        TODO: replace with real loading logic, e.g.:
            import joblib
            self.model = joblib.load(path or settings.MODEL_PATH)
        """
        raise NotImplementedError("ModelAdapter.load is not yet implemented.")

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        """
        Run inference on the feature matrix.

        Args:
            features: DataFrame of shape (n_samples, n_features).

        Returns:
            1-D numpy array of predictions.

        TODO: implement after load() is working.
        """
        raise NotImplementedError("ModelAdapter.predict is not yet implemented.")
