*(Step 1: Create the Virtual Environment*

*Run this command in your terminal to create the venv folder:*



*PowerShell)*



## **python -m venv venv**





*Step 2: Activate the Virtual Environment*

*Once created, run the activation command again:*



*PowerShell*



### **.\\venv\\Scripts\\Activate**



Step 3: (If you get a script execution error)

If PowerShell blocks the script with an error about execution policies, run this command first to allow it, then try activating again:



PowerShell



### **Set-ExecutionPolicy Unrestricted -Scope Process**



1\. தேவையான Packages-களை இன்ஸ்டால் செய்யவும்

உங்கள் டெர்மினலில் (வென்வுக் குறியீடு (venv) வந்த பிறகு) இந்தக் கட்டளையை இயக்கித் தேவையான அனைத்து லைப்ரரிகளையும் இன்ஸ்டால் செய்யுங்கள்:



PowerShell





### **pip install fastapi uvicorn pydantic google-genai streamlit requests**







2\. Gemini API Key-ஐ செட் செய்யவும்

உங்கள் AI backend வேலை செய்வதற்கு உங்கள் Gemini API key தேவை. அதை உங்களுடைய PowerShell டெர்மினலில் இப்படி செட் செய்யுங்கள்:



**PowerShell**

### **$env:GEMINI\_API\_KEY="AQ.Ab8RN6JWUaZ\_C2HjIqmmQIxZmVuA7WGq031pWzPyxrxBqUK0bQ"**















Step 1: Open a New Terminal Window

Open a second PowerShell window or command prompt.



Navigate to your project folder and activate your virtual environment:



Bash

### 

### **cd D:\\NANMUTHALVAN PROJECTS\\LEGALEASE-main**

### **.\\venv\\Scripts\\Activate**







Start the Backend Server

Check your project folder (D:\\NANMUTHALVAN PROJECTS\\LEGALEASE-main) for your backend file. It is usually named main.py, app\_backend.py, or server.py.



Run it using Uvicorn (assuming your backend file is named main.py with an app named app):



Bash

### **uvicorn main:app --reload --port 8000**





&#x20;Run the App Correctly

Instead of using python app.py, Streamlit apps must be run using the Streamlit CLI so that its session state and server context work correctly.



In your terminal (venv), run:



Bash



### **streamlit run app.py**













FastAPI Backend-ஐ இயக்கவும்

உங்கள் FastAPI கோப்பை (எடுத்துக்காட்டாக app.py அல்லது backend கோப்பு) ஒரு டெர்மினலில் இயக்கவும்:



PowerShell





### **python app.py**









