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
