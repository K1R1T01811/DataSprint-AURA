# DataSprint-HyperPrice
# 🚀 Fuel Price Optimization & Interactive Dashboard  

This project uses **Machine Learning (Random Forest & Linear Regression)** to analyze fuel pricing data, predict optimal prices, and evaluate business metrics such as profit.  
It also includes an **interactive dashboard** (powered by `ipywidgets` + `plotly`) for dynamic analysis of price and profit trends across zones and time blocks.  

---

## 📌 Features  

### 🔎 Data Exploration
- Displays first rows, dataset info, and summary statistics.  
- Pairplots for relationships between key factors (Fuel Price, Demand, Traffic, Distance).  
- Correlation heatmap for feature interactions.  

### 🤖 Machine Learning Models
- **Random Forest Regressor** → Predicts `PredictedPrice`.  
- **Linear Regression** → Predicts `Price`.  
- Model performance metrics:  
  - Mean Absolute Error (MAE)  
  - Mean Squared Error (MSE)  
  - R² Score  
- Business metric: **Profit calculation** from predictions.  

### 📊 Visualizations
- Pairplot (`seaborn`)  
- Correlation heatmap  
- Predicted vs Actual Prices (Random Forest)  
- Predicted Profit vs Demand  
- Zone & TimeBlock-based analysis  

### 🖥️ Interactive Dashboard
- Sliders for adjusting:  
  - Fuel Price  
  - Demand Index  
  - Traffic Index  
  - Distance (km)  
- Dropdown filters for:  
  - Zone  
  - Time Block  
- Dynamic visualizations:  
  - Price vs Distance (with regression line)  
  - Profit distribution histogram  

---

## 🛠️ Tech Stack  

- **Python 3.x**  
- **Libraries**:  
  - `pandas`, `numpy` → Data handling  
  - `matplotlib`, `seaborn`, `plotly` → Visualizations  
  - `scikit-learn` → Machine learning models  
  - `ipywidgets` → Interactive dashboard  

---


### Required Columns:
- `FuelPrice`  
- `DemandIndex`  
- `TrafficIndex`  
- `Distance_km`  
- `Price`  
- `PredictedPrice`  
- `Cost`  
- `Profit`  
- `Zone`  
- `TimeBlock`  
- `Timestamp`  

---

## ▶️ How to Run  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/fuel-price-optimization.git
   cd fuel-price-optimization
   pip install -r requirements.txt

