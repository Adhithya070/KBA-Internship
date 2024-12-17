from flask import Flask, request, jsonify

app = Flask(__name__)

votes = {"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}

@app.route('/api/vote', methods=['POST'])
def submit_vote():
    data = request.json  
    candidate = data.get("candidate")  

    if candidate in votes:  
        votes[candidate] += 1  
        return jsonify({
            "message": f"Vote cast for {candidate}",
            "status": "success"
        }), 200
    else:
        return jsonify({
            "message": "Invalid candidate",
            "status": "error"
        }), 400


@app.route('/api/results', methods=['GET'])
def get_results():
    return jsonify(votes), 200  

if __name__ == '__main__':
    app.run(debug=True, port=5000)
