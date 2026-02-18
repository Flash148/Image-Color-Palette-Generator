from flask import Flask, render_template, request
import os
from color_extractor import extract_colors, load_image, rgb_to_hex


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


#extract route that
@app.route('/extract', methods=['POST'])
def extract():
    #get the uploaded file
    file = request.files['image']

    #get the number of colors
    num_colors = int(request.form['num_colors'])

    #save file to temporary location
    filepath = os.path.join('static/uploads', file.filename)
    file.save(filepath)

    #extract colors 
    image_array = load_image(filepath)
    colors, percentages = extract_colors(image_array, num_colors)

    #prepare color data for rendering
    color_data = []
    for i in range(len(colors)):
        color_data.append({
            'rgb': tuple(int(x) for x in colors[i]),
            'hex': rgb_to_hex(colors[i]),
            'percentage': percentages[i] * 100 #convert to percentage
        })

    return render_template('result.html', colors=color_data, image_path=filepath)



if __name__ == '__main__':
    app.run(debug=True)