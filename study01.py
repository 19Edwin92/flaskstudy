from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return '안녕 Flask'
 
#URL 인자 웹브라우저 내용에 반영하기(1) 문자열
@app.route('/user/<id>')
def show_user_profile(id):
  return 'User %s' %id

#URL 인자 웹브라우저 내용에 반영하기(2) 숫자열
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

#URL 인자 웹브라우저 내용에 반영하기(3) 복수의 데코레이터
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="값이 비어있을 때 초기값 설정가능"):
  return 'User %s' %name

#render_template를 통해서 html문서 배포하기 
@app.route('/study01')
def study01():
  return render_template('study01.html')

      
if __name__ == '__main__':
   app.run(debug = True)