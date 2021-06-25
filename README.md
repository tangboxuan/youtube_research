# YouTube API Fetcher

## Installation

### 1. Install dependencies  

1. Install pipenv (a Python package manager)  
```
pip install pipenv  
```

2. Then, in the root directory of this folder, run the following command  
```
pipenv install  
```

### 2. Set Up Google API Key  

1. Obtain a Google API Key at [this page](https://developers.google.com/maps/documentation/javascript/get-api-key) (under section titled Creating API Keys)

2. In the .env file found in the root directory, replace <YOUR_API_KEY> with your API key

## Usage

1. Enter products in the input.txt file found in the root directory, one per row. (Sample provided)

2. Run main.py using command
```
python main.py
```

The csv files can be found in the /output folder