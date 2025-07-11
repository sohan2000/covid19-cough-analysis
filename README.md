## Project Overview

This project leverages deep learning to classify COVID-19 status based on cough and breathing sounds. The model utilizes a CNN-Bidirectional LSTM architecture and is trained on the Covid-sounds dataset provided by Cambridge University. The dataset includes audio samples from COVID-positive, negative, and other respiratory disease cases, enabling robust classification. The model has demonstrated superior performance compared to previous approaches using the same dataset.

> *COVID-19 is highly contagious, with over 29.9 million cases reported in India and 179 million cases worldwide. The rising case numbers have strained testing facilities and put lab technicians at risk. Scientists have turned to machine learning to analyze coughs, leading to the development of models that can classify cough types. This project implements a CNN-Bidirectional LSTM model using the Covid-sounds dataset, which contains both breathing and cough samples. The model processes these recordings and classifies them, outperforming other models on the same dataset.*

- **Published in:** 2022 International Conference for Advancement in Technology (ICONAT)
- **Date of Conference:** 21-22 January 2022
- **Date Added to IEEE Xplore:** 10 March 2022
- **Electronic ISBN:** 978-1-6654-2577-3
- **Print on Demand ISBN:** 978-1-6654-2578-0

### **🔗 [View Publication on IEEE Xplore](https://ieeexplore.ieee.org/document/9726067)**

## Dataset and Usage

- The dataset was provided by Cambridge University to VNRVJIET, Hyderabad, India, and is strictly for non-commercial, academic use.
- Unauthorized replication of the dataset is prohibited and may result in legal action.

## Data Preparation

### Manual Classification

- **yes:** 141 samples
- **no:** 408 samples

### Data Augmentation

- **yes_augmented_clean:** 682 samples
- **no_augmented_clean:** 524 samples

### Feature Extraction

- Audio data is converted into MFCC features:
  - **X:** 8,442
  - **Y:** 8,442 (labels: yes/no)

## Model and Code Execution

### Running the Major Project Code

- Executing the code generates the `covid_model` directory, which contains all assets, variables, and the trained model.

### Streamlit Web App

1. **Install Streamlit:**
   - Open Anaconda Prompt and run:
     ```
     pip install streamlit
     ```
2. **Run the Application:**
   - In Anaconda Prompt, execute:
     ```
     streamlit run streamlit.py
     ```

## User Prediction Steps

1. Upload an audio file using the "Browse files" button.
2. Click "Generate Prediction."
3. View your prediction results.
