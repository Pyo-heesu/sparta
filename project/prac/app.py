from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
## test
## test2
## test3
## test4
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!', 'title_give':title_receive})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!',"title" : title_receive})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

#    127.0.0.1 == 0.0.0.0 == localhost
