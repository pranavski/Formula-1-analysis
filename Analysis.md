# Analysis steps and methods

# Variables for F1 Data

- **race_time** (in seconds): Total time taken to complete the race.
- **driver**: Name of the driver.
- **constructor**: Team or constructor the driver is affiliated with.
- **starting_grid_position**: Position from which the driver started the race.
- **pitstop_duration** (in seconds): Total time spent in pit stops.
- **circuit**: Name of the circuit where the race took place.
- **weather_conditions**: Weather during the race (categorical: sunny, rainy, etc.).
- **lap_times** (in seconds): Time taken for each lap.
- **driver_experience**: Years of experience of the driver.
- **team_budget**: Budget of the constructor (numerical).
- **track_type**: Type of track (categorical: street, road, oval).
- **distance_traveled** (in kilometers): Total distance of the race.

# Questions to be answered

## **Question 1: Weather Conditions and Performance (This is a supervised Learning Model)**
What is the relationship between different weather conditions (e.g., sunny, rainy) and the average race times across various circuits? Do certain drivers perform better under specific weather conditions?
### **Variables used:**
- **race_time**: Dependent variable representing overall performance.
- **weather_conditions**: Key independent variable to analyze the impact of weather on performance.
- **circuit**: To account for differences in circuit layouts and their interaction with weather.
- **driver**: To assess if specific drivers perform better under certain weather conditions.

### **Cleaning:**
- **race_time**: Checked for missing values and outliers; normalized for consistency across races.
- **weather_conditions**: Ensured consistency in categorical labels (e.g., 'rainy' vs. 'wet').
- **circuit**: Verified uniform naming conventions and matched circuits with weather data.
- Filtered incomplete data rows where weather information or race_time was missing.

### **Modeling/Computation:**
- Used Random Forest Regression to predict race_time based on weather_conditions, circuit, and other variables such as driver_experience and team_budget.
- Encoded categorical variables (e.g., weather_conditions, circuit, track_type) where necessary or allowed the model to split on them directly.
- Tuned the number of trees, maximum depth, and minimum samples per leaf using cross-validation to optimize performance.
- Analyzed feature importance to understand which variables (e.g., weather_conditions, circuit) and their interactions most influence race_time.
- Evaluated the model using Mean Absolute Error (MAE) and R-squared to ensure good performance and interpretability.

### **Graphs/Visualizations:**
- **Aggregated Heatmap**: For large datasets, a heatmap summarizing the average race times across weather conditions and circuits, aggregated over all drivers. Due to the large number of circuits and drivers with their fastest laps, an aggregated heatmap makes the most sense to use.
- **Boxplot**: A boxplot to visualize the distribution of race times across different weather conditions, highlighting median times and variability.

### **Brief discussion of why analysis is effective at answering question:**
This analysis is effective because it compares a full model (including all predictors) with models that exclude one predictor at a time. This approach allows us to observe the changes in R-squared values when specific predictors, such as weather_conditions or driver_experience, are removed. The visualizations will aid in illustrating these numeric results and highlight the relationships between the most influential predictors and the outcome (race_time).

## **Question 2: Dimensionality Reduction Impact (This is a dimensionality reduction model)**
How does applying PCA to continuous performance variables (like lap times and pitstop durations) affect the predictive accuracy of models? What insights can be gained from the mean absolute error differences between models using PCA and those using all original variables?

### **Variables used:**
- **lap_times**: Continuous performance variable to be transformed by PCA.
- **pitstop_duration**: Another continuous variable considered for dimensionality reduction.
- **race_time**: Target variable to evaluate predictive accuracy.

### **Cleaning:**
- Removed rows with missing or inconsistent values for continuous performance variables.
- Scaled continuous variables to ensure PCA components are not biased by differing units.
- Verified data integrity by confirming consistent alignment between variables (e.g., all laps and pitstop data matching race times).

### **Modeling/Computation:**
- Applied PCA to reduce dimensions of continuous variables (lap_times, pitstop_duration) and extracted principal components.
- Built two predictive models:
  - Using all original variables (no PCA).
  - Using principal components (PCA-applied variables).
- Compared the predictive accuracy (e.g., Mean Absolute Error) of both models to assess the impact of PCA.
- Evaluated variance explained by the principal components to determine how much information was retained.

### **Graphs/Visualizations:**
- **Scree Plot**: A plot showing the eigenvalues associated with each principal component to determine the number of components to retain.
- **PCA Projection Scatter Plot**: A scatter plot of the first two principal components to visualize the distribution of data points in the reduced dimensional space.

### **Brief discussion of why analysis is effective at answering question:**
PCA simplifies high-dimensional data while retaining most of the variability, which can reduce overfitting and computational complexity. Comparing MAE helps quantify the trade-off between dimensionality reduction and predictive accuracy. Visualizations, such as explained variance and heatmaps, make it clear how PCA transforms the dataset and highlights its impact on redundancy and model performance.

## **Question 3: **
### **Variables used:**
- 

### **Cleaning:**
- 

### **Modeling/Computation:**
- 

### **Graphs/Visualizations:**
- 

### **Brief discussion of why analysis is effective at answering question:**
- 

## **Question 4:**
### **Variables used:**
- 

### **Cleaning:**
- 

### **Modeling/Computation:**
- 

### **Graphs/Visualizations:**
- 

### **Brief discussion of why analysis is effective at answering question:**
- 
