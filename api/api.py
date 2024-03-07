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

if __name__ == '__main__':
    app.run(debug=True)