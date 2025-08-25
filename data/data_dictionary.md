# Dicionário de Dados — Projeto CardioIA

| Variável                | Descrição                                                                 | Tipo               | Unidade | Valores / Faixa |
|--------------------------|---------------------------------------------------------------------------|--------------------|---------|-----------------|
| patient_id               | Identificador único do paciente (anônimo)                                | integer            | -       | 1..N            |
| age_years                | Idade (anos)                                                            | integer            | anos    | 29–90           |
| sex_male                 | Sexo biológico (1=masculino, 0=feminino)                                | integer (binary)   | -       | 0 ou 1          |
| bmi                      | Índice de Massa Corporal                                                 | float              | kg/m²   | 18–45           |
| systolic_bp_mmHg         | Pressão arterial sistólica                                               | integer            | mmHg    | 90–200          |
| diastolic_bp_mmHg        | Pressão arterial diastólica                                              | integer            | mmHg    | 60–120          |
| total_chol_mg_dL         | Colesterol total                                                         | integer            | mg/dL   | 130–320         |
| hdl_chol_mg_dL           | HDL (bom colesterol)                                                     | integer            | mg/dL   | 25–80           |
| ldl_chol_mg_dL           | LDL (mau colesterol, aprox. pela fórmula de Friedewald)                  | integer            | mg/dL   | 30–250          |
| triglycerides_mg_dL      | Triglicerídeos                                                           | integer            | mg/dL   | 50–400          |
| fasting_glucose_mg_dL    | Glicemia em jejum                                                        | integer            | mg/dL   | 70–220          |
| smoker                   | Tabagista atual                                                          | integer (binary)   | -       | 0 ou 1          |
| diabetes                 | Diagnóstico de diabetes (glicemia ≥ 126 mg/dL)                           | integer (binary)   | -       | 0 ou 1          |
| hypertension             | Hipertensão (PAS ≥ 140 ou PAD ≥ 90)                                      | integer (binary)   | -       | 0 ou 1          |
| family_history           | Histórico familiar de doença cardíaca                                    | integer (binary)   | -       | 0 ou 1          |
| physical_activity_level  | Nível de atividade física (0=baixa … 3=alta)                             | integer (ordinal)  | -       | 0,1,2,3         |
| resting_hr_bpm           | Frequência cardíaca em repouso                                           | integer            | bpm     | 50–110          |
| max_hr_bpm               | Frequência cardíaca máxima estimada em teste                             | integer            | bpm     | 120–200         |
| chest_pain_type          | Tipo de dor torácica (0=assintomático, 1=angina típica, 2=angina atípica, 3=não-anginosa) | integer (categorical) | -   | 0–3             |
| exercise_angina          | Angina induzida por exercício                                            | integer (binary)   | -       | 0 ou 1          |
| st_depression            | Depressão do segmento ST pós-esforço                                     | float              | mm      | 0.00–6.00       |
| st_slope                 | Inclinação do segmento ST (0=descendente, 1=plana, 2=ascendente)         | integer (categorical) | -   | 0–2             |
| rest_ecg                 | ECG de repouso (0=normal, 1=anormalidade ST-T, 2=HVE)                    | integer (categorical) | -   | 0–2             |
| thalassemia              | Talassemia (0=normal, 1=defeito fixo, 2=defeito reversível, 3=desconhecido) | integer (categorical) | -   | 0–3             |
| heart_disease            | **Alvo:** presença de doença cardíaca                                   | integer (binary)   | -       | 0 ou 1          |
