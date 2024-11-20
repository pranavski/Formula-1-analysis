import pandas as pd
from plotnine import *
import numpy as np

# Graph 1: Aggregated Heatmap
# Example data including driver performance
data = pd.DataFrame({
    'Race_Track': ['Track A', 'Track A', 'Track A', 'Track B', 'Track B', 'Track B', 
                   'Track C', 'Track C', 'Track C'],
    'Weather_Condition': ['Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Rainy', 'Cloudy', 
                           'Sunny', 'Rainy', 'Cloudy'],
    'Driver': ['Driver 1', 'Driver 1', 'Driver 1', 'Driver 2', 'Driver 2', 'Driver 2',
               'Driver 3', 'Driver 3', 'Driver 3'],
    'Average_Race_Time': [120.5, 130.2, 125.8, 118.3, 135.0, 128.9, 125.8, 140.4, 130.2]  # in seconds
})

# Create the plot using ggplot syntax
plot = (
    ggplot(data, aes(x='Race_Track', y='Weather_Condition', fill='Average_Race_Time')) +
    geom_tile() +
    geom_text(aes(label=round(data['Average_Race_Time'], 1)), format_string='{:.1f}') +
    scale_fill_gradient(low='#ffffd9', high='#081d58', name='Avg Race Time (s)') +
    facet_wrap('~ Driver', ncol=1, scales='free_y') +
    theme_minimal() +
    theme(
        figure_size=(10, 15),
        axis_text_x=element_text(rotation=0),
        panel_spacing=0.01
    ) +
    labs(
        x='Race Track',
        y='Weather Condition',
        title='Race Performance by Driver'
    )
)

# Display the plot
plot

## Graph 2: Boxplot
import pandas as pd
from plotnine import ggplot, aes, geom_boxplot, labs, theme_minimal

# Sample data for weather conditions and race times
data = pd.DataFrame({
    'Weather_Condition': ['Sunny', 'Sunny', 'Rainy', 'Rainy', 'Cloudy', 'Cloudy', 'Sunny', 'Rainy', 'Cloudy'],
    'Race_Time': [120.5, 118.3, 130.2, 135.0, 125.8, 128.9, 122.0, 132.0, 127.5],  # in seconds
    'Driver': ['Driver 1', 'Driver 2', 'Driver 1', 'Driver 2', 'Driver 1', 'Driver 2', 'Driver 3', 'Driver 3', 'Driver 3']
})

# Create the box plot
box_plot = (
    ggplot(data, aes(x='Weather_Condition', y='Race_Time')) +
    geom_boxplot(fill="skyblue", color="black") +
    labs(
        title="Distribution of Race Times by Weather Condition",
        x="Weather Condition",
        y="Race Time (seconds)"
    ) +
    theme_minimal()
)

# Display the plot
box_plot

# Question 2: How does applying PCA to continuous performance variables (like lap times and pitstop durations) affect the predictive accuracy of models? What insights can be gained from the mean absolute error differences between models using PCA and those using all original variables?
# Graph 1: Scree plot
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from plotnine import ggplot, aes, geom_line, geom_point, labs, theme_minimal
import pandas as pd

# Sample data
data = pd.DataFrame({
    'lap_time_1': [100, 102, 98, 101, 97],
    'lap_time_2': [102, 99, 100, 98, 96],
    'pitstop_duration': [10, 12, 11, 13, 10]
})

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Apply PCA
pca = PCA()
pca.fit(data_scaled)
explained_variance = pca.explained_variance_ratio_ * 100  # Convert to percentage

# Create a DataFrame for plotting
scree_data = pd.DataFrame({
    'Principal Component': [f'PC{i+1}' for i in range(len(explained_variance))],
    'Explained Variance (%)': explained_variance
})

# Scree plot
scree_plot = (
    ggplot(scree_data, aes(x='Principal Component', y='Explained Variance (%)')) +
    geom_line(group=1, color="blue") +
    geom_point(size=2, color="red") +
    labs(
        title="Scree Plot: Explained Variance by Principal Components",
        x="Principal Component",
        y="Explained Variance (%)"
    ) +
    theme_minimal()
)

scree_plot

# Graph 2: PCA Projection Scatter Plot
from plotnine import ggplot, aes, geom_point, labs, theme_minimal
import numpy as np

# Transform data using the first two principal components
pca_data = pca.transform(data_scaled)
pca_df = pd.DataFrame({
    'PC1': pca_data[:, 0],
    'PC2': pca_data[:, 1],
    'Category': ['Driver 1', 'Driver 2', 'Driver 3', 'Driver 4', 'Driver 5']  # Example labels
})

# PCA projection scatter plot
pca_scatter_plot = (
    ggplot(pca_df, aes(x='PC1', y='PC2', color='Category')) +
    geom_point(size=3) +
    labs(
        title="PCA Projection Scatter Plot",
        x="Principal Component 1",
        y="Principal Component 2"
    ) +
    theme_minimal()
)

pca_scatter_plot

# Question 3:
# Graph 1:

# Graph 2:

# Question 4:
# Graph 1:

# Graph 2: