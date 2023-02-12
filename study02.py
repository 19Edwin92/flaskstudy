# REdirect 와 HTTP 메소드에 대해서 살펴보자. 
# REdirect 메소드, 5째줄부터 30째줄까지 - 첫줄에  import redirect, url_for 추가 
# HTTP 메소드, 32째줄부터 - 첫줄에  import request 추가 

# 01 Redirect
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

#메인페이지 
@app.route('/')
def home():
  return '안녕 redirect 알아보기에 대해서 알아보자. http://127.0.0.1:5000/redirectpage/guest 또는 http://127.0.0.1:5000/redirectpage/아무거나 입력해보자.'

#redirect를 발생시킬 페이지
@app.route('/redirectpage/<name>')
def redirectpage(name):
  if name == 'guest':
    return redirect('/guest')
  else:
    return redirect(url_for('hello_user', username = name))
  
#상황1 - 방문자일 때, guest 일 때
@app.route('/guest')
def hello_guest():
  return '안녕 redirect 알아보기, 방문자님 안녕하세요.'

#상황2 - 사용자일 때, guest 이외일 때
@app.route('/user/<username>')
def hello_user(username):
  return '안녕 redirect 알아보기, %s님 반갑습니다.' % username  

# 02 HTTP 메소드 
#상황발생 : HTTP메소드를 실행시킬 조건의 상황 설정
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
    
#발생상황 : 조건부 상황에 따라 실행될 결과적 경로
@app.route('/success/<name>')
def success(name):
   return '반갑습니다. %s님' % name
 
#study02.html 경로
@app.route('/study02')
def study02():
  return render_template('study02.html')

if __name__ == '__main__':
  app.run(debug=True)
  
