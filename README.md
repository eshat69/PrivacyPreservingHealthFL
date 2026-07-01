[![View Repository](https://img.shields.io/badge/View-Repository-blue?style=for-the-badge&logo=github)](https://github.com/eshat69/PrivacyPreservingHealthFL)
![GitHub stars](https://img.shields.io/github/stars/eshat69/PrivacyPreservingHealthFL?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/eshat69/PrivacyPreservingHealthFL)
![GitHub repo size](https://img.shields.io/github/repo-size/eshat69/PrivacyPreservingHealthFL)
![GitHub language](https://img.shields.io/github/languages/top/eshat69/PrivacyPreservingHealthFL)
![Issues](https://img.shields.io/github/issues/eshat69/PrivacyPreservingHealthFL?style=flat-square)

# PrivacyPreservingHealthFL

> **Interpretable Privacy-Preserving Federated Learning for Healthcare Analytics**

A research-oriented federated learning framework for healthcare analytics that enables collaborative model training while preserving patient privacy. This project combines **Federated Learning**, **Differential Privacy**, and **Explainable AI (XAI)** to develop trustworthy machine learning models for healthcare data.

---

## 📌 Project Overview

Healthcare organizations often cannot share sensitive patient data due to privacy regulations and ethical concerns. Traditional centralized machine learning requires collecting all data in one location, increasing privacy and security risks.

This project proposes a **Privacy-Preserving Federated Learning** framework where multiple hospitals collaboratively train a global model without exchanging raw patient data. To further strengthen privacy, **Differential Privacy (Opacus)** is incorporated during local training. Model predictions are interpreted using **SHAP (SHapley Additive Explanations)** to improve transparency and trust.

---

## 🎯 Objectives

- Build a centralized baseline using machine learning.
- Simulate multiple hospitals using the UCI Heart Disease dataset.
- Implement Federated Learning using Flower and PyTorch.
- Integrate Differential Privacy with Opacus.
- Explain model predictions using SHAP.
- Compare centralized and federated learning performance.

---

## 🚀 Features

- Federated Learning with Flower
- PyTorch Neural Network
- Differential Privacy using Opacus
- Explainable AI using SHAP
- Centralized XGBoost Benchmark
- Automated Data Preprocessing
- Exploratory Data Analysis (EDA)
- Model Evaluation and Visualization

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Machine Learning | Scikit-learn, XGBoost |
| Deep Learning | PyTorch |
| Federated Learning | Flower |
| Differential Privacy | Opacus |
| Explainable AI | SHAP |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Development | Jupyter Notebook, VS Code |

---

## 📂 Project Structure

```text
PrivacyPreservingHealthFL/

├── data/
│   ├── raw/
│   ├── processed/
│   └── clients/
│
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_centralized_baseline.ipynb
│   ├── 04_prepare_clients.ipynb
│   ├── 05_federated_learning.ipynb
│   ├── 06_differential_privacy.ipynb
│   └── 07_evaluation.ipynb
│
├── models/
├── results/
├── reports/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📊 Dataset

**Dataset:** UCI Heart Disease Dataset

The dataset contains patient clinical information collected from multiple hospitals.

Hospitals used as federated clients:

- Cleveland
- Hungarian
- Switzerland
- VA Long Beach

Each hospital is treated as an independent federated client during training.

---

## 🧠 Machine Learning Pipeline

```
Raw Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Centralized Learning (XGBoost)
      │
      ▼
Client Preparation
      │
      ▼
Federated Learning (Flower + PyTorch)
      │
      ▼
Differential Privacy (Opacus)
      │
      ▼
Explainability (SHAP)
      │
      ▼
Performance Evaluation
```

---

## 📈 Models

### Centralized Learning

- Logistic Regression
- Random Forest
- XGBoost (Best Baseline)

### Federated Learning

- PyTorch Neural Network
- FedAvg Aggregation

### Privacy Enhancement

- Differential Privacy (Opacus)

### Explainability

- SHAP (SHapley Additive Explanations)

---

## 📊 Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

---

## 📸 Results

The project compares:

| Model | Accuracy | Privacy | Explainability |
|--------|----------|----------|----------------|
| Centralized XGBoost | ✅ | ❌ | ✅ |
| Federated Learning | ✅ | ✅ | ✅ |
| Federated + Differential Privacy | ✅ | ✅✅ | ✅ |

---

## 🔒 Privacy Approach

Instead of sharing patient data:

- Each hospital trains its own local model.
- Only model parameters are communicated.
- Differential Privacy adds controlled noise to protect sensitive information.
- SHAP explains model predictions without exposing raw data.

---

## ▶️ Getting Started

Clone the repository:

```bash
git clone https://github.com/<your-username>/PrivacyPreservingHealthFL.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebooks in the following order:

1. 01_preprocessing.ipynb
2. 02_eda.ipynb
3. 03_centralized_baseline.ipynb
4. 04_prepare_clients.ipynb
5. 05_federated_learning.ipynb
6. 06_differential_privacy.ipynb
7. 07_evaluation.ipynb

---

## 🔮 Future Work

- Support MIMIC-IV dataset
- Add Secure Aggregation
- Experiment with FedProx and FedAdam
- Deploy using Docker and Kubernetes
- Integrate Homomorphic Encryption
- Develop a web dashboard for monitoring federated training

---

## 📚 References

- Flower Federated Learning Framework
- PyTorch
- Opacus
- SHAP
- XGBoost
- UCI Machine Learning Repository

---

## 👨‍💻 Author

**Eshat Rahman**

B.Sc. in Computer Science and Engineering

---

## 📄 License

This project is released under the **MIT License**.
