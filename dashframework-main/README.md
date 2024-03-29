# Group 34 Source Code

## About this app

Everything is developed using python programming language. The data needed can be found in the github repository and in the google drive link below.

## Requirements

* Python 3 (add it to your path (system variables) to make sure you can access it from the command prompt)
* Git (https://github.com/Bilal-B00/visualization/)
* Pandas 
* Numpy
* Dash
* Plotly
* GeoJSON and TopoJSON versions of UK Boundary Data

## How to run this app

We suggest you to create a virtual environment for running this app with Python 3. Clone this repository 
and open your terminal/command prompt in the root folder. Open the app.py file and run the file. The link that pops up when running the code should be copied into your browser (preferably Google Chrome). The link should show the Visualization tool. The datasets (map.csv and data.csv) are needed for the project. Map.csv can be found in this github repository. Data.csv can be found here: https://drive.google.com/file/d/16RB-uyc-jRGqEqSNMVA2mEjdY0f5-e2n/view?usp=sharing. Data.csv should be placed into the dashframework-main folder.


open the command prompt
cd into the folder where you want to save the files and run the following commands. To get the HTTPS link, press the clone button in the right top corner and then copy the link under "Clone with HTTPS". 

```
> git clone <HTTPS link>
> cd <folder name on your computer>
> python -m venv venv

```
If python is not recognized use python3 instead

In Windows: 

```
> venv\Scripts\activate

```
In Unix system:
```
> source venv/bin/activate
```

Install all required packages by running:
```
> pip install -r requirements.txt
```

Run this app locally with:
```
> python app.py
```
You will get a http link, open this in your browser to see the results. You can edit the code in any editor (e.g. Visual Studio Code) and if you save it you will see the results in the browser.

## Resources

* [Dash](https://dash.plot.ly/)
* Python 3 (add it to your path (system variables) to make sure you can access it from the command prompt)
* Git (https://github.com/Bilal-B00/visualization/)
* Pandas
* Numpy
* Plotly
* [GeoJSON and TopoJSON versions of UK Boundary Data](https://martinjc.github.io/UK-GeoJSON/)

