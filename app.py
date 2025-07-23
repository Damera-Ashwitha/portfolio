from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import datetime

app = Flask(__name__)

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client.portfolio_db
messages_collection = db.messages  # collection to store contact messages

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Insert into MongoDB
        messages_collection.insert_one({
            "name": name,
            "email": email,
            "message": message,
            "timestamp": datetime.datetime.utcnow()
        })

        return redirect('/?success=true')

    return render_template('index.html',
        name="Ashwitha Damera",
        tagline="Computer Science Student | ML Enthusiast | Full-Stack Developer",
        about="I am Ashwitha Damera, a Computer Science and Engineering student at GNITS, Hyderabad, with a CGPA of 9.3. I'm passionate about machine learning and full-stack development. I love solving real-world problems and continuously learning through hands-on experience and projects.",
        skills=[
            {"category": "Programming", "items": "C, C++, Python, Java"},
            {"category": "Web Technologies", "items": "HTML, CSS"},
            {"category": "ML Tools", "items": "NumPy, Pandas, Scikit-learn"},
            {"category": "Development Tools", "items": "VS Code, Linux"},
        ],
        projects=[
            {
                "title": "Employee Attrition Prediction",
                "description": "Developed a full-stack web app using FastAPI and Random Forest to predict employee attrition. Features a modern dashboard, styled survey form, and visual insights into attrition probability and reasons.",
                "tools": "Python, FastAPI, HTML, CSS, Machine Learning"
            }
        ],
        certifications=[
            "NPTEL - The Joy of Computing with Python",
            "Cybersecurity Workshop",
            "Database & SQL – Infosys Springboard",
            "Python Foundation – Infosys Springboard",
            "Basics of Python – Infosys Springboard"
        ],
        activities=[
            "GHMC SEEPC Coordinator",
            "Volunteer – Telangana Formation Day Celebrations"
        ],
        email="ashwithadamera2885@gmail.com",
        phone="+91-7013182885",
        year=2025
    )

if __name__ == '__main__':
    app.run(debug=True)
