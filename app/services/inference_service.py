"""
Model inference service.
Loads the trained model and runs predictions on the enriched DataFrame.
"""
import pandas as pd

from app.models.model_adapter import ModelAdapter


def run_inference(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run model inference on the weather-enriched power dataset.

    Args:
        df: DataFrame with all feature columns present (including weather columns).

    Returns:
        DataFrame with an appended 'prediction' column (or a separate predictions df).

    TODO:
        - Select the correct feature columns expected by the model.
        - Load model via ModelAdapter.load().
        - Call ModelAdapter.predict(features).
        - Append predictions back to df under an appropriate column name.
        - Handle model loading errors and invalid feature shapes.
    """
    # Placeholder — returns df unchanged until implemented
    adapter = ModelAdapter()  # noqa: F841  TODO: use adapter for real predictions
    return df
