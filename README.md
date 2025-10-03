#  Heart Disease Analysis

## 1. Descrição e Objetivos
Este é um projeto de **ciência de dados aplicado à saúde**, que tem como objetivo explorar e modelar dados relacionados a doenças cardíacas, a partir de variáveis clínicas e demográficas.  
O estudo envolve as etapas clássicas do **CRISP-DM** (Cross Industry Standard Process for Data Mining):  
- Entendimento do problema  
- Entendimento dos dados  
- Preparação dos dados  
- Análise exploratória (EDA)  
- Modelagem preditiva  
- Avaliação dos resultados  

O objetivo final é identificar os principais fatores que influenciam a ocorrência de doenças cardíacas e construir um modelo preditivo que auxilie na estimativa de risco.

---

## 2. Base de Dados
- Dataset: `heart.csv`  
- Origem: [UCI Machine Learning Repository – Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease)  
- Registos: 303 pacientes  
- Variáveis: 14 variáveis clínicas e demográficas (idade, sexo, pressão arterial, colesterol, eletrocardiograma, etc.)  
- Variável target: presença ou ausência de doença cardíaca (binária).  

---

## 3. Limpeza e Preparação dos Dados
As seguintes etapas foram realizadas:
- Verificação e tratamento de valores nulos.  
- Conversão de variáveis categóricas em numéricas.  
- Normalização/Padronização de variáveis contínuas.  
- Criação de novas variáveis derivadas quando relevante.  

---

## 4. Análise Exploratória (EDA)
Na etapa de **análise exploratória**, foram respondidas as seguintes perguntas:
- Qual a distribuição da idade dos pacientes?  
- Existe diferença significativa entre homens e mulheres na prevalência da doença?  
- Como se relacionam colesterol e pressão arterial com a doença?  
- Quais variáveis apresentam maior correlação com o target?  

**Principais insights:**
- Idade e sexo são fatores determinantes na prevalência da doença.  
- Colesterol elevado está fortemente associado à presença de doença cardíaca.  
- Variáveis relacionadas ao eletrocardiograma e frequência cardíaca também mostraram poder discriminativo.  

Visualizações gráficas (histogramas, boxplots, heatmaps) foram utilizadas para apoiar estas conclusões.

---

## 5. Modelagem Preditiva
Foram testados diferentes algoritmos de **classificação supervisionada**:
- Regressão Logística  
- Random Forest  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

**Métricas utilizadas:**
- Acurácia  
- Precision, Recall e F1-Score  
- ROC-AUC  

O modelo com melhor desempenho foi a **Random Forest**, apresentando um ROC-AUC de aproximadamente **0.85**, mostrando boa capacidade discriminativa.

---

## 6. Aplicação Interativa (Streamlit)
Além da análise em notebook, foi criada uma aplicação interativa em **Streamlit** (`streamlit_app.py`) que permite:
- Inserir variáveis clínicas de um paciente.  
- Obter uma previsão automática sobre a probabilidade de doença cardíaca.  
- Visualizar os principais fatores que influenciaram a decisão do modelo.  

Execução:
```bash
streamlit run streamlit_app.py
```

---

## 7. Estrutura de Pastas

```
heart-disease-analysis/
│── heart disease.ipynb    # Notebook principal
│── heart.csv              # Dataset
│── requirements.txt       # Dependências do projeto
│── streamlit_app.py       # Aplicação Streamlit
│── README.md              # Este documento
```

---

## 8. Tecnologias Utilizadas
- Python 3.x  
- Jupyter Notebook  
- Streamlit  
- Pandas, NumPy, Scikit-learn  
- Matplotlib, Seaborn  

---

## 9. Execução Local

Pré-requisitos:
- Python 3.x  
- pip  
- Git  

Passos:
```bash
# Clonar o repositório
git clone https://github.com/Lage-DataScientist/heart-disease-analysis.git
cd heart-disease-analysis

# Criar ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar notebook
jupyter notebook

# Executar aplicação Streamlit
streamlit run streamlit_app.py
```

---

## 10. Conclusões
- Foi possível identificar variáveis-chave associadas a doenças cardíacas.  
- A modelagem demonstrou que algoritmos baseados em árvores (como Random Forest) apresentaram maior poder preditivo.  
- A aplicação Streamlit torna o projeto acessível e aplicável a contextos reais, permitindo interação direta com os dados.  

Este estudo reforça o papel da ciência de dados na área da saúde, ajudando a construir ferramentas de apoio à decisão clínica.  

---

## 11. Contato
👤 **Autor:** André Lage  
🔗 GitHub: [Lage-DataScientist](https://github.com/Lage-DataScientist)  
🔗 LinkedIn: [Andre Lage DataScientist](https://www.linkedin.com/in/andre-lage-datascientist/) 
🔗 My Website: [Andre Lage DataScientist](https://andre.lagelab.kozow.com/)