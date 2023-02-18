from flask import Flask, request
import math
 
app = Flask(__name__) 

# http://127.0.0.1:8000/quadratic?a=2&b=6&c=2
@app.route('/quadratic/', methods=['GET'])
def quadratic():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    c = int(request.args.get('c'))

    d = (b ** 2) - (4 * a * c)
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return { "x1": round(x1,4), "x2": round(x2,4)}
 
if __name__ == '__main__':
    app.run(port=8000)