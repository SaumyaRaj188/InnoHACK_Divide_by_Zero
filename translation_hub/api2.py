from pdf2image import convert_from_path
from pytesseract import pytesseract
# URL of the Flask endpoint where you want to send the POST request

import os
# Send the POST request

# Check the response status code


from flask import Flask, request, jsonify
from openai import OpenAI
client = OpenAI(api_key='YOUR_API_KEY')
from final_prompt import translate




from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)


# Define a route that handles a POST request
@app.route('/translate', methods=['POST'])
def translate_endpoint():
    # Accessing JSON data from the request body
    data = request.json

    # CHECK FOR ALL NECESSARY ARGUMENTS
    if 'trans_lang' not in data or 'type' not in data or 'content' not in data:
        return jsonify({'error': 'Missing required variables'}), 400

    # TRANSLATE ACCORDINGLY
    trans_lang = data['trans_lang']
    translation_type = data['type']
    content = data["content"]
    result = translate(client,trans_lang=trans_lang,trans_type=translation_type,content=content)

    # RETURN RESULT
    return jsonify({'translation': result})


@app.route('/pdf', methods=['POST'])
def upload_pdf():
    # import module
    print("a")
    if 'file' not in request.files:
        return jsonify({'translation':'No file part'})
    file = request.files['file']
    print("b")
    trans_lang = request.form['data']
    print("c")
    if file.filename== '':
        return jsonify({'translation':'No file selected'})
    
    file.save(file.filename)
    print("d")

    # Store Pdf with convert_from_path function
    images = convert_from_path(file.filename)
    os.remove(file.filename)

    text=""

    for i in range(len(images)):
        text += pytesseract.image_to_string(images[i])
        text += "\n\n"
    trans = translate(client,trans_lang,'auto',text)
    if trans==None:
        return jsonify({"translation":"some error occured"})
    else:
        return jsonify({"translation": "hello how are you"})



@app.route('/img', methods=['POST'])
def upload_img():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        # Save the uploaded file to a desired location
        file.save('uploads/' + file.filename)
        return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
