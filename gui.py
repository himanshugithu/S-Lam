from tkinter import *
from PIL import ImageTk, Image
import tkintermapview
# from oneM2Mgetall import onem2m_get_request, onem2m_get_requestAQ, onem2m_get_requestSL, onem2m_get_requestWF,onem2m_get_requestWQ
import datetime
from oneM2Mget import *

# Function to update all parameters
def update_data(temp,humi,lux):
    pass
    # # Update time and day labels
    # current_time = datetime.datetime.now().strftime("%H:%M:%S")
    # current_day = datetime.datetime.now().strftime("%A")
    # time_label.config(text="Time: " + current_time)
    # day_label.config(text="Day: " + current_day)
    
    # Update sensor data
    # value = onem2m_get_request()
    # value1 = onem2m_get_requestAQ()
    # value3 = onem2m_get_requestWF()
    # value4 = onem2m_get_requestSL()
    # value5 = onem2m_get_requestWQ()

    # temp_label.config(text="Temp:" + f" {temp}\xb0C")
    # rh_label.config(text="rH:" + f" {humi}%")
    # # signal_label.config(text="Signal Strength" + f" {}dB")
    # lux_label.config(text="Lux:" + f" {lux}ppm")
    # energy_label.config(text="Energy \n Generated:" + f" {value4[1]}Kwh")
    # water_flow_label.config(text="Water flow:" + f" {value3[1]}")
    # tds_label.config(text="Com. TDS:" + f" {str(value5[4][:-1])}")

    # Update map

    # Schedule the next update after 30 seconds
    
def init_map(tem,humi,lux):
    root = Tk()
    root.title("Sensor Data")
    root.configure(background='#0A0A0A')
    root.geometry('450x750')

    frame = Frame(root, bg='#0A0A0A')
    frame.pack(pady=10)

    # Create labels for time and day
    time_label = Label(frame, text="Time: ", font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    time_label.pack(side=LEFT, anchor=NW, pady=(10, 5), padx=(30, 50))

    day_label = Label(frame, text="Day: ", font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    day_label.pack(side=RIGHT, anchor=NW, pady=(10, 5), padx=(50, 30))

    # Create a frame to contain the images
    frame = Frame(root, bg='#0A0A0A')
    frame.pack(pady=10)

    # Load and resize the first image
    image1 = Image.open(r"smartCity_livingLab.png").resize((150, 100))
    photo1 = ImageTk.PhotoImage(image1)

    # Load and resize the second image
    image2 = Image.open(r"iiith_icon1.png").resize((150, 100))
    photo2 = ImageTk.PhotoImage(image2)

    # Create labels to display the images horizontally inside the frame
    label1 = Label(frame, image=photo2, bg='#0A0A0A')
    label1.image = photo1
    label1.pack(side=LEFT, padx=(0, 20))  # Add padding on the right side of the first image

    label2 = Label(frame, image=photo1, bg='#0A0A0A')
    label2.image = photo2
    label2.pack(side=LEFT, padx=(20, 0))  # Add padding on the left side of the second image

    # Create a canvas for drawing the line below the frame
    canvas_frame_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
    canvas_frame_line.create_line(0, 0, 500, 0, fill="white", width=2)
    canvas_frame_line.pack(pady=(5, 0))  # Adjust the padding to position the line below the frame

    # Add a label for the text "Smart city dashboard"
    label_text = Label(root, text="Smart city dashboard", font=('Arial', 14, 'bold'), bg='#0A0A0A', fg='white')
    label_text.pack(pady=(5, 0))  # Adjust the padding to position the label below the line

    # Create a canvas for drawing the line below the text
    canvas_text_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
    canvas_text_line.create_line(0, 0, 500, 0, fill="white", width=2)
    canvas_text_line.pack(pady=(5, 0))  # Adjust the padding to position the line below the text

    my_label = LabelFrame(root)
    my_label.pack(pady=5)

    map_widget = tkintermapview.TkinterMapView(my_label, width=400, height=270)
    map_widget.set_address("International Institute of Information Technology, Hyderabad")
    map_widget.set_zoom(16)
    map_widget.pack()
    map_widget.set_address("International Institute of Information Technology, Hyderabad")

    # Create a frame for the sensor data columns
    sensor_frame = Frame(root, bg='#0A0A0A')
    sensor_frame.pack(pady=20)  # Increase the distance between the two columns

    # Left column for sensor data
    left_column = Frame(sensor_frame, bg='#0A0A0A')
    left_column.pack(side=LEFT, padx=30)  # Increase the padding for the left column

    # Right column for sensor data
    right_column = Frame(sensor_frame, bg='#0A0A0A')
    right_column.pack(side=RIGHT, padx=30)  # Increase the padding for the right column

    # Add labels for sensor data
    temp_label = Label(left_column, font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    temp_label.pack(anchor=W, pady=5)

    rh_label = Label(left_column, font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    rh_label.pack(anchor=W, pady=5)

    signal_label = Label(left_column, font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    signal_label.pack(anchor=W, pady=5)

    lux_label = Label(left_column, font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    lux_label.pack(anchor=W, pady=5)

    energy_label = Label(right_column, font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    energy_label.pack(anchor=W, pady=5)

    water_flow_label = Label(right_column, font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    water_flow_label.pack(anchor=W, pady=5)

    tds_label = Label(right_column, font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
    tds_label.pack(anchor=W, pady=5)
    temp_label.config(text="Temp:" + f" {tem}\xb0C")
    rh_label.config(text="rH:" + f" {humi}%")
    # signal_label.config(text="Signal Strength" + f" {}dB")
    lux_label.config(text="Lux:" + f" {lux}ppm")
    root.mainloop()
    root.after(30000, update_data)

# Initial update

if __name__ == "__main__":
    print("kdsncsn")
    init_map(11,11,11)
    update_data(11,11,11)
    