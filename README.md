# Insurance Chatbot with Flask, MySQL, and Dialogflow ES

This project demonstrates a simple chatbot built with Dialogflow ES, connected to a Flask backend that queries a MySQL database for insurance policy information.

## Features

- User queries their policy status via Dialogflow
- Flask receives the request via webhook and looks up the MySQL database
- Returns policy info: status, expiration date, and user name

---

## Requirements

- Python 3
- MySQL Server
- Ngrok
- DialogFlow ES

---

## Setup Instructions

### 1. Clone the repository
``` bash
git clone https://github.com/yourusername/insurance-chatbot.git
cd insurance-chatbot
```

### 2. 	Download the InsuranceAssistant folder and compress it into a .zip archive

- Make sure that the files agent.json and package.json and the folders intents/ and entities/ are at the root level of the zip.

### 3. 	Upload the model to DialogFlow ES

- Go to Dialogflow ES Console → Settings → Export and Import → Restore from zip.
- Upload the .zip archive you just created to import the agent.


### 4. Create and populate the MySQL database

- Log into MySQL:
```bash
mysql -u root -p
```

- Run:
```sql
CREATE DATABASE insurance;
USE insurance;
```

- Import the backup:
```sql
mysql -u root -p insurance < insurance_backup.sql
```


### 5. Run the Flask server
```bash
python app.py
```


### 6. Use Ngrok to expose your local Flask server
```bash
ngrok http 5001
```


### 7. Connect with Dialogflow

1.	Go to Dialogflow ES
2.	In your agent, go to Fulfillment → Enable Webhook
3. Copy the generated HTTPS URL from ngrok and paste it into the webhook URL field in Dialogflow Fulfillment.
4. In your Dialogflow intent, add a parameter called policy_number and ensure it's passed in the request.

### 8. Test
  1. In the Dialogflow simulator, try typing:

> What is the status of policy number 123456?

  2. Expected response:

> Thanks Mario Rossi! I've found your policy #123456. It's currently active and valid until 2026-07-15.

---

## Notes
-	app.py connects to MySQL using user root and no password by default. You can modify this in the get_policy_data() function.
-	The SQL file includes 3 sample policies.
-	This project is for demonstration purposes only.

---

## License

MIT License

Copyright (c) 2025 Alessandro Bigolin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
