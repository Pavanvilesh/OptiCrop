from database1 import (
    create_database,
    save_prediction,
    get_predictions,
    get_crop_count,
    get_crop_statistics
)

from weather import get_weather

from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


# Create Database
create_database()



# Load ML Model

model = pickle.load(open("model/model.pkl", "rb"))




# Crop Images

crop_images = {

    "rice": "rice.jpg",
    "wheat": "wheat.jpg",
    "maize": "maize.jpg",
    "cotton": "cotton.jpg",
    "jute": "jute.jpg",
    "coffee": "coffee.jpg",
    "banana": "banana.jpg",
    "mango": "mango.jpg",
    "apple": "apple.jpg",
    "orange": "orange.jpg",
    "papaya": "papaya.jpg",
    "coconut": "coconut.jpg",
    "grapes": "grapes.jpg",
    "watermelon": "watermelon.jpg",
    "muskmelon": "muskmelon.jpg",
    "pomegranate": "pomegranate.jpg",
    "chickpea": "chickpea.jpg",
    "kidneybeans": "kidneybeans.jpg",
    "pigeonpeas": "pigeonpeas.jpg",
    "mothbeans": "mothbeans.jpg",
    "mungbean": "mungbean.jpg",
    "blackgram": "blackgram.jpg"

}




# HOME PAGE

@app.route("/")
def home():

    return render_template("index.html")







# PREDICTION

@app.route("/predict", methods=["POST"])
def predict():

    try:

        N = float(request.form["Nitrogen"])

        P = float(request.form["Phosphorus"])

        K = float(request.form["Potassium"])

        temperature = float(request.form["Temperature"])

        humidity = float(request.form["Humidity"])

        ph = float(request.form["Ph"])

        rainfall = float(request.form["Rainfall"])




        prediction = model.predict([[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]])



        crop = prediction[0]



        # Save database

        save_prediction(crop)



        image = crop_images.get(
            crop.lower(),
            "default.jpg"
        )



        return render_template(

            "result.html",

            crop=crop,

            image=image,

            nitrogen=N,

            phosphorus=P,

            potassium=K,

            temperature=temperature,

            humidity=humidity,

            ph=ph,

            rainfall=rainfall

        )



    except Exception as e:

        return f"Error : {e}"









# DASHBOARD

@app.route("/dashboard")
def dashboard():

    total = get_crop_count()

    predictions = get_predictions()

    statistics = get_crop_statistics()

    weather = get_weather()



    return render_template(

        "dashboard.html",

        total=total,

        predictions=predictions,

        statistics=statistics,

        weather=weather

    )








# HISTORY

@app.route("/history")
def history():

    predictions = get_predictions()


    return render_template(

        "history.html",

        predictions=predictions

    )








# ABOUT

@app.route("/about")
def about():

    return render_template("about.html")








# CONTACT

@app.route("/contact")
def contact():

    return render_template("contact.html")








# RUN

if __name__ == "__main__":

    app.run(debug=True)