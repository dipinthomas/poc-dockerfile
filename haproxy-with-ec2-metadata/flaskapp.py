import os
from flask import jsonify, request, Flask
from ec2_metadata import ec2_metadata

app = Flask(__name__)

@app.route("/", methods=["GET"])
def az():
    return 'REGION = ' +  ec2_metadata.region + '\n' + ' AZ = ' + ec2_metadata.availability_zone + '\n'
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
