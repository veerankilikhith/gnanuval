from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    message = """
    Hey Gnanu,

Ninnu first time chusina roju nundi destiny ane nammakam start ayyindhi.
Mana journey chala vintha kadha…

5th class nundi mana iddaram same school lo chadavadam… inter varaku same college lo undadam… kani okkasari kuda chudatam jaragaledu. Same centre lo 2 years exams rayadam jarigindhi… still we didn’t notice each other.

But ippudu alochisthe anipisthundhi… maybe destiny was slowly writing our story.

Nuv SVS lo chadivavu ani telisinappudu nenu shock ayyanu.
Nuv lunch box kosam kindhaki vasthav ani cheppaavu appudu kuda shock okkasari kuda chudala ani.Maybe destiny wanted the right time.

Gnanu… nuv antte chala istam.
I truly love you from the bottom of my heart.

Nitho unte baguntundhi… nuv navvithe inka baguntundhi…
Honestly, naaku life lo chala pedda expectations levu — nitho kalisi nadavadam chalu ane feeling vastundi.

I don’t want to force you or rush you.
Nee decision ni respect chestha.
Kani oka maata matram nijam — naa feelings maravu.

Will you give me a chance to be part of your life… forever❤️?
Will you walk with me… not just now… but for life❤️?
    """
    return render_template("index.html", message=message)

import os

@app.route("/yes")
def yes():
    return render_template("yes.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
