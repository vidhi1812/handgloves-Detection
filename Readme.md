**Smart Gloves detection System**

1-The System tries to detect the gloves or no gloves in hand when we upload any image of hand or also using video framing also.

2-For this System we Use ***python 3.10+ version ***

**For Dataset-**

1- Choose Robowflow 
2-Train the YOLO8n 
3- then run the script gloves_detection.py for images 
4- run the script "glove.py" for video.

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

![imag2](https://github.com/user-attachments/assets/0fdef5d4-d76f-44ae-b7c7-66238659faf0)

![imag2](https://github.com/user-attachments/assets/1496bf12-468f-4b0b-922e-7ed7325cd01d)


<p align="center"> <img src="https://github.com/user-attachments/assets/980a474c-cc34-4c3a-8c4a-e4329fa85d29" width="400" height="300"/> </p> <p align="center"><b>Input Image</b></p> <p align="center"> <img src="https://github.com/user-attachments/assets/00ca97a6-8943-4e82-bce1-15cbcf07b5e9
" width="400" height="300"/> </p> <p align="center"><b>Output Image (Gloves Detected)</b></p>
