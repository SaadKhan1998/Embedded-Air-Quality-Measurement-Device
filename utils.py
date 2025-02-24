# utils.py - Utility functions for data processing

import numpy as np
from matplotlib import pyplot as plt

def filter_list(lst):
    """Remove None values and convert to integers."""
    return list(map(int, filter(lambda x: x is not None, lst)))

def scale_list(temp_list):
    """Scale values to fit within LED display range."""
    max_value = max(temp_list) if temp_list else 1
    return [int((i / max_value) * 6) for i in temp_list]

def list_compression(lst, num_points=8):
    """Compress list into defined number of points for visualization."""
    segment_length = max(1, len(lst) // num_points)
    return scale_list([
        int(round(sum(lst[i * segment_length:(i + 1) * segment_length]) / segment_length))
        for i in range(num_points)
    ])

def show_plots(pm1, pm25, pm10, temp, humidity):
    """Plot sensor data trends."""
    plt.figure(figsize=(10, 15))
    plt.subplots_adjust(hspace=0.5)
    
    def plot_data(y_data, title, color):
        x_axis = range(len(y_data))
        plt.plot(x_axis, y_data, color)
        plt.axhline(np.mean(y_data), linestyle=':', color=color[0])
        plt.xlabel('Sample')
        plt.ylabel('Value')
        plt.title(title)
    
    plt.subplot(5, 1, 1)
    plot_data(pm1, 'PM1.0', 'rd-')
    plt.subplot(5, 1, 2)
    plot_data(pm25, 'PM2.5', 'ko-')
    plt.subplot(5, 1, 3)
    plot_data(pm10, 'PM10.0', 'bo-')
    plt.subplot(5, 1, 4)
    plot_data(temp, 'Temperature', 'ro-')
    plt.subplot(5, 1, 5)
    plot_data(humidity, 'Humidity', 'go-')
    plt.show()


