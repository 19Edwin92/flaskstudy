from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return '안녕 Flask'
      
if __name__ == '__main__':
   app.run(debug = True)