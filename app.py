from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name','')  # name 변수 추출
    data = pd.read_excel('소상공인_대구.xlsx')
    result = data[data['상호명'] == name].to_dict('records')
    return jsonify(result)


if __name__ == '__main__':
    app.run()