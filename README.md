# Electric Vehicle Adoption Prediction Web App

## Overview

This project is a Machine Learning web application that predicts an individual's likelihood of adopting an Electric Vehicle (EV). Using user-provided demographic, economic, behavioral, and perception-related information, the model classifies users into one of three adoption categories:

- 🟢 **Low**
- 🟡 **Medium**
- 🔴 **High**

The application is built with **Streamlit** and provides an interactive interface for users to enter their information and receive an instant prediction.

---

## Features

- Interactive Streamlit web interface
- Predicts EV adoption likelihood using a trained Machine Learning model
- Classifies users into:
  - Low Adoption Likelihood
  - Medium Adoption Likelihood
  - High Adoption Likelihood
- Simple and user-friendly input form
- Fast predictions using a serialized (`.pkl`) model

---

## Input Features

The prediction model uses the following features:

| Feature | Description |
|---------|-------------|
| Age | User's age |
| Annual Income | Annual income |
| Education Level | Encoded education level |
| Location | Encoded residential location |
| Daily Commute | Daily commuting distance |
| Weekly Travel | Weekly travel distance |
| Car Ownership | Encoded vehicle ownership/type |
| Vehicle Age | Age of current vehicle |
| Fuel Expense | Monthly fuel expenditure |
| Charging Station Availability | Availability of public charging stations |
| Distance to Nearest Charging Station | Distance to closest charging station |
| Home Charging | Encoded home charging availability |
| Electricity Cost | Monthly electricity cost |
| Environmental Awareness | Environmental consciousness score |
| Government Awareness | Awareness of EV government incentives |
| Technology Affinity | Interest in adopting new technology |
| Range Anxiety | Concern about EV driving range |
| Battery Concern | Concern about battery performance/life |
| EV Knowledge | Knowledge of electric vehicles |
| Previous EV Experience | Encoded previous EV experience |
| Monthly Energy Consumption | Monthly household energy usage |
| Monthly Charging Requirement | Estimated monthly charging requirement |

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Feature Encoding
4. Model Training
5. Model Evaluation
6. Model Serialization using Joblib
7. Deployment with Streamlit

---

## Project Structure

```text
Electric-Vehicle-Adoption-Prediction/
│
├── app.py                  # Streamlit web application
├── EV_Adoption.ipynb       # Model development notebook
├── model.joblib               # Trained machine learning model
├── dataset.csv             # Dataset used for training
├── requirements.txt        # Project dependencies
└── README.md
```

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/electric-vehicle-adoption-prediction.git
```

### 2. Navigate into the project directory

```bash
cd electric-vehicle-adoption-prediction
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

---

## Model Output

The model predicts one of the following classes:

| Prediction | Meaning |
|------------|---------|
| **Low** | User has a low likelihood of adopting an Electric Vehicle |
| **Medium** | User has a moderate likelihood of adopting an Electric Vehicle |
| **High** | User has a high likelihood of adopting an Electric Vehicle |

---

## Dataset

The dataset contains demographic, financial, transportation, and behavioral information related to electric vehicle adoption. It includes variables such as age, income, commuting habits, charging accessibility, environmental awareness, technology affinity, and previous EV experience.

---

## Future Improvements

- Deploy the application using Streamlit Community Cloud
- Display prediction confidence/probability scores
- Add feature importance visualization
- Improve the user interface and responsiveness
- Compare multiple machine learning models
- Integrate Explainable AI techniques (SHAP/LIME)

---

## License

This project is intended for educational and research purposes.

---

## Author

**Adedeji Badmus**

Computer Science Student | Machine Learning Enthusiast
