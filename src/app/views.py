from app import app



@app.route('/hello')
def hello():
    return 'Hello flask in docker'