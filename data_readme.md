## Data

We publish the breathing and cough samples we used in our KDD paper here. It contains 459 cough and breathe samples from 378 users (from Web and Android applications until 22 May, 2020). We have carefully checked samples to guarantee the quality of the data. We have collected voice, symptoms and other metadata, but at this stage we only share cough and breathing as we used in KDD paper.

Since we have two applications to collect the data, we use 'web' and 'android' to distinguish them.

Also, in the name format, 'nocough' and 'withcough' indicate whether the user reported a cough (whether dry or wet) symptom, while 'nosymp' means the user had no symptoms at that time.

### Usage: 

1. For **task1**, we use covidandroidnocough + covidandroidwithcough + covidwebnosympcough + covidwebwithcough  v.s.  healthyandroidnosymp + healthywebnosymp  ( 62 user (141 sample) / 220 users (298 samples) in total);
2. For **task2**, we use covidandroidwithcough  + covidwebwithcough  v.s.   healthyandroidwithcough  + healthywebwithcough ( 23 user (54 sample) / 29 users (32 samples) in total);
3. For **task3**, we use covidandroidwithcough  + covidwebwithcough  v.s.   asthmaandroidwithcough  + asthmawebwithcough ( 23 user (54 sample) / 18 users (20 samples) in total);

### Other:

1. Augmentation：augmented data for task2 and task3 are also provided in health* and asthma* files;
2. Multimodal: to combine cough with breathing, we also give a mapping dictionary with breathing file as key and cough as  value. Please refer to 'andriod_breath2cough.json';

