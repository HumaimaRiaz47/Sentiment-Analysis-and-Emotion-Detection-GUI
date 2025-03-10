# Sentiment-Analysis-and-Emotion-Detection-GUI
A Python-based GUI application for sentiment analysis, named entity recognition (NER), and emotion detection using Tkinter.

## Overview
This project is a Python-based GUI application for **sentiment analysis**, **named entity recognition (NER)**, and **emotion detection**.  
The application features **user registration and login functionality** handled using file-based storage. It is built using `Tkinter` for the graphical interface and integrates various NLP techniques for text analysis.


## Features
- **User Authentication:** Registration and login functionality using file handling.  
- **Sentiment Analysis:** Uses `VADER SentimentIntensityAnalyzer` to classify text sentiment.  
- **Named Entity Recognition (NER):** Implements `spaCy` to identify named entities.  
- **Emotion Detection:** Utilizes `NRCLex` to analyze emotions in text.  
- **GUI Interface:** Built with `Tkinter` for ease of use.  


## Technologies Used
- **Programming Language:** Python  
- **IDE:** PyCharm  
- **Libraries:**  
  - `vaderSentiment` for sentiment analysis  
  - `spaCy` for named entity recognition (NER)  
  - `NRCLex` for emotion detection  
  - `tkinter` for GUI development  


## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install required dependencies:
   ```sh
   pip install vaderSentiment spacy NRCLex
   ```
3. Download spaCy's English model:
   ```sh
   python -m spacy download en_core_web_md
   ```
4. Run the application:
   ```sh
   python app.py
   ```


## Usage
1. Open the application and register/login.  
2. Enter text for analysis.  
3. Select the desired analysis type (**Sentiment, NER, or Emotion Detection**).  
4. View the results in the GUI output.  


## File Handling for Authentication
- **User credentials** are stored securely using file handling.  
- The system verifies login details before granting access to the main application.

## ScreenShots

![Screenshot from 2025-03-10 15-48-39](https://github.com/user-attachments/assets/373023a9-742e-4c0c-bbe1-363ac9b165d6)
![Screenshot from 2025-03-10 15-49-15](https://github.com/user-attachments/assets/3a678524-2ab7-4cee-bcc5-4d5dd071ccb2)
![Screenshot from 2025-03-10 15-51-29](https://github.com/user-attachments/assets/b63dcdde-0d09-4945-8db9-799f2a76dcb8)
![Screenshot from 2025-03-10 15-52-46](https://github.com/user-attachments/assets/3e127738-a43d-4955-a2a6-5da4a3e24b15)
![Screenshot from 2025-03-10 16-04-49](https://github.com/user-attachments/assets/977d7e63-97ee-4b14-8fcd-72ea011dc1be)
![Screenshot from 2025-03-10 16-07-34](https://github.com/user-attachments/assets/398cefa9-dd41-492c-87d2-5184bb88f0bc)

