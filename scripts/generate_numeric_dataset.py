import numpy as np
resting_ecg = np.random.choice(['normal','stt_abnormal','lv_hypertrophy'], size=N, p=[0.75,0.2,0.05])
exercise_induced_angina = np.random.choice([0,1], size=N, p=[0.8,0.2])


oldpeak = np.clip(np.random.exponential(0.6, size=N), 0, 6)
st_slope = np.random.choice(['up','flat','down'], size=N, p=[0.5,0.35,0.15])


# Score de risco sintético: pondera fatores clássicos
risk_score = (
0.02*(age-50) + 0.03*(sbp-120) + 0.02*(cholesterol_total-180) +
0.03*(fasting_glucose-100) + 0.05*(bmi-27) + 0.2*family_history +
0.15*(smoking_status == 'current').astype(int) + 0.1*(st_slope=='down').astype(int) +
0.1*exercise_induced_angina + 0.08*oldpeak
)


prob_hd = 1/(1 + np.exp(- ( -1.2 + risk_score )))


target_heart_disease = (np.random.rand(N) < prob_hd).astype(int)


# Monta DataFrame


df = pd.DataFrame({
'id': np.arange(1, N+1),
'age': age,
'sex': sex,
'bmi': np.round(bmi,2),
'sbp': sbp,
'dbp': dbp,
'cholesterol_total': cholesterol_total,
'fasting_glucose': fasting_glucose,
'heart_rate': heart_rate,
'smoking_status': smoking_status,
'family_history': family_history,
'chest_pain_type': chest_pain_type,
'resting_ecg': resting_ecg,
'exercise_induced_angina': exercise_induced_angina,
'oldpeak': np.round(oldpeak,2),
'st_slope': st_slope,
'target_heart_disease': target_heart_disease
})


# Saída
out_dir = Path('data')
out_dir.mkdir(parents=True, exist_ok=True)


df.to_csv(out_dir / 'cardio_numeric_dataset.csv', index=False)
try:
import openpyxl # para xlsx
df.to_excel(out_dir / 'cardio_numeric_dataset.xlsx', index=False)
except Exception as e:
print('Aviso: não foi possível exportar .xlsx (instale openpyxl). Erro:', e)


print('Gerado data/cardio_numeric_dataset.csv (e .xlsx se possível). Linhas:', len(df))