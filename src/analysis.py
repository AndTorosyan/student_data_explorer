import numpy as np
from .exceptions import DataError

def summarize(values):
 arr = np.array(values, dtype=float)
 if arr.size == 0:
    raise DataError("No numeric data to analyze.")
 if np.isnan(arr).any():
    raise DataError("Data contains non-numeric values.")
 return {
 "count": int(arr.size),
 "mean": float(arr.mean()),
 "min": float(arr.min()),
 "max": float(arr.max()),
 "std": float(arr.std()),
 "median": float(np.median(arr))
 } 
