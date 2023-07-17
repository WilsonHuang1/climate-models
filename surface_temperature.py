import numpy as np
import cartopy.crs as ccrs
import geocat.viz as gv
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import base64
from io import BytesIO
from netCDF4 import Dataset
from plot import Plot

# INFORMATION ON TS ATTRIBUTE FOR NETCDF DATA
# filling on, default _FillValue of 9.969209968386869e+36 used, 'TS': <class 'netCDF4._netCDF4.Variable'>
# float32 TS(time, lat, lon)
#     units: K
#     long_name: Surface temperature (radiative)
#     cell_methods: time: mean
# unlimited dimensions: time
# current shape = (12, 96, 144)

class SurfaceTemperaturePlot(Plot):

    def __init__(self, months, time_periods, color="viridis", absv_diff="absv", central_longitude=0):

        # Initiate instance of super class: Plot
        super().__init__(months, time_periods, color, absv_diff, central_longitude, "Global Surface Temperature", "K", "sfc_temp_plot.pdf")


    def set_data(self):

        # get the data from the first month in the list of months
        file = f"netcdf_files_full/b.e12.B1850.T31_g37.1x.cam.h0.3000-{self.months[0]}.nc"
        self.ds = xr.open_dataset(file, decode_times=False)
        print(f"collecting data from file: {file}")
        
        try:
            # Go through each month's file and sum  precipitation values, TMQ
            for month in self.months[1:]:
                file = f"netcdf_files_full/b.e12.B1850.T31_g37.1x.cam.h0.3000-{month}.nc"
                print(f"collecting data from file: {file}")
                next_ds = xr.open_dataset(file, decode_times=False)
                self.ds.TS.values += next_ds.TS.values

            self.data = self.ds.TS
            self.ds.close()

        # AttributeError: attribute TS was not found in the file
        except AttributeError:
            print("Dataset is missing \'TS\' attribute")
            exit()

        # Another error occurred while accessing the data
        except:
            print("Something went wrong while accessing the data file")
            exit()

        # Average the values by dividing the values by the number of months
        self.data.values = (self.data.values) / len(self.months)