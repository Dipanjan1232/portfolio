# portfolio.py - Complete Portfolio with Local Image & Resume Paths
# Run: python portfolio.py

from flask import Flask, render_template_string, request, jsonify, send_file
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# ================= YOUR LOCAL FILE PATHS =================
PROFILE_PHOTO_PATH = r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\WhatsApp Image 2026-05-18 at 7.29.27 PM.jpeg"
RESUME_PATH = r"D:\Dipanjan Khatua CV (1).pdf"

# ================= EMAIL SETUP =================
YOUR_EMAIL = "dipanjankhatua3@gmail.com"
YOUR_PASSWORD = "YOUR_APP_PASSWORD_HERE"  # Change to your Gmail App Password
USE_EMAIL = True  # Set False to disable email

# ================= HTML TEMPLATE =================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dipanjan Khatua | Fullstack & AI Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a192f, #0b2b3b, #0f3b4a);
            color: #e6f1ff;
            line-height: 1.6;
        }
        .container {
            max-width: 1200px;
            margin: auto;
            padding: 0 20px;
        }
        /* Glassmorphism effect */
        .glass {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(12px);
            border-radius: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        header {
            text-align: center;
            padding: 50px 0 30px;
        }
        .profile-pic {
            width: 170px;
            height: 170px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #64ffda;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            transition: transform 0.3s;
        }
        .profile-pic:hover {
            transform: scale(1.02);
        }
        h1 {
            font-size: 2.8rem;
            margin-top: 20px;
            background: linear-gradient(135deg, #64ffda, #00b4d8);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .tagline {
            font-size: 1.3rem;
            color: #ccd6f6;
            margin-bottom: 20px;
            font-weight: 300;
        }
        .bio {
            max-width: 800px;
            margin: 0 auto 25px;
            font-size: 1rem;
            background: rgba(100,255,218,0.1);
            padding: 20px;
            border-radius: 20px;
            border-left: 4px solid #64ffda;
        }
        .btn-resume {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: #64ffda;
            color: #0a192f;
            padding: 12px 28px;
            border-radius: 40px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 0 4px 12px rgba(100,255,218,0.3);
        }
        .btn-resume:hover {
            background: #00b4d8;
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,180,216,0.4);
        }
        section {
            margin: 40px 0;
            padding: 30px;
            background: rgba(10,25,47,0.6);
            backdrop-filter: blur(8px);
            border-radius: 25px;
            transition: 0.3s;
            border: 1px solid rgba(100,255,218,0.2);
        }
        section:hover {
            border-color: #64ffda;
            box-shadow: 0 5px 15px rgba(100,255,218,0.1);
        }
        h2 {
            font-size: 1.8rem;
            color: #64ffda;
            border-left: 5px solid #64ffda;
            padding-left: 20px;
            margin-bottom: 25px;
        }
        .skills-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }
        .skill {
            background: rgba(100,255,218,0.15);
            padding: 8px 22px;
            border-radius: 40px;
            font-size: 0.95rem;
            font-weight: 500;
            color: #64ffda;
            transition: 0.2s;
        }
        .skill:hover {
            background: #64ffda;
            color: #0a192f;
            transform: scale(1.02);
        }
        .project {
            background: rgba(255,255,255,0.03);
            padding: 20px;
            margin-bottom: 25px;
            border-radius: 18px;
            border-left: 4px solid #64ffda;
            transition: 0.2s;
        }
        .project:hover {
            background: rgba(100,255,218,0.05);
            transform: translateX(5px);
        }
        .project h3 {
            color: #64ffda;
            margin-bottom: 10px;
        }
        .cert {
            background: rgba(0,180,216,0.1);
            padding: 12px 18px;
            margin: 12px 0;
            border-radius: 12px;
            font-weight: 500;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid rgba(100,255,218,0.4);
            border-radius: 12px;
            background: rgba(10,25,47,0.8);
            color: #fff;
            font-size: 1rem;
        }
        .contact-form input:focus, .contact-form textarea:focus {
            outline: none;
            border-color: #64ffda;
            box-shadow: 0 0 8px #64ffda;
        }
        .contact-form button {
            background: #64ffda;
            color: #0a192f;
            padding: 12px 28px;
            border: none;
            border-radius: 40px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }
        .contact-form button:hover {
            background: #00b4d8;
            color: white;
        }
        footer {
            text-align: center;
            padding: 25px;
            margin-top: 40px;
            background: rgba(0,0,0,0.4);
            border-radius: 20px 20px 0 0;
        }
        a {
            color: #64ffda;
            text-decoration: none;
            transition: 0.2s;
        }
        a:hover {
            color: #00b4d8;
            text-decoration: underline;
        }
        @media (max-width: 768px) {
            h1 { font-size: 2rem; }
            .tagline { font-size: 1rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <img src="/profile-photo" alt="Dipanjan Khatua" class="profile-pic">
            <h1>Dipanjan Khatua</h1>
            <div class="tagline">Fullstack Developer | AI Enthusiast | Problem Solver</div>
            <div class="bio">
                "I am Dipanjan Khatua – a problem solver at heart. I love turning ideas into reality using code. 
                My expertise lies in Python, DBMS, IoT, and AI. I won the IEEE R10 Robotics Competition with my army robot 'Rakshak', 
                and my AI project 'Krishi Mitra' emerged as the winner at the Agrinova National Hackathon. 
                Every line of code I write is driven by one goal: to build technology that makes a real difference."
            </div>
            <a href="/resume" download class="btn-resume">📄 Download Resume</a>
        </header>

        <section>
            <h2>⚙️ Technical Skills</h2>
            <div class="skills-grid">
                <span class="skill">Python</span>
                <span class="skill">SQL / MySQL</span>
                <span class="skill">HTML / CSS / JS</span>
                <span class="skill">Flask / Django</span>
                <span class="skill">OpenCV</span>
                <span class="skill">IoT / Arduino</span>
                <span class="skill">Git / GitHub</span>
                <span class="skill">Power BI</span>
                <span class="skill">Java</span>
            </div>
        </section>

        <section>
            <h2>🚀 Featured Projects</h2>
            <div class="project">
                <h3>🤖 Rakshak – Multi-terrain Army Robot</h3>
                <p><strong>Tech:</strong> Arduino IDE, Python, OpenCV, ESP32, Motor Drivers, Tkinter, MySQL, NumPy</p>
                <p><strong>Role:</strong> Design, Software & Circuit Lead</p>
                <p><strong>Impact:</strong> IEEE R10 Robotics Competition Winner – Amphibious bot for supply delivery in bunkers and disaster zones.</p>
            </div>
            <div class="project">
                <h3>🌾 Krishi Mitra AI – Smart Agricultural Support System</h3>
                <p><strong>Tech:</strong> ESP32, Soil/NPK/pH sensors, OpenAI API, AWS Cloud, Python, Image Processing</p>
                <p><strong>Role:</strong> Team Leader</p>
                <p><strong>Impact:</strong> Agrinova National Hackathon Winner. IoT+AI system for real-time soil advice and crop disease detection.</p>
            </div>
        </section>

        <section>
            <h2>📜 Certifications</h2>
            <div class="cert">✅ Java Developer Certification – Issued April 27, 2026</div>
            <div class="cert">✅ Power BI Workshop Certificate</div>
        </section>

        <section>
            <h2>🎓 Education</h2>
            <p><strong>The Neotia University</strong> – BCA, 3rd Year | CGPA: 7.43 | Graduation: 2026</p>
        </section>

        <section>
            <h2>📬 Contact Me</h2>
            <form id="contactForm" class="contact-form">
                <input type="text" id="name" placeholder="Your Name" required>
                <input type="email" id="email" placeholder="Your Email" required>
                <textarea id="message" rows="5" placeholder="Your Message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
            <div id="formStatus" style="margin-top: 12px; color: #64ffda;"></div>
            <div style="margin-top: 25px;">
                📧 <a href="mailto:dipanjankhatua3@gmail.com">dipanjankhatua3@gmail.com</a><br>
                📞 <a href="tel:+916006381851">+91 6006381851</a><br>
                📍 Chandipur, Purba Medinipur, West Bengal - 721659<br>
                🐙 <a href="https://github.com/Dipanjan1232" target="_blank">GitHub</a> &nbsp;|&nbsp;
                🔗 <a href="https://www.linkedin.com/in/dipanjan-khatua-4887282a4" target="_blank">LinkedIn</a>
            </div>
        </section>

        <footer>
            © 2026 Dipanjan Khatua | Built with 💙 for Fullstack & AI
        </footer>
    </div>

    <script>
        document.getElementById('contactForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            const statusDiv = document.getElementById('formStatus');
            statusDiv.innerHTML = "Sending...";
            try {
                const response = await fetch('/send_message', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, email, message })
                });
                const data = await response.json();
                if (response.ok) {
                    statusDiv.innerHTML = "✅ Message sent successfully!";
                    document.getElementById('contactForm').reset();
                } else {
                    statusDiv.innerHTML = "❌ Error: " + data.error;
                }
            } catch (err) {
                statusDiv.innerHTML = "❌ Network error. Please try again.";
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/profile-photo')
def profile_photo():
    # Serve the image from absolute path
    return send_file(PROFILE_PHOTO_PATH, mimetype='image/jpeg')

@app.route('/resume')
def download_resume():
    # Serve resume from absolute path
    return send_file(RESUME_PATH, as_attachment=True)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if not name or not email or not message:
        return jsonify({'error': 'All fields required'}), 400
    
    if not USE_EMAIL:
        print(f"Message from {name} ({email}): {message}")
        return jsonify({'success': True, 'note': 'Email disabled but message saved.'})
    
    try:
        msg = EmailMessage()
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg['Subject'] = f"Portfolio Contact from {name}"
        msg['From'] = YOUR_EMAIL
        msg['To'] = YOUR_EMAIL
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(YOUR_EMAIL, YOUR_PASSWORD)
            smtp.send_message(msg)
        
        return jsonify({'success': True})
    except Exception as e:
        print("Email error:", e)
        return jsonify({'error': 'Failed to send email. Check password or set USE_EMAIL=False'}), 500

if __name__ == '__main__':
    print("="*55)
    print("🚀 Portfolio is running at http://localhost:5000")
    print("📌 Make sure the following files exist:")
    print(f"   Profile photo: {PROFILE_PHOTO_PATH}")
    print(f"   Resume PDF: {RESUME_PATH}")
    print("📧 To enable email, set YOUR_PASSWORD = your Gmail App Password")
    print("="*55)
    app.run(debug=True, host='0.0.0.0', port=5000)