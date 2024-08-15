import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.models.chat_model.emix_service_model.emix_service_model import EmixServiceChat
from api.routes.app_routes import app_routes
from api.utils.first_init import FirstInit
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
from importlib.metadata import version, PackageNotFoundError


firstInit = FirstInit()

# os.environ["OPENAI_API_KEY"] = str(firstInit.get_api_key())
os.environ.get('OPENAI_API_KEY')
app = Flask(__name__)
app.debug = True
CORS(app)   
app_routes(app)




@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    # print(str(firstInit.get_api_key()))    

    app.run()
