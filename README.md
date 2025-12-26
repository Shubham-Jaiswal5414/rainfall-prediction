# Rainfall Prediction System

A machine learning-based Streamlit application that predicts rainfall patterns across different Indian states using synthetic weather data.

## 🌧️ Features

- **Multi-State Support**: Predictions for 8 Indian states
  - Maharashtra
  - Kerala
  - Tamil Nadu
  - Rajasthan
  - Punjab
  - Karnataka
  - Uttar Pradesh
  - West Bengal

- **Monthly Predictions**: Data for all 12 months of the year

- **Weather Parameters**: Considers multiple factors
  - Temperature (°C)
  - Humidity (%)
  - Wind Speed (km/h)
  - Month
  - State

- **Machine Learning Model**: Uses Linear Regression for accurate predictions

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shubham-Jaiswal5414/rainfall-prediction.git
   cd rainfall-prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Running the Application

Start the Streamlit app:
```bash
streamlit run rain.py
```

The app will open in your browser at `http://localhost:8501`

## 📈 How It Works

1. **Data Generation**: Synthetic rainfall data is generated based on realistic patterns
   - **Monsoon Season (Jun-Sep)**: High rainfall
   - **Summer (Mar-May)**: Moderate rainfall
   - **Winter (Dec-Feb)**: Low rainfall

2. **State-Specific Patterns**: Each state has unique rainfall characteristics
   - Kerala: Highest rainfall (1.8x multiplier)
   - Rajasthan: Lowest rainfall (0.4x multiplier)

3. **Model Training**: Linear Regression model trained on 480 data points (8 states × 12 months × 5 variations)

4. **Prediction**: Input weather parameters to predict rainfall in millimeters

## 🎯 Usage

1. Select a **State** from the dropdown
2. Choose a **Month**
3. Adjust **Temperature**, **Humidity**, and **Wind Speed** using sliders
4. Click **"Predict"** button
5. View the predicted rainfall in mm

## 📁 Project Structure

```
rainfall-prediction/
├── rain.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore configuration
└── .streamlit/
    └── config.toml        # Streamlit configuration
```

## 📦 Dependencies

- **streamlit** (1.52.2): Web framework for data apps
- **pandas** (2.3.3): Data manipulation and analysis
- **scikit-learn** (1.8.0): Machine learning library
- **numpy** (2.4.0): Numerical computing

See `requirements.txt` for complete list.

## 🌐 Deployment

This app is ready to be deployed on **Streamlit Cloud** for free:

1. Push the repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy the `rainfall-prediction` repository

## 📊 Dataset Information

- **Total Records**: 480 (8 states × 12 months × 5 daily variations)
- **Features**: State, Month, Temperature, Humidity, Wind Speed
- **Target**: Rainfall (mm)
- **Data Type**: Synthetic (generated based on realistic patterns)

## 🔬 Model Performance

- **Algorithm**: Linear Regression
- **Features**: 19 (after one-hot encoding)
- **Training Data**: 480 samples

## 💡 Future Enhancements

- [ ] Add actual historical weather data
- [ ] Implement more advanced ML models (Random Forest, XGBoost)
- [ ] Add seasonal trend analysis
- [ ] Include weather forecast integration
- [ ] Add data visualization charts
- [ ] Implement model evaluation metrics

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Shubham Jaiswal**
- GitHub: [@Shubham-Jaiswal5414](https://github.com/Shubham-Jaiswal5414)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For questions or suggestions, feel free to reach out!

---

**Happy Predicting!** 🌦️
