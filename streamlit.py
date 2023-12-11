import numpy as np
import IPython
import librosa
import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input as mobilenet_v2_preprocess_input

## Some utility functions for augmenting dataset
def noise(data):
    noise_amp = 0.04*np.random.uniform()*np.amax(data)
    data = data + noise_amp*np.random.normal(size=data.shape[0])
    return data
def stretch(data, rate=0.70):
    return librosa.effects.time_stretch(data, rate)
def shift(data):
    shift_range = int(np.random.uniform(low=-5, high = 5)*1000)
    return np.roll(data, shift_range)
def pitch(data, sampling_rate, pitch_factor=0.8):
    return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)
def higher_speed(data, speed_factor = 1.25):
    return librosa.effects.time_stretch(data, speed_factor)
def lower_speed(data, speed_factor = 0.75):
    return librosa.effects.time_stretch(data, speed_factor)

## For extracting MFCC features
def extract_features(data):
    result = np.array([])
    mfccs = librosa.feature.mfcc(y=data, sr=22050, n_mfcc=58)
    # Calculate delta and delta2 MFCCs
    delta_mfccs = librosa.feature.delta(mfccs)
    delta2_mfccs = librosa.feature.delta(mfccs, order=2)
    # Comprehensive MFCCs for better feature extraction
    comprehensive_mfccs = np.concatenate((mfccs, delta_mfccs, delta2_mfccs))
    mfccs_processed = np.mean(comprehensive_mfccs.T,axis=0)
    result = np.array(mfccs_processed)
    return result

## Get all the mfcc features as well as augmented data
def get_features(data):
    sample_rate = 22050
    res1 = extract_features(data)               #without augmentation
    result = np.array(res1)
    noise_data = noise(data)                    #noised
    res2 = extract_features(noise_data)
    result = np.vstack((result, res2))
    stretch_data = stretch(data)                #stretched
    res3 = extract_features(stretch_data)
    result = np.vstack((result, res3))
    shift_data = shift(data)                    #shifted
    res4 = extract_features(shift_data)
    result = np.vstack((result, res4))
    pitch_data = pitch(data, sample_rate)       #pitched
    res5 = extract_features(pitch_data)
    result = np.vstack((result, res5)) 
    higher_speed_data = higher_speed(data)      #speed up
    res6 = extract_features(higher_speed_data)
    result = np.vstack((result, res6))
    lower_speed_data = higher_speed(data)       #speed down
    res7 = extract_features(lower_speed_data)
    result = np.vstack((result, res7))
    return result

model = tf.keras.models.load_model("./covid_model") # load model
uploaded_file = st.file_uploader("Choose an audio.wav file", type="wav") # load file

X, features = [], []
if uploaded_file is not None:
    s , sr = librosa.core.load(uploaded_file)
    features.append(s)
    features1 = []
    for i in range(len(features)):
        features1.append(get_features(features[i]))
    ## Appending features in list X
    for i in range(len(features1)):
        for j in features1[i]:
            X.append(j)
    X = np.array(X)
    X = X.reshape(X.shape[0],1,X.shape[1])
    st.audio(uploaded_file, format='audio/ogg', start_time=0)
    # st.title(X.shape)
    Genrate_pred = st.button("Generate Prediction")
    if Genrate_pred:
        pred = model.predict(X)
        # st.title(pred)

## converting labels [1,0],[0,1] to 'yes' and 'no' respectively
preds = []
for pre in pred:
    if np.argmax(pre)==0:
        preds.append('yes')
    else: preds.append('no')

# st.title(preds)

st.title("Prediction for the voice sample is:")
st.title("YES: "+ str((preds.count('yes')/len(preds))*100)+ "%")
st.title("NO: "+ str((preds.count('no')/len(preds))*100)+ "%")