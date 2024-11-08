from flask import Flask, jsonify, request

app = Flask(__name__)
heart = [
    {

        "heart_id" : "123",
        "date" : ["11/8/2024"],
        "heart_rate" : ["90 beats/min"]

   
    },
        {

        "heart_id" : "124",
        "date" : ["11/8/2024"],
        "heart_rate" : ["60 beats/min"]

   
    },
    {

        "heart_id" : "125",
        "date" : ["11/8/2024"],
        "heart_rate" : ["100 beats/min"]

   
    },
]
@app.route('/heart', methods=['GET'])
def getHeart():
    return jsonify(heart)


@app.route('/heart', methods=['POST'])
def SpecificId():
    specific_heart = request.get_json()
    heart.append(specific_heart)
    return jsonify({'message':'A new patient has been added'}), 200


@app.route('/heart/<int:index>', methods=['DELETE'])
def delete_Heart(index):
    heart.pop(index)
    return 'A record has been deleted', 200



if __name__ == '__main__':
    app.run() 