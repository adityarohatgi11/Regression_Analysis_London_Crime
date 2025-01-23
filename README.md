This repository contains an enhanced analysis of the relationship between police deployment and crime rates in London, incorporating both econometric methods and machine learning models. The study builds upon the paper *"Panic on the Streets of London: Police, Crime, and the July 2005 Terror Attacks"* by Draca, Machin, and Witt (AER, 2011).

---

## Project Overview

This analysis investigates the impact of police deployment on crime rates using weekly panel data from 32 boroughs in London over two years. The dataset includes variables such as crime, police hours, population, unemployment rate, labor force participation, demographic breakdowns, and more. The study employs econometric methods alongside machine learning models to estimate the causal effect of police presence on crime rates and to predict crime trends.

---

## Methodologies Deployed

### 1. **Log-Log Regression (Cross-Sectional Analysis)**
   - **Objective**: Explore the relationship between crime rate and police rate, controlling for unemployment, labor force participation, young male percentage, and white percentage.
   - **Transformation**: Natural log transformation of variables to handle non-linear relationships.
   - **Method**: Ordinary Least Squares (OLS) regression.

### 2. **Panel Data Analysis (Differenced Regression)**
   - **Objective**: Address unobserved heterogeneity by differencing data across the same weeks in two consecutive years.
   - **Approach**: Incorporate week fixed effects to control for systematic temporal variation in crime trends.

### 3. **Natural Experiment**
   - **Scenario**: A temporary six-week surge in police deployment in five boroughs following the 2005 London terrorist attacks.
   - **Key Variables**:
     - `sixweeks`: Indicates weeks 80–85 (the intervention period).
     - `sixweeks_treat`: Highlights the treated boroughs during the intervention period.
   - **Objective**: Estimate the causal impact of an exogenous increase in police presence on crime rates.

### 4. **Machine Learning Models**
   - **Linear Regression**: Predicts log crime rates using features like police rate, unemployment rate, and demographic factors.
   - **Random Forest Regressor**: A robust ensemble method for predicting log crime rates with non-linear interactions.
   - **Evaluation Metrics**: Mean Squared Error (MSE) and R-squared (R²) are used to compare model performance.

---

## Data Description

- **Source**: Provided dataset `london_crime.csv` contains weekly observations across 32 boroughs over two years (3328 total observations).
- **Key Variables**:
  - `crime`: Number of crimes in a borough in a given week.
  - `police`: Police hours worked in a borough in a given week.
  - `population`: Borough population (constant over time).
  - `emp`: Labor force participation rate.
  - `un`: Unemployment rate.
  - `ymale`: Percentage of males under 25 years old.
  - `white`: Percentage of the white population.
  - `week`: Week index (1–104).
  - `borough`: Borough identifier (1–32).

---

## Repository Contents

### 1. `crime_ml_analysis.py`
- Implements the analysis with four components:
  1. **Log-log regression** to estimate initial relationships.
  2. **Differenced regression** to handle unobserved heterogeneity.
  3. **Natural experiment regression** leveraging the 2005 London attacks as an exogenous shock.
  4. **Machine learning models** (Linear Regression and Random Forest) for predictive analysis.

### 2. `london_crime.csv`
- The dataset used in the analysis, containing crime and socioeconomic data.

### 3. `README.md`
- Documentation outlining the objectives, methodologies, and findings.

---

## Instructions for Use

1. Clone this repository.
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Ensure Python 3.x and the required libraries (`pandas`, `numpy`, `statsmodels`, `scikit-learn`) are installed.

3. Run the analysis:
   ```bash
   python crime_ml_analysis.py
   ```

### Results
The script outputs:
- Regression summaries for:
  - Log-log regression.
  - Differenced regression.
  - Natural experiment regression.
- Machine learning performance metrics (MSE, R²) for Linear Regression and Random Forest models.

---

## Insights and Takeaways

- **Initial Analysis**: Cross-sectional regression indicates a positive correlation between police and crime rates, likely due to reverse causation.
- **Panel Data Analysis**: Differencing reveals a more nuanced relationship, controlling for unobserved heterogeneity.
- **Natural Experiment**: Exogenous police increases show a significant reduction in crime rates in treated boroughs, providing causal evidence for police effectiveness.
- **Machine Learning**: Models effectively predict crime rates, with Random Forest outperforming Linear Regression in capturing non-linear relationships.

---

## Author
- **Aditya Rohatgi**

---

## License
This project is licensed under the MIT License.

