from flask import Flask

#创建1个Flask实例
app = Flask(__name__)

@app.route('/')
def first_flask():
    return '<h1>Hello,flask!</h1>'

if __name__ == "__main__":
    app.run('127.0.0.1','9090')