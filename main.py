from flask import Flask, request, render_template

app = Flask(__name__)

memory = {}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    
    if user_input in memory:
        response = memory[user_input]
    elif "ঘোরে" in user_input:
        response = "পৃথিবী সূর্যকে ঘিরে ঘোরে মহাকর্ষের কারণে।"
    else:
        response = "আমি জানি না। তুমি কি আমাকে শেখাবে?"

    return {'reply': response}

@app.route('/teach', methods=['POST'])
def teach():
    q = request.form['question']
    a = request.form['answer']
    memory[q] = a
    return {'reply': f"ঠিক করে শিখে নিলাম:\n❓ {q}\n✅ {a}"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
