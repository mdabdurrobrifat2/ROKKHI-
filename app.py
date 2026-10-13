from flask import Flask, request, redirect

app = Flask(__name__)

# এখানে সব Donor জমা হবে
donors = []

@app.route('/')
def home():
    return '''
    <html><body style="background:#0a192f;color:white;font-family:sans-serif;padding:20px;text-align:center">
    <h1 style="color:#00FF88">ROKKHI - AI POWERED NATIONAL SOC</h1>
    <p style="letter-spacing:3px;color:#aaa">রক্ষী - AI POWERED NATIONAL SOC</p>
    <div style="margin-top:30px">
        <a href="/blood" style="background:#00FF88;color:black;padding:15px 30px;text-decoration:none;border-radius:10px;font-weight:bold">GO TO BLOOD DONOR LIST</a>
    </div>
    <div style="padding:20px;display:grid;gap:15px;margin-top:30px;text-align:left">
        <div style="background:#162040;padding:20px;border-radius:15px;border-left:4px solid #00FF88">
            <h3>🛡️ SYSTEM STATUS: SECURE</h3>
            <p style="color:#00FF88">● All National Assets Protected</p>
            <p>Threats Blocked Today: 1,247</p>
        </div>
    </div>
    <p style="margin-top:40px;color:#555">Developed for Bangladesh Army<br>By: Mulaid, Dhaka | Prototype v1.0</p>
    </body></html>
    '''

@app.route('/blood', methods=['GET', 'POST'])
def blood():
    global donors
    if request.method == 'POST':
        name = request.form.get('name')
        blood_group = request.form.get('blood_group')
        phone = request.form.get('phone')
        location = request.form.get('location')
        if name and blood_group:
            donors.append({'name': name, 'blood_group': blood_group, 'phone': phone, 'location': location})
        return redirect('/blood')

    # donor list html
    donor_html = ""
    if not donors:
        donor_html = "<p style='color:#aaa;text-align:center'>কোনো Donor নেই। নিচে ফর্ম থেকে এড করুন।</p>"
    else:
        for d in donors:
            donor_html += f'''
            <div style="background:#162040;padding:15px;border-radius:10px;margin-bottom:10px;border-left:4px solid #ff4444">
                <h3 style="margin:0;color:#00FF88">{d['name']} - {d['blood_group']}</h3>
                <p style="margin:5px 0">📞 {d['phone']} | 📍 {d['location']}</p>
            </div>
            '''

    return f'''
    <html><body style="background:#0a192f;color:white;font-family:sans-serif;padding:20px">
    <a href="/" style="color:#00FF88;text-decoration:none">← Back Home</a>
    <h1 style="text-align:center;color:#ff4444">🩸 Blood Donor List</h1>
    
    <div style="max-width:600px;margin:auto">
        {donor_html}
        
        <div style="background:#162040;padding:20px;border-radius:15px;margin-top:30px">
            <h3>Add New Donor</h3>
            <form method="POST" style="display:grid;gap:10px">
                <input name="name" placeholder="নাম" required style="padding:12px;border-radius:8px;border:none">
                <select name="blood_group" required style="padding:12px;border-radius:8px;border:none">
                    <option value="">Blood Group</option>
                    <option>A+</option><option>A-</option><option>B+</option><option>B-</option>
                    <option>O+</option><option>O-</option><option>AB+</option><option>AB-</option>
                </select>
                <input name="phone" placeholder="ফোন নাম্বার" required style="padding:12px;border-radius:8px;border:none">
                <input name="location" placeholder="লোকেশন (যেমন: Dhaka)" required style="padding:12px;border-radius:8px;border:none">
                <button type="submit" style="padding:12px;background:#00FF88;border:none;border-radius:8px;font-weight:bold;cursor:pointer">ADD DONOR</button>
            </form>
        </div>
    </div>
    </body></html>
    '''

app.run(host='0.0.0.0', port=5000)
