from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

app.config.from_object(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/search', methods=['GET'])
def search():
    print('함수')
    name = request.args.get('name','')  # name 변수 추출
    if name:
        print("name", name)
    else:
        print('name 없음')
    data = pd.read_csv('소상공인시장진흥공단_상가(상권)정보_인천_202303.csv')
    result = data[data['상호명']==name][['상호명', '상권업종대분류코드', '상권업종대분류명', '도로명주소', '지번주소', '경도', '위도']].to_dict('records')
    print('함수끝')
    return jsonify(result)


if __name__ == '__main__':
    app.run()