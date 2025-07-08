# python-project
Zomato Data Analysis
# 🍽️ Zomato Restaurant Data Analysis | End-to-End Python EDA Project

## 📌 Project Title
**Zomato Restaurant Data Analysis**  
**Tools Used**: Python, Pandas, Matplotlib, Seaborn, NumPy  
**Project Type**: Exploratory Data Analysis (EDA) | Data Cleaning | Data Visualization  
**GitHub Repository**: [Insert Link Here]

---

## 🎯 Objective

To explore Zomato restaurant data to uncover meaningful business insights and customer behavior patterns using Python and visualization libraries.

---

## ✅ Step-by-Step Implementation

### 1. Data Cleaning
- Identified and handled missing values in critical columns (`rate`, `votes`, `cost`)
- Cleaned the `rate` column (converted "4.2/5" to float, removed "NEW", "-")
- Cleaned the `approx_cost(for two people)` column by removing commas and converting to integers

### 2. Exploratory Data Analysis (EDA)

#### ⭐ Distribution of Ratings
- Majority of ratings fall between **3.5 and 4.5**
- Slight **left skew**, indicating more positive reviews

#### 🍽️ Restaurant Type Analysis
- **Delivery** is the most common restaurant type
- **Buffet** and **Cafes** tend to have higher average ratings and cost more
- **Dining** and **Quick Bites** are more affordable

#### 📦 Impact of Online Ordering & Table Booking
- Restaurants with **online ordering** have:
  - Higher average rating (3.86 vs 3.49)
  - About 7x more votes than those without
- Restaurants with **table booking** have:
  - Higher ratings (4.19 vs 3.60)
  - About 4x more votes

### 3. Cost Analysis
- Average cost for two people ≈ ₹XXX (based on dataset)
- **Buffets** and **Cafes** are more expensive on average
- Cost and rating show weak positive correlation (**0.27**)

### 4. Votes vs Ratings
- Moderate positive correlation (**0.49**) between votes and ratings
- More votes generally indicate better customer reception

### 5. Correlation Matrix
- `votes` vs `rate`: **0.49**
- `cost` vs `rate`: **0.27**
- `votes` vs `cost`: **0.32**
- Correlation heatmap created to visualize relationships

### 6. Data Visualizations
- Histogram with KDE: Rating distribution
- Bar charts: Top restaurant types, average cost, and ratings
- Scatter plots: 
  - Rating vs Cost
  - Votes vs Cost
- Heatmap for correlation between `rate`, `votes`, and `cost`

### 7. Top Restaurant Insights
- Extracted **Top 10 Highest-Rated** and **Top 10 Most-Voted** restaurants
- Compared average cost and popularity
- Identified trends among premium and popular venues

---

## 🧠 Key Takeaways
- Online ordering and table booking options improve both popularity and perceived service quality
- Cost is not a strong predictor of rating but has mild influence on votes
- High vote count correlates with good ratings, but not all popular restaurants are top-rated

---

## 📂 Deliverables
- Cleaned and structured dataset
- Insightful visualizations and charts
- Correlation heatmap
- Actionable business insights

---

## 📣 Open to Analyst Roles

I'm seeking opportunities to apply my skills in **data cleaning**, **EDA**, **business analysis**, and **data visualization** to solve real-world problems and guide strategic decisions.

---

### 🏷️ Tags:
#Python #Pandas #DataAnalytics #EDA #ZomatoEDA #Seaborn #DataCleaning #RestaurantTrends #BusinessInsights #DataVisualization #AnalystRole #GitHubProjects #JupyterNotebook
