from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ROKKHI - National SOC</title>
</head>
<body style='margin:0;background:#0A0F1E;color:white;font-family:sans-serif'>
<div style='background:#0f1a33;padding:20px;text-align:center;border-bottom:2px solid #00FF88'>
    <h1 style='color:#00FF88;margin:0;font-size:40px;letter-spacing:2px'>ROKKHI</h1>
    <p style='letter-spacing:3px;color:#aaa'>রক্ষী - AI POWERED NATIONAL SOC</p>
</div>

<div style='padding:20px;display:grid;gap:15px'>
    <div style='background:#162040;padding:20px;border-radius:15px;border-left:4px solid #00FF88'>
        <h3>🛡️ SYSTEM STATUS: SECURE</h3>
        <p style='color:#00FF88'>● All National Assets Protected</p>
        <p>Threats Blocked Today: 1,247</p>
    </div>
    
    <div style='background:#162040;padding:20px;border-radius:15px;border-left:4px solid #ff4444'>
        <h3>🚨 LIVE THREAT FEED</h3>
        <p>⚠️ DDoS Attempt on NDC - BLOCKED</p>
        <p>⚠️ Phishing on Govt Domain - BLOCKED</p>
        <p style='color:#aaa'>Last Update: Just Now</p>
    </div>

    <div style='background:#162040;padding:20px;border-radius:15px'>
        <h3>📊 AI ANALYSIS</h3>
        <p>ROKKHI AI is monitoring 14,500+ Govt IPs in real-time.</p>
        <button style='width:100%;padding:15px;background:#00FF88;border:none;border-radius:10px;font-weight:bold;font-size:16px'>RUN DEEP SCAN</button>
    </div>
</div>

<div style='text-align:center;padding:20px;color:#555'>
    <p>Developed for Bangladesh Army</p>
    <p>By: Mulaid, Dhaka | Prototype v1.0</p>
</div>
</body>
</html>
    """

@app.route('/blood')
def blood():
    return """
    <h1 style='color:#00FF88;background:#0A0F1E;padding:20px;'>Blood Donor List</h1>
    ...
    """

app.run(host='0.0.0.0', port=5000)
