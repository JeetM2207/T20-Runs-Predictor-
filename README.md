# 🏏 T20 Runs Predictor

Welcome to the **T20 Runs Predictor** — a machine learning-powered web app that predicts the final score of a T20 cricket innings using ball-by-ball match data.

🔴 Try it live: [t20runspredictor.streamlit.app](https://t20runspredictor.streamlit.app/)

---

## 📊 About the Project

This app uses a trained ML pipeline built using **Random Forest** and **XGBoost** regressors to predict the final score of a batting team in a T20 match.

The features used include:
- Batting team
- Bowling team
- Match city
- Overs completed
- Runs scored so far
- Wickets fallen
- Runs in the last 5 overs
- Current run rate (CRR)

---

## 🚀 Live Demo

![App Screenshot Placeholder](https://user-images.githubusercontent.com/yourusername/screenshot.png)

👉 Visit the app here: [https://t20runspredictor.streamlit.app/](https://t20runspredictor.streamlit.app/)

---

## 🧠 Machine Learning Pipeline

- Data extracted from YAML match files
- Feature engineering: `CRR`, `Last 5 Over Runs`
- Model training using:
  - `RandomForestRegressor`
  - `XGBRegressor`
- Pipeline saved using `pickle`

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🌐
- Pandas, NumPy 📊
- Scikit-learn 🤖
- XGBoost 🔥
- Git & GitHub

---

## 📁 Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/JeetM2207/T20-Runs-Predictor-.git
cd T20-Runs-Predictor-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
