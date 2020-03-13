import os
import numpy as np
import json
from flask import Flask, request, render_template
app = Flask(__name__)


#uploads_dir = os.path.join(app.instance_path, 'uploads')
#os.makedirs(uploads_dir, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])

def hello_world():
    
    if request.method == 'GET':
        
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        profile = request.files['file']
        file_path = "../data_io/videos/" + "upload.mp4"
        #file_path = "../data_io/detectron_out/" + "upload.npz"
        #file_path = "./joints3d/upload3d.npy"
        profile.save(file_path)
        os.system("python ./command.py")
        
        return render_template('result.html')

@app.route('/upload3d', methods=['GET'])
def upload3d():
    points = np.load("./joints3d/upload3d.npy")
    return json.dumps(points.tolist())

    
if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0", port=80)