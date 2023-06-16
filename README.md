# Virtual-Trial-Room

It is a virtual environment that utilizes the laptop camera to capture the user's image, which serves as an input. By employing face and body detection techniques, the video stream is analyzed to identify the presence of human faces, allowing product images such as dresses and face accessories to be accurately masked on to user’s image

# Libraries

- Pillow-The Pillow package is a popular Python library that provides support for manipulating and processing images.some common uses of the Pillow package are image processing,image filtering,image enhancement etc.
- Pandas-The pandas package is a powerful and widely used Python library for data manipulation and analysis. It provides data structures and functions that make it easier to work with structured data, such as tabular data or time series data.
- Seaborn-The seaborn library is a powerful data visualization library built on top of Matplotlib, another popular visualization library in Python. Seaborn provides a higher-level interface and more aesthetically pleasing default styles compared to Matplotlib. Used for statistical analysis of data[provides functions to draw line plots,bar plot etc using which statistical analysis of the data can be done].
- OpenCV-OpenCV (Open Source Computer Vision) is a popular open-source computer vision and image processing library. It provides a comprehensive set of tools and functions for various tasks related to computer vision, including image and video processing, object detection and recognition, feature extraction, camera calibration, and more. 
- Mysqlclient-The mysqlclient library is a Python interface for connecting to and interacting with MySQL databases.
- Pyotp-The pyotp library is a Python library that provides support for generating and verifying OTP (One-Time Password) tokens.
- Pyglet-The pyglet library is a powerful multimedia library for Python that provides support for creating games, interactive applications, and multimedia-rich user interfaces. It offers a range of features for graphics, audio, windowing, and event handling.
- Flask-The Flask library is a popular web framework for Python that allows you to build web applications quickly and efficiently.It provides the necessary tools and features to handle routing, request handling, template rendering, and more, allowing you to build web applications efficiently.
- Flask socketIO-Flask-SocketIO is an extension for Flask that adds WebSocket support to Flask applications. WebSocket is a communication protocol that provides full-duplex communication channels over a single TCP connection, enabling real-time bidirectional communication between the client (typically a web browser) and the server. 
- imutils-The imutils library is a set of convenience functions that simplify common image processing tasks in OpenCV (Open Source Computer Vision Library) with Python. It provides a collection of helper functions and wrappers that make it easier to work with images and perform common image processing operations.

# Requirements
## Functional Requirements
-Create a web application using flask. 
- User can select the product and add to cart. 
- System will build the options for trying clothes. 
- If user selects try the system will open the camera and collect the details of the person.
- Then system find the person body features using the Haar cascade classifier. 
- Then matches the dress to the corresponding body and display the results. 
- Application should accurately shows the virtual mirror for the selected dress.

## Non-Functional Requirements
- The program must be self-contained so that it can easily be moved from one Computer to another. It is assumed that network connection will be available on the computer on which the program resides. 
- Capacity, scalability and availability. The system shall achieve 100 per cent availability at all times. The system shall be scalable to support additional clients and volunteers.
- Maintainability. The system should be optimized for supportability, or ease of maintenance as far as possible. This may be achieved through the use documentation of coding standards, naming conventions, class libraries and abstraction. 
- Randomness, verifiable and load balancing. The system should be optimized for supportability, or ease of maintenance as far as possible. This may be achieved through the use documentation of coding standards, naming conventions, class libraries and abstraction. It should have randomness to check the nodes and should be load balanced

## Hardware Requirements
- System : Intel I5. 
- Hard Disk : 120 GB.
- Monitor : 15” LED 
- Input Devices : Keyboard, Mouse 
- Ram : 8 GB

## Software Requirements
- Operating system : Windows 7 and above.
- Coding Language : PYTHON 3.6 
- Tools : Anaconda

### Procedure

 Step 1: 
  ```bash
  conda create -n tf python=3.6
  ```
  Step 2: 
  ```bash
  Activate tf
  ```
  Step 3: 
  ```bash
  Pip install pillow
Pip install pandas
Pip install Seaborn
Pip install opencv-contrib-python==3.4.5.20
Conda install -c conda-forge dlib
Pip install –only-binary :all: mysqlclient
Pip install pyotp
Pip install pyglet
Pip install flask
Pip install flask-Socketio
Pip install imutils

  ```
 
