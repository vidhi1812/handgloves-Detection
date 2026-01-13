**Smart Gloves detection System**   
The Smart Gloves Detection System detects whether a person is wearing gloves or not using images or real-time video streams. The system is designed for industrial and safety-use cases where glove compliance is mandatory. It uses a YOLOv8n object detection model trained on a custom dataset to identify hands with and without gloves.

2-For this System we Use ***python 3.10+ version ***

**For Dataset-**  
Dataset Name: Hand Gloves Detection Dataset  
Source: Roboflow :  https://universe.roboflow.com/gpartnershikp/gloves-oy8ur
Classes:  
glove  
no_glove  
The dataset was annotated using bounding boxes and exported in YOLOv8 format.   
Images include variations in hand orientation, lighting conditions, and partial occlusions to improve real-world robustness.   


**Model Used**  
Model: YOLOv8n (Nano version)  
Framework: Ultralytics YOLO   
Reason for Choice:   
YOLOv8n provides a good balance between speed and accuracy, making it suitable for real-time detection on images and video streams.

**Preprocessing & Training**

Images were resized automatically by YOLO during training.  
***Default YOLO augmentations were used, including:***
Random scaling  
Flipping  
Brightness and contrast adjustments  

The model was trained on the Roboflow dataset using a custom train.py script.   
Training was performed using Python 3.10+ inside a virtual environment.   

**How to work:**
 
 *Create the venv :*
 python -m venv venv

 *Activate the venv:*
 venv/scripts/activate

 *Install the requirements:*
  pip install -r requirements.txt

  *Run Script*
  python gloves_detection.py



  **for training for YOLO8n Model**


  *Create the venv :*
 python -m venv venv

 *Activate the venv:*
 venv/scripts/activate

 *Install the requirements:*
  pip install -r requirements.txt

  *Run training Script*
  python train.py




<p align="center"> <img src="https://github.com/user-attachments/assets/980a474c-cc34-4c3a-8c4a-e4329fa85d29" width="400" height="300"/> </p> <p align="center"><b>Input Image</b></p> <p align="center"> <img src="https://github.com/user-attachments/assets/00ca97a6-8943-4e82-bce1-15cbcf07b5e9" width="400" height="300"/> </p> <p align="center"><b>Output Image (Gloves Detected)</b></p>

<p align="center"> <img src="https://github.com/user-attachments/assets/0fdef5d4-d76f-44ae-b7c7-66238659faf0" width="400" height="300"/> </p> <p align="center"><b>Input Image</b></p> <p align="center"> <img src="https://github.com/user-attachments/assets/1496bf12-468f-4b0b-922e-7ed7325cd01d" width="400" height="300"/> </p> <p align="center"><b>Output Image (Gloves Detected)</b></p>
