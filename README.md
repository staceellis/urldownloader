# Title

urldownloader

## Requirements

1. Install Anaconda [Conda environment](https://anaconda.org/). 


### Windows installation 

1. To use `urldownloader` create a [Conda environment](https://anaconda.org/)


2. Open Anaconda Prompt and **Change directory** / Navigate to location of **urldownloader** directory
	```commandline
	cd C:\Users\User\scripts\url_downloader
	```

3. Create a conda environment or virtualenv and activate environment
	```commandline
	conda env create -f environment.yml
	conda activate urldownloader
	```
   
### Usage Examples
1. Open Command Line (Anaconda Prompt) **Change directory** to project location, activate environment.
	```commandline
	cd C:\Users\User\scripts\url_downloader
	conda activate urldownloader
	```

3. Run script via CLI (DESTINATION = image output directory, .CSV = .csv file containing url column).
	```commandline
	python CLI.py [DESTINATION] [.CSV]
	```
	e.g
	```commandline
	python CLI.py "C:\Users\user\Desktop\Images" "C:\Users\user\Desktop\URLs.csv"



