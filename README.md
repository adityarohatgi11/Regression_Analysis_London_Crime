This repository contains a Python-based statistical analysis of the relationship between police deployment and crime rates in London's boroughs, inspired by the paper *"Panic on the Streets of London: Police, Crime, and the July 2005 Terror Attacks"* by Draca, Machin, and Witt (AER, 2011). The analysis explores the effectiveness of police as a crime deterrent using econometric methodologies.

---

## Project Overview

The analysis investigates the impact of police deployment on crime rates using weekly panel data from 32 boroughs in London over two years. The dataset includes variables such as crime, police hours, population, unemployment rate, labor force participation, demographic breakdowns, and more. The primary goal is to estimate the causal effect of police presence on crime rates while addressing challenges such as reverse causation and unobserved heterogeneity.

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

### 1. `london_crime_reg.py`
- Implements the analysis with three parts:
  1. **Log-log regression** to estimate initial relationships.
  2. **Differenced regression** to handle unobserved heterogeneity.
  3. **Natural experiment regression** leveraging the 2005 London attacks as an exogenous shock.

### 2. `london_crime.csv`
- The dataset used in the analysis, containing crime and socioeconomic data.

### 3. `a_londoncrime_2024.docx`
- Assignment documentation outlining the objectives and methodologies.

---

## Instructions for Use

1. Clone this repository.
   ```bash
   git clone <repository-url>
   cd <repository-name>
