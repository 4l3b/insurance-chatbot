from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_policy_data(policy_number):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="insurance"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM policies WHERE policy_number = %s", (policy_number,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    policy_number = req['queryResult']['parameters'].get('policy_number')

    policy = get_policy_data(policy_number)

    if policy:
        response_text = (
            f"Thanks {policy['user_name']}! I’ve found your policy #{policy_number}. "
            f"It’s currently {policy['status']} and valid until {policy['expiry_date']}."
        )
    else:
        response_text = (
            f"Sorry, I couldn’t find a policy with number #{policy_number}. "
            f"Please check the number and try again."
        )

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)