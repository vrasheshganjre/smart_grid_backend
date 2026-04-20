"""
CSV parsing service.
Converts raw uploaded bytes into a validated pandas DataFrame.
"""
import io
import pandas as pd


def parse_uploaded_csv(
    contents: bytes,
    return_dataframe: bool = False,
) -> dict | pd.DataFrame:
    """
    Parse raw CSV bytes.

    Args:
        contents: Raw bytes from the uploaded file.
        return_dataframe: When True, returns the full DataFrame instead of metadata.

    Returns:
        dict with 'rows' and 'columns' keys, or a DataFrame when return_dataframe=True.

    TODO:
        - Add column validation against an expected schema.
        - Add data-quality checks (nulls, dtypes, value ranges).
        - Add support for different CSV dialects / encodings.
    """
    df = pd.read_csv(io.BytesIO(contents))

    if return_dataframe:
        return df

    return {"rows": len(df), "columns": list(df.columns)}
