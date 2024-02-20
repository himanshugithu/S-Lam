import cv2
# import time
import oneM2Mget
from Speak import text_to_speech
from getLUX import calculate_luminance
from faceDistance import getDistance
from gui import *
speech_played = False

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()                      # Capture frame-by-frame
    if not ret:
        print("Error: Failed to capture frame.")
        break
    luminance = calculate_luminance(frame)       # Calculate luminance from the captured frame
    distance = getDistance(frame) 
    temp = oneM2Mget.getTemperature()               # Calculate distance from face to camera
    print(distance)
    
    if distance is not None and distance < 40:   # Check if distance is valid (not None) and less than 40
        if not speech_played:                    # Check if speech has already been played for this detection
            try:
                response_data = oneM2Mget.getTemperature()
                con_value = response_data
                data = f"Welcome to Smart City Living Lab. The current value of CO2 is {con_value[1]}, temperature is {con_value[2]}, and humidity is {con_value[3]}."
                text_to_speech(data)
                print(response_data)
                speech_played = True             # Set the flag to True to indicate that speech has been played
            except Exception as e:
                print(f"Error: {e}")
    else:
        speech_played = False                    # Reset the flag when no face is detected or face is too far

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    init_map(temp[2],temp[3],luminance)
    print(temp)
cap.release()
cv2.destroyAllWindows()