# REdirect 와 HTTP 메소드에 대해서 살펴보자. 
# REdirect 메소드, 7번째줄부터 32번째줄까지 - 첫줄에  import redirect, url_for 추가 
# HTTP 메소드(이론편), 34번째줄부터 - 53번쨰줄,  import request 추가 
# HTTP 메소드(실습편), 55번째줄부터 - 76번쨰줄, 
# 쿠키와 세션, 78번째줄부터 - 번째줄,

# 01 Redirect
from flask import Flask, redirect, url_for, request, render_template, make_response, session
app = Flask(__name__)
app.secret_key = 'any random string'

#메인페이지 
# @app.route('/')
# def home():
#   return '안녕 redirect 알아보기에 대해서 알아보자. http://127.0.0.1:5000/redirectpage/guest 또는 http://127.0.0.1:5000/redirectpage/아무거나 입력해보자.'

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

# 02 HTTP 메소드 이론편
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

# 03 HTTP 메소드 실습편
#study03-01.html 경로
@app.route('/study0301')
def study0301():
  return render_template('study03-01.html')

#study03-02.html 경로
@app.route('/study0302')
def study0302():
  return render_template('study03-02.html')


@app.route('/study03',methods = ['POST', 'GET'])
def study03():
   if request.method == 'POST':
      result = request.form
      # name = request.form['name']
      # if name != "edwin": 
      #   return render_template('study03-02.html', result="fail")
      # else:
      #   return render_template('study03-02.html', result="success", name=name)
      return render_template('study03-02.html', result=result)
    
# 3 쿠키와 세션
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
  if request.method == 'POST':
    users = request.form['nm']
    resp = make_response("Cookie Setting Complete")
    resp.set_cookie('userID', users)
    return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>' 

@app.route('/')
def index():
  if 'username' in session:
    username = session['username']
    return 'Logged in as ' + username + '<br>' + \
    "<b><a href = '/logout'>click here to log out</a></b>"
  else:
    return "You are not logged in <br><a href = '/login'></b>" + \
    "click here to log in</b></a>"


@app.route('/study03cookie')
def study03cookie():
  return render_template('study04.html')

    
    
    
if __name__ == '__main__':
  app.run(debug=True)
  
