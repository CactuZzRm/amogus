from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_answer', methods=['GET'])
def get_answer():
    return jsonify({"answer": 'amogus'})

if __name__ == '__main__':
    app.run(debug=True)