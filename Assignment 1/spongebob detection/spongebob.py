import streamlit as st
import numpy as np
import cv2

hue_range = {
    "Spongebob": {
        "lower": 20,
        "higher": 30
    }
}

uploaded_file = st.sidebar.file_uploader("Upload an image:")

if uploaded_file is not None:
    
    #convert string data to numpy array
    npimg = np.fromstring(uploaded_file.getvalue(), np.uint8)
    # convert numpy array to image
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR) #reads as BGR by default

    # Switch to HSV for simplier color handling.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    for object_name in hue_range.keys():
    # Set lower and high hue for mask filtering
        lower_h = hue_range[object_name]["lower"]
        upper_h = hue_range[object_name]["higher"]
    
    # Create the mask.
    mask = cv2.inRange(hsv, (lower_h,100,100), (upper_h,255,255))
    
    