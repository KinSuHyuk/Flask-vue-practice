from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET'])
def search():
    print('search함수 시작')
    name = request.args.get('name','')  # name 변수 추출
    print('파일 읽기 시작')
    data = pd.read_excel('소상공인_대구.xlsx')
    print('파일 읽기 끝')
    print('컬럼명', data['상호명'])
    result = data[data['상호명'] == name].to_dict('records')
    return jsonify(result)

if __name__ == '__main__':
    app.run()