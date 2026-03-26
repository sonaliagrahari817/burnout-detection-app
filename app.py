
from flask import Flask, request, render_template

app = Flask(__name__)

# Home route (form page)
@app.route('/')
def home():
    return render_template('index.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Form data lena
        name = request.form['name']
        sleep = float(request.form['sleep'])
        study = float(request.form['study'])
        stress = float(request.form['stress'])
        screen = float(request.form['screen'])

        score = stress*2 + study + screen - sleep

        # 🔥 Burnout Logic (rule-based AI)
        if stress > 7 and sleep < 5 and screen > 6:
            result = "High Burnout 😵"
            suggestion = "Take proper rest, reduce screen time, and relax a bit."
        
        elif stress > 4 or study > 8:
            result = "Medium Burnout 😐"
            suggestion = "Try to manage time better, take short breaks, and balance study & rest."
        
        else:
            result = "Low Burnout 😊"
            suggestion = "You're doing well! Keep maintaining a healthy routine."
        
        
        # Output page
        return f"""
        <html>
        <body style="font-family: Arial; text-align:center; margin-top:50px;">

        <h2>Hey {name}! 👋</h2>
        <h4>Here is your burnout analysis:</h4>

        <h3 style="color:{'red' if 'High' in result else 'orange' if 'Medium' in result else 'green'};">
        Burnout Level: {result}
        </h3>

        <p>Your Burnout Score: {score}</p>

        <p>{suggestion}</p>
        <p><b>Tip:</b> Take at least 5–10 min break after every study hour 📚</p>

        <p><i>(Higher score means higher burnout)</i></p>

        <br>
        <a href="/">⬅ Go Back</a>

        </body>
        </html>
        """

    except Exception as e:
      return f"Error occurred: {str(e)}"


# Run app
if __name__ == "__main__":
    app.run()
