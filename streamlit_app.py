import streamlit as st
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

# ==============================
# 1. Carregar o pipeline treinado
# ==============================
modelo = joblib.load("modelo_cardiaco.pkl")

# Criar explainer SHAP para o modelo carregado
explainer = shap.TreeExplainer(modelo.named_steps["classifier"])

# ==============================
# 2. Criar interface no Streamlit
# ==============================
st.title("🫀 Predição de Doença Cardíaca com Explicabilidade SHAP")

st.write("Insere os dados do paciente para prever o risco de doença cardíaca e ver os fatores que mais influenciaram a decisão.")

# Inputs
age = st.number_input("Idade", 20, 100, 50)
sex = st.selectbox("Sexo", ["Masculino", "Feminino"])
cp = st.selectbox("Tipo de Dor no Peito", [0, 1, 2, 3])
trtbps = st.number_input("Pressão Arterial em Repouso (mmHg)", 80, 200, 120)
chol = st.number_input("Colesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Glicemia > 120 mg/dl", [0, 1])
rest_ecg = st.selectbox("Resultados ECG", [0, 1, 2])
thalach = st.number_input("Frequência Cardíaca Máxima", 50, 250, 150)
exang = st.selectbox("Angina induzida por exercício", [0, 1])
oldpeak = st.number_input("Depressão ST", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Inclinação do ST", [0, 1, 2])
ca = st.selectbox("Número de vasos coloridos", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# ==============================
# 3. Preparar dados do paciente
# ==============================
dados = pd.DataFrame([{
    "age": age,
    "sex": 1 if sex == "Masculino" else 0,
    "cp": cp,
    "trtbps": trtbps,
    "chol": chol,
    "fbs": fbs,
    "rest_ecg": rest_ecg,  
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}])


# ==============================
# 4. Fazer previsão
# ==============================
if st.button("🔮 Prever Risco"):
    prob = modelo.predict_proba(dados)[:, 1][0]

    threshold = 0.4
    pred = 1 if prob >= threshold else 0

    # Mostrar resultado
    st.write(f"**Probabilidade de Doença:** {prob:.2%}")
    if pred == 1:
        st.error("🚨 O modelo prevê que o paciente **TEM risco de doença cardíaca**.")
    else:
        st.success("✅ O modelo prevê que o paciente **NÃO tem risco significativo de doença cardíaca**.")

    # ==============================
    # 5. Explicação com SHAP
    # ==============================
    st.subheader("📊 Fatores que influenciaram esta previsão")

    # Calcular SHAP values para este paciente
    preprocessor = modelo.named_steps["preprocessor"]
    dados_transformados = preprocessor.transform(dados)

    shap_values = explainer.shap_values(dados_transformados, check_additivity=False)
    shap_values_class1 = shap_values[:, :, 1]   # só classe positiva

    # Criar objeto Explanation
    explanation = shap.Explanation(
        values=shap_values_class1[0],
        base_values=explainer.expected_value[1],
        data=dados_transformados[0],
        feature_names=preprocessor.get_feature_names_out()
    )

    # Criar figura SHAP waterfall
    fig, ax = plt.subplots(figsize=(10, 6))
    shap.plots.waterfall(explanation, show=False)
    st.pyplot(fig)
