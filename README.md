# 2DOceanVectorPlotter
Plotting a 2D vector which displays ocean current directions using matplotlib.pyplot. Currents are plotted at a certain depth only. Dataset was downloaded from the ROMS Real Time Forecasting website. The file were formatted in a .nc file type.
To change the depth simply change the array index on depth = depths[]
Change m, n to use more or less data.
Expand image for a higher res image.

For the .py (Python file) change the data address to where ever your nc file is located at.

Run the roms_ncst_download.sh or roms_fcst_download.sh to download all the nc files from the roms website

Sample nc file was uploaded.
See results for results.


Requirements:
NetCDF4
Numpy 
Matplotlib.pyplot 



Large Scale Diagram:
![2DVectorPlotLargeScale](https://user-images.githubusercontent.com/68083724/159191116-1282e7cb-a351-4538-9d2c-acd21767fb95.png)

Small Scale Diagram:
![2DVectorPlotSmallScale](https://user-images.githubusercontent.com/68083724/159191373-04588ee6-2f42-4244-8840-6ad75485f00f.png)

3D surface Plot
![fig1 (6)](https://user-images.githubusercontent.com/68083724/162594689-1ca9b3fc-0715-480d-a89f-a1403f7db502.png)


3D Wireframe
![fig1 (5)](https://user-images.githubusercontent.com/68083724/162594687-63318023-0346-48cc-961a-d159ec573cc3.png)
