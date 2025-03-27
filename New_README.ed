# Climate Models Visualization Application Guide

This guide will help you understand and use the climate model visualization web application. The application allows you to generate various visualizations of climate data, including temperatures, precipitation patterns, and comparative analyses.

## Getting Started

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bsepaul/climate-models.git
   cd climate-models
   ```

2. **Set up the environment**:
   - Using a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows: env\Scripts\activate
     pip install -r requirements.txt
     ```
   - Alternatively, if you have Nix package manager:
     ```bash
     nix develop
     ```

3. **Run the application**:
   ```bash
   python webapp.py
   ```
   
   The application will start on http://localhost:5000

### Required Data Files

The application expects climate model data in NetCDF format stored in a `netcdf_files` directory. The application specifically looks for:
- `netcdf_files/test_data_4000-4050.nc`

## Using the Visualization Interface

The interface allows you to create visualizations through a series of selection steps:

1. **Select Variable**:
   - Temperature
   - Precipitation

2. **Select Plot Type** (depends on variable chosen):
   - For Temperature:
     - Surface Map
     - Elevation Map
     - Longitudinal Average
     - Monthly Average
     - Time Series
   - For Precipitation:
     - Rate Map
     - Monthly Average
     - Time Series

3. **Select Analysis Type**:
   - Single Time Period
   - Difference of Time Periods

4. **Select Time Period**:
   - Choose from available model years (4000-4010, 4010-4020, etc.)
   - For difference plots, select two time periods to compare

5. **Select Color Scheme**:
   - Choose from various color palettes for visualization

6. **Additional Parameters** (depending on plot type):
   - Elevation level (for elevation maps)
   - Months to include in analysis
   - Geographic region (latitude/longitude bounds)
   - Standard deviation range for color scaling
   - Toggle percentage change display for difference plots

7. **Create Model** to generate the visualization

## Types of Visualizations

### Surface Temperature Maps
Displays temperature distribution across the globe or a specified region for selected months and time periods.

### Elevation Temperature Maps
Shows temperature patterns at specific atmospheric levels, allowing analysis of temperature distribution at different altitudes.

### Longitudinal Average Plots
Displays temperature variation across latitudes, averaging data along longitudes to show zonal temperature patterns.

### Monthly Average Plots
Shows how temperature or precipitation varies by month, averaged over a selected region and time period.

### Time Series
Displays temporal evolution of temperature or precipitation over the entire model time range for a selected region.

### Difference Plots
Compares two time periods to visualize changes in temperature or precipitation patterns, with optional percentage change display.

## Modifying the Application

### Adding New Plot Types

To add a new plot type:

1. Create a new class that inherits from the `Plot` base class in a new Python file
2. Implement the required methods:
   - `__init__` for initialization
   - `get_time_period_data` for data extraction
   - `make_fig` for visualization creation

3. Update the UI by modifying:
   - `website/templates/base.html` to add the option in the interface
   - `website/static/script.js` to handle the new plot type in the UI logic
   - `website/render.py` to include the new plot type in the rendering process

Example structure for a new plot type:

```python
from plot import Plot
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np

class NewPlotType(Plot):
    def __init__(self, months, time_periods, color="viridis", 
                min_longitude=-180, max_longitude=180, 
                min_latitude=-90, max_latitude=90, 
                central_longitude=0, num_std_dev=2):
        
        super().__init__(
            months=months,
            time_periods=time_periods,
            color=color,
            min_longitude=min_longitude,
            max_longitude=max_longitude,
            min_latitude=min_latitude,
            max_latitude=max_latitude,
            central_longitude=central_longitude,
            num_std_dev=num_std_dev,
            title="Your New Plot Title",
            label="Y-axis Label",
            file_name="new_plot_type.pdf"
        )
        
    def get_time_period_data(self, time_period):
        # Implement data extraction and processing
        # Return processed data
        
    def make_fig(self):
        # Implement visualization creation
        # Set self.fig to the created figure
```

### Adding Support for Additional Data Variables

To add a new climate variable:

1. Identify the variable in your NetCDF data files
2. Create appropriate plot classes for the variable
3. Update the UI to include the new variable option
4. Modify the `render.py` file to handle the new variable

### Customizing the UI

The UI is built with:
- HTML templates in `website/templates/`
- CSS in `website/static/styles.css`
- JavaScript in `website/static/script.js`

Modify these files to change the appearance and behavior of the interface.

## Output and Export Options

The application provides several output options:

- Interactive visualizations in the browser
- Download as PDF
- For monthly average plots, download data as CSV files

## Troubleshooting

Common issues:

1. **Missing data files**: Ensure the NetCDF files are properly placed in the `netcdf_files` directory
2. **Dependency errors**: Check that all requirements are installed
3. **Plot generation failures**: Check the console logs for error details

## Data Structure

The application expects NetCDF files with the following variables:
- `TS`: Surface temperature
- `T`: Temperature at different elevation levels
- `PRECC`: Convective precipitation rate
- `PRECL`: Large-scale precipitation rate

Variables should have dimensions:
- `time`: Temporal dimension
- `lat`: Latitude
- `lon`: Longitude
- `lev`: Elevation levels (for 3D variables)