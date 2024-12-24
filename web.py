from flask import Flask, jsonify, render_template, request
import cv2
import numpy as np
import ai
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/get_result", methods=["POST"])
def result():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400

    image = request.files['image']
    print(image)
    np_array_image = np.fromstring(image.read(), np.uint8)
    img = cv2.imdecode(np_array_image, cv2.IMREAD_UNCHANGED)
    trans_mask = img[:,:,3] == 0
    img[trans_mask] = [255, 255, 255, 255]
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img = cv2.bitwise_not(img)
    cv2.imwrite("a.png",img)
    print(ai.get_letter(ai.predict(img)))
    return jsonify({'data': ai.get_letter(ai.predict(img))})


app.run(port=5001)