# 📘 **AICTE Edunet Green-Skill Internship: Supply Chain GHG Emissions Analysis**  
_Tracking, Cleaning, and Visualizing US Industry GHG Emissions_ 🌱🌍

![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)
![Pandas](https://img.shields.io/badge/pandas-2.0+-orange)
![Seaborn](https://img.shields.io/badge/seaborn-0.12+-blue)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.7+-purple)

---

## 🧾 Project Overview

> **Goal:**  
> Analyze and visualize supply chain greenhouse gas (GHG) emissions across US industries using open data and Python tools.  
> This 4-week internship project focuses on data cleaning, exploratory analysis, modeling, and reporting to support green skills and sustainability.  
>  
> **Duration:** _4 Weeks_  
> **Tech Stack:** Python, Pandas, Seaborn, Matplotlib, Jupyter Notebook

---

## 📅 Weekly Progress Tracker

| Week      | Status      | Description                                      |
|-----------|------------|--------------------------------------------------|
| **Week 1** | ✅ Completed | Data cleaning, EDA, and basic visualization      |
| **Week 2** | ⏳ In progress | Model selection and training                     |
| **Week 3** | ❌ Not started | Advanced analytics, dashboard, and reporting      |
| **Week 4** | ❌ Not started | Final review, documentation, and deployment      |

**Progress Bar:**  
`[■■■■□□□□] 2/4 weeks completed`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/)
- Jupyter Notebook

### Installation

```bash
git clone https://github.com/yourusername/green-skill-internship.git
cd green-skill-internship
pip install -r requirements.txt
```

### Setup Instructions

1. **Open the project folder in VS Code or your favorite IDE.**
2. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```
3. **Open `Week1_GHG/Week1_GHG.ipynb` and run the cells.**

---

## 📊 Features Implemented

### Basic Features
- 📥 Load and preview US supply chain GHG emissions dataset
- 🧹 Data cleaning: handle missing values, drop duplicates, remove unused columns
- 📋 List and inspect column names and data types
- 📊 Basic visualizations: bar charts, histograms

### Advanced Features
- 🔍 Top 10 industries by emission factors
- 📈 Distribution analysis of emission values
- 🏷️ Data quality scoring and filtering (planned)
- 🛠️ Modular notebook for easy extension

---

## 🛠️ Usage Instructions

### Run the Analysis

```python
import pandas as pd
data_set = pd.read_csv('Week1_GHG/SupplyChainEmission.csv')
data_set.head()
```

### Data Cleaning Example

```python
data_set.dropna(subset=["Supply Chain Emission Factors with Margins"], inplace=True)
data_set.drop_duplicates(inplace=True)
data_set = data_set.drop(columns=['Unnamed: 7'])
```

### Visualization Example

```python
import seaborn as sns
import matplotlib.pyplot as plt

top_10 = data_set.sort_values(by="Supply Chain Emission Factors with Margins", ascending=False).head(10)
plt.figure(figsize=(12,7))
sns.barplot(data=top_10, x='Industry Name', y='Supply Chain Emission Factors with Margins', color='grey')
plt.title('Top 10 Industries by Emissions')
plt.xticks(rotation=40)
plt.show()
```

> **Note:** For advanced analysis, modify the notebook to filter by year, substance, or reliability scores.

---

## 📂 Project Structure

```
AICTE Edunet Green-Skill Internship/
│
├── Week1_GHG/
│   ├── SupplyChainEmission.csv   # Main dataset
│   └── Week1_GHG.ipynb          # Jupyter notebook for analysis
├── Readme.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── ...
```
- **Week1_GHG/**: Contains all data and analysis notebooks.
- **Readme.md**: This file.
- **requirements.txt**: List of required Python packages.

---

## 🧪 Testing

To run basic tests:

```bash
pytest
```

Or, for notebook cell validation:

```python
# In a notebook cell
assert not data_set.isnull().any().any(), "Dataset contains null values!"
```

---

## 📌 Upcoming Work

| Week      | Planned Tasks                                      | Status      |
|-----------|----------------------------------------------------|-------------|
| **Week 2** | Model selection, training, and evaluation          | ⏳ In progress |
| **Week 3** | Advanced analytics, dashboard, and reporting       | ❌ Not started |
| **Week 4** | Final review, documentation, and deployment        | ❌ Not started |

---

## 📸 Screenshots / Demo

![Demo Placeholder](https://via.placeholder.com/800x400?text=Demo+Screenshot)

> _Replace with your own screenshots for better presentation!_

---

## 🤝 Contribution

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 🧾 License and Credits

This project is licensed under the MIT License.  
See [LICENSE](LICENSE) for details.

**Credits:**  
- [AICTE Edunet](https://www.aicte-india.org/)
- US Supply Chain Emission Dataset

---

> 📍 **This README will be updated weekly with progress logs and new instructions as the project