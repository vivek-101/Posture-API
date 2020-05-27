from flask import Flask, request, jsonify
from test import initiate,bmi_calculator,Posture
from scraper import exercise
app = Flask(__name__)


@app.route("/predict_api/",methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    output = initiate(int(data['hours']))
    tips = exercise(data['issue'])
    exc_keys = [key for key in tips.keys()]
    exc_url = [value[0] for value in tips.values()]
    exc_ben = [value[1] for value in tips.values()]
    bmi = bmi_calculator(float(data['height']), float(data['weight']))
    posture = Posture(bmi['bmi'],output[2])
    return jsonify(line_graph=output[0],
                   pie_chart=output[1],
                   exercise1=(exc_keys[0], exc_url[0], exc_ben[0]),
                   exercise2=(exc_keys[1], exc_url[1], exc_ben[1]),
                   exercise3=(exc_keys[2], exc_url[2], exc_ben[2]),
                   bmi=bmi['bmi'],
                   category=bmi['category'],
                   posture=posture), 200


if __name__ == '__main__':
    app.run(debug=True)
