import os
import threading
from flask import Flask
from run import main  # <- yaha apne bot ka start function import karo (jo bot chalata hai)

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 8080))

@app.route("/")
def home():
    return "Bot is running on Render!"

def start_bot():
    main()  # yaha tumhara bot start hoga (jo run.py me hai)

if __name__ == "__main__":
    # Bot ko background thread me start kar do
    threading.Thread(target=start_bot).start()

    # Flask server ko run karwao
    app.run(host="0.0.0.0", port=PORT)