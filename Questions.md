# Analysis Questions

This document outlines the variables and questions related to Formula 1 (F1) data analysis. It serves as a guide for understanding the key metrics and inquiries that can be explored within the dataset.

# Variables for F1 Data

- **race_time (in seconds)**: Total time taken to complete the race.
- **driver**: Name of the driver.
- **constructor**: Team or constructor the driver is affiliated with.
- **starting_grid_position**: Position from which the driver started the race.
- **pitstop_duration (in seconds)**: Total time spent in pit stops.
- **circuit**: Name of the circuit where the race took place.
- **weather_conditions**: Weather during the race (categorical: sunny, rainy, etc.).
- **lap_times (in seconds)**: Time taken for each lap.
- **driver_experience**: Years of experience of the driver.
- **team_budget**: Budget of the constructor (numerical).
- **track_type**: Type of track (categorical: street, road, oval).
- **distance_traveled (in kilometers)**: Total distance of the race.

# Questions About F1 Data

## 1. **Impact of Constructor on Race Time:**
   - How does the constructor affiliation of a driver influence their race time? Are there specific constructors that consistently produce faster race times compared to others?

## 2. **Weather Conditions and Performance:**
   - What is the relationship between different weather conditions (e.g., sunny, rainy) and the average race times across various circuits? Do certain drivers perform better under specific weather conditions?

## 3. **Starting Grid Position Analysis:**
   - How does a driver's starting grid position correlate with their final race time? Is there a specific range of starting positions that significantly increases the likelihood of achieving a top finish?

## 4. **Variance in Lap Times by Circuit Type:**
   - Which types of circuits (e.g., street, road, oval) exhibit the smallest variance in lap times? What characteristics of these circuits contribute to this consistency in performance?

## 5. **Clustering of Driver Performance:**
   - When clustering drivers based on lap times, pitstop durations, and race outcomes, what distinct performance groups emerge? What traits define these clusters, and how can they inform team strategies?

## 6. **Dimensionality Reduction Impact:**
   - How does applying PCA to continuous performance variables (like lap times and pitstop durations) affect the predictive accuracy of models? What insights can be gained from the mean absolute error differences between models using PCA and those using all original variables?

## 7. **Driver Experience and Race Outcomes:**
   - Is there a significant relationship between a driver's years of experience and their race performance metrics (e.g., race time, lap times)? How does this relationship vary across different constructors or circuits?

## 8. **Impact of Team Budget on Performance:**
   - How does the budget of a constructor influence the performance of their drivers? Are there thresholds of budget that correlate with significantly better race outcomes?

## 9. **Effect of Circuit Characteristics on Lap Times:**
   - What specific characteristics of a circuit (e.g., length, number of turns, elevation changes) have the most significant impact on lap times? How do these factors vary across different types of circuits?

## 10. **Analysis of Pitstop Strategies:**
    - How do different pitstop strategies (e.g., number of stops, timing of stops) affect overall race time? Are there optimal strategies that lead to better performance based on race conditions or circuit types?

## **More Questions to come as analysis progresses**

