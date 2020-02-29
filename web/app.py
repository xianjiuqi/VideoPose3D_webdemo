import os
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
        #file_path = "../data_io/videos/" + "upload.mp4"
        file_path = "../data_io/detectron_out/" + "upload.npz"
        profile.save(file_path)
        os.system("python ./command.py")
        

        
        return render_template('result.html')
    
if __name__ == '__main__':
    app.run(debug=True)