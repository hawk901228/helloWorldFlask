from flask import Flask, jsonify
app = Flask(__name__)

pets = [
    {
        'id': 1,
        'type': u'dog'
    },
    {
        'id': 2,
        'type': u'cat'
    }
]
@app.route('/petTracking/api/v1.0/pets', methods = ['GET'])
def get_tasks():
    return jsonify({'pets': pets})


if __name__ == '__main__':
    app.run()