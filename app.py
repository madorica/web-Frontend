
from flask import Flask, request , render_template 
import subprocess

app = Flask(__name__,template_folder='./templates/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:button_id>', methods=['GET'])
def button_click(button_id):
    result = f"Button {button_id} was clicked on the backend!"
    if button_id == 1:
        subprocess.run(["touch",'/home/madorica/Desktop/file1.txt'])
    return result

if __name__ == '__main__':
    app.run(debug=True)