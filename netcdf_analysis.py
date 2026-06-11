import matplotlib.pyplot as plt
import xarray as xr

ds = xr.open_dataset('CRU_CH4_mch4e.nc')

fig, ax = plt.subplots(figsize=(13, 6))
ds['mch4e'].isel(time=-1).plot(ax=ax)

ax.set_title('CH4 Emissions (kg/m2/s) - 2024')

plt.show()