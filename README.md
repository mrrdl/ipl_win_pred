IPL Win Predictor
An interactive web application that predicts the outcome of Indian Premier League (IPL) matches using machine learning. Built with Python and Streamlit, this app leverages historical match data to forecast match winners based on user inputs.

🔗 Live Demo
Experience the application live at: iplpredwin.streamlit.app

📂 Project Structure
app.py – Main Streamlit application script.

pipe.pkl – Serialized machine learning pipeline/model.

requirements.txt – List of Python dependencies.

⚙️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/mrrdl/ipl_win_pred.git
cd ipl_win_pred
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
To run the application locally:

bash
Copy
Edit
streamlit run app.py
After executing the above command, the application will be accessible in your web browser at http://localhost:8501/.

🧠 Model Details
The application utilizes a pre-trained machine learning model (stored in pipe.pkl) to predict match outcomes. The model was trained on historical IPL match data, considering various features such as team statistics, player performances, and match conditions.

🛠️ Features
User-friendly interface built with Streamlit.

Real-time predictions based on user inputs.

Lightweight and easy to deploy.

🤝 Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.
