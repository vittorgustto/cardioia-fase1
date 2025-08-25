import pandas as pd
from pathlib import Path


fp_csv = Path('data/cardio_numeric_dataset.csv')
assert fp_csv.exists(), f'Arquivo não encontrado: {fp_csv}'


df = pd.read_csv(fp_csv)


# Regras mínimas
assert len(df) >= 100, 'Dataset deve ter pelo menos 100 linhas.'
required_cols = [
'id','age','sex','bmi','sbp','dbp','cholesterol_total','fasting_glucose',
'heart_rate','smoking_status','family_history','chest_pain_type','resting_ecg',
'exercise_induced_angina','oldpeak','st_slope','target_heart_disease'
]
missing = [c for c in required_cols if c