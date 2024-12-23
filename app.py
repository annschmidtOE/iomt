from flask import Flask, render_template
import base64
from io import BytesIO
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def home():
    x = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "lørdag", "søndag"]
    y = [2, 4, 1, 3, 5, 10, 2]

    fig = plt.figure(figsize=(8, 4))
    plt.bar(x, y, color='skyblue')
    plt.title("Medicinforbrug pr. dag")
    plt.xlabel("Dag")
    plt.ylabel("Antal piller")

    img = BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    return render_template("index.html", graph=graph_url)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")