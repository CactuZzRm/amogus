from flask import Flask, request, jsonify
import jamspell
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

app = Flask(__name__)

@app.route('/get_answer', methods=['GET'])
def get_answer():
    return jsonify({"answer": 'amogus'})

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    corrector = jamspell.TSpellCorrector()
    corrector.LoadLangModel('wiki+text/model_twiki.bin')
    
    text = corrector.FixFragment('Цвæр царæгай кæнæ зæйæгой нæ зæронт кæны')
    changed_text = text

    return jsonify({'changed_text': changed_text})

if __name__ == '__main__':
    app.run(debug=True)
