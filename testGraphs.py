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