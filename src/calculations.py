import numpy as np
from config import INFLATION_RATE

def project_earnings(salary, work_months):
    """Compute earnings with inflation"""
    earnings = []
    for month in range(work_months):
        salary *= (1 + INFLATION_RATE / 12) 
        earnings.append(salary)
    return np.sum(earnings) 
