# Python-netCDF
CRU Methane (CH₄) Emissions Analysis

This project analyzes global methane (CH₄) emissions using the CRU_CH4_mch4e.nc dataset from the LPJ-EOSIM dynamic global vegetation model. The dataset provides monthly methane fluxes from 1700 to 2024 at 0.5° spatial resolution (units: kg CH₄ m⁻² month⁻¹), covering 3,900 time steps across a global grid of 360 × 720 cells.

Analysis Overview

The notebook explores methane emissions through two main approaches. First, spatial plots visualize the geographic distribution of CH₄ emissions at selected time steps, highlighting regional patterns across the globe. Second, time-series plots examine both the global average and total methane emissions over the full historical record, providing insight into long-term trends and interannual variability.

Tools and Libraries

The analysis is built using Python with xarray for NetCDF data handling, matplotlib for visualization, and numpy for numerical computations.
