from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Student Grade Calculator - Push 1 (Total & Average)"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    if not data or "marks" not in data:
        return jsonify({"error": "Please provide a list of marks"}), 400
    
    marks = data["marks"]
    if not isinstance(marks, list) or len(marks) == 0:
        return jsonify({"error": "Marks must be a non-empty list"}), 400
        
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    
    return jsonify({
        "total": total_marks,
        "average": average_marks
    })

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
