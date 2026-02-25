from __future__ import annotations
import pandas as pd
import statsmodels.api as sm
from typing import Optional, List, Dict, Any

def multiple_linear_regression(
    df: pd.DataFrame, outcome: str, predictors: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    TODO (Student task): Fit a multiple linear regression model.
    """
    #Recieved help at TA session
    if not pd.api.types.is_numeric_dtype(df[outcome]): #Raise error if ther is not a numeric output
        raise ValueError(f"Outcome column '{outcome}' must be numeric.")

    if predictors is None: #If predictors is none use all numeric columns except outcome by default in the regression
        predictors = df.select_dtypes(include=['number']).columns.drop(outcome).tolist()

    data = df[[outcome] + predictors].dropna() #Temporary clean data. Made with help since I was getting strange errors.
    y = data[outcome] #Steps from the hint
    X = sm.add_constant(data[predictors])
    model = sm.OLS(y, X).fit() #Run it

    results = { #Extract results and convert to Python types
        "outcome": outcome,
        "predictors": predictors,
        "n_rows_used": int(len(data)),
        "r_squared": float(model.rsquared),
        "adj_r_squared": float(model.rsquared_adj),
        "intercept": float(model.params['const']),
        "coefficients": model.params.drop('const').to_dict()
    }

    return results







"""
from typing import Optional, List, Dict, Any
import pandas as pd
import statsmodels.api as sm 


def multiple_linear_regression(
    df: pd.DataFrame, outcome: str, predictors: Optional[List[str]] = None
) -> Dict[str, Any]:
    
    #TOdO (Student task): Fit a multiple linear regression model.
    
    #Recieved help at TA session
    if not pd.api.types.is_numeric_dtype(df[outcome]):
        raise ValueError(f"Outcome column '{outcome}' must be numeric.")

    if predictors is None:
        predictors = df.select_dtypes(include=['number']).columns.drop(outcome).tolist()

    data = df[[outcome] + predictors].dropna()
    y = data[outcome]
    X = sm.add_constant(data[predictors])
    model = sm.OLS(y, X).fit()

    results = {
        "outcome": outcome,
        "predictors": predictors,
        "n_rows_used": int(len(data)),
        "r_squared": float(model.rsquared),
        "adj_r_squared": float(model.rsquared_adj),
        "intercept": float(model.params['const']),
        "coefficients": model.params.drop('const').to_dict()
    }

    return results
"""
