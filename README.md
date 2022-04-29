# Richter's Predictor: Modeling Earthquake Damage
This project is a part of the [Data Science Retreat](https://datascienceretreat.com) mini competition. 

Richter's Predictor: Modeling Earthquake Damage Challenge hosted by DRIVENDATA. 

#### -- Project Status: [Active]

## Project Intro/Objective

Based on aspects of building location and construction, our goal is to predict the level of damage to buildings caused by the 2015 Gorkha earthquake in Nepal.

The data was collected through surveys by Kathmandu Living Labs and the Central Bureau of Statistics, which works under the National Planning Commission Secretariat of Nepal. This survey is one of the largest post-disaster datasets ever collected, containing valuable information on earthquake impacts, household conditions, and socio-economic-demographic statistics.


## Needs of this project

- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting


### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* etc.

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [lightgbm](https://lightgbm.readthedocs.io/en/latest/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. 


## Getting Started

1. Clone this repo 
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.    
3. Data processing/transformation scripts are being kept [here]

4. In a terminal or command window, navigate to the top-level project directory `richters_predictor/` (that contains this README) and run one of the following commands:

    * Create a new environment.
    ```bash
    conda create -n minicomp python=3.9
    ```  
    ```bash
    conda activate minicomp
    ``` 
    ```bash
    pip install ipykernel
    ```
    ```bash
    python -m ipykernel install --user --name minicomp --display-name "minicomp_kernel"
    ```
    
    * Install the required package.  
    ```bash 
    pip3 install -r requirements.txt
    ```

    * Open jupyter notebook 
    ```bash
    jupyter notebook richters_predictor.ipynb
    ```
   
### Data

There are 39 columns in this dataset, where the building_id column is a unique and random identifier. The remaining 38 features are described in [Data Driven](https://www.drivendata.org/competitions/57/nepal-earthquake/page/136/). 



## License 
This project is licensed under MIT License - see the <a href="LICENSE">LICENSE</a> file for details.



## Contact
E-mail: msak1612@gmail.com
