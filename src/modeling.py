import pandas as pd
import numpy as np
import statsmodels.api as sm
from typing import Optional, List, Dict, Any

def multiple_linear_regression(
    df: pd.DataFrame, outcome: str, predictors: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Fit a multiple linear regression model.
    """
    import statsmodels.api as sm

    # Outcome must be numeric
    if not pd.api.types.is_numeric_dtype(df[outcome]):
        raise ValueError("Outcome must be numeric.")
