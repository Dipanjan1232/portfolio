"""
================================================================================
                    DIPANJAN KHATUA - PROFESSIONAL PORTFOLIO
================================================================================
A fully functional Flask web application with:
- Neon animated design (exactly as your original HTML)
- 6 professionally formatted projects (including KrishiMitra AI with video)
- Working contact form (email via Gmail SMTP)
- Resume download
- Local images and video served via Flask routes

HOW TO RUN:
1. Install Flask: pip install flask
2. Edit the file paths below (PROFILE_PHOTO_PATH, RESUME_PATH, IMAGE_BASE_FOLDER, KRISHI_VIDEO_PATH)
3. (Optional) Set YOUR_PASSWORD to a Gmail App Password for email
4. Run: python portfolio.py
5. Open http://localhost:5000
================================================================================
"""

from flask import Flask, render_template_string, request, jsonify, send_file, abort
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# ============================================================================
# 1. CONFIGURE YOUR LOCAL FILE PATHS (EDIT THESE)
# ============================================================================
PROFILE_PHOTO_PATH = r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\WhatsApp Image 2026-05-18 at 7.29.27 PM.jpeg"
RESUME_PATH = r"D:\Dipanjan Khatua CV (1).pdf"
IMAGE_BASE_FOLDER = r"D:\Attendence management system\images"
KRISHI_VIDEO_PATH = r"C:\Users\ASUS\Videos\Screen Recordings\Screen Recording 2026-05-20 192144.mp4"

# ============================================================================
# 2. EMAIL SETUP (for contact form)
# ============================================================================
YOUR_EMAIL = "dipanjankhatua3@gmail.com"
YOUR_PASSWORD = "your_gmail_app_password_here"   # 🔴 Replace with Gmail App Password
USE_EMAIL = True   # Set False to disable email sending (for testing)

# ============================================================================
# 3. ROUTES FOR SERVING IMAGES AND VIDEO
# ============================================================================
@app.route('/images/<path:filename>')
def serve_image(filename):
    full_path = os.path.join(IMAGE_BASE_FOLDER, filename)
    if os.path.exists(full_path):
        return send_file(full_path, mimetype='image/jpeg')
    abort(404)

@app.route('/videos/<path:filename>')
def serve_video(filename):
    if filename == "krishi_mitra_demo.mp4" and os.path.exists(KRISHI_VIDEO_PATH):
        return send_file(KRISHI_VIDEO_PATH, mimetype='video/mp4')
    abort(404)

# ============================================================================
# 4. COMPLETE HTML TEMPLATE (PROFESSIONALLY FORMATTED CAPTIONS)
# ============================================================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dipanjan Khatua - Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        * {
            caret-color: transparent;
            margin: 0; padding: 0; box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }
        body {
            background: radial-gradient(circle at 20% 20%, rgba(0,255,255,0.25), transparent 40%),
                        radial-gradient(circle at 80% 80%, rgba(255,0,200,0.25), transparent 40%),
                        radial-gradient(circle at 50% 50%, rgba(0,255,150,0.2), transparent 50%),
                        linear-gradient(135deg, #000000, #020b33, #001f3f, #0a043c, #020202);
            background-size: 250% 250%;
            animation: neonBg 6s ease-in-out infinite alternate;
            color: #fff;
            overflow-x: hidden;
        }
        @keyframes neonBg {
            0% { background-position: 0% 0%; filter: brightness(0.85); }
            50% { background-position: 100% 50%; filter: brightness(1.1); }
            100% { background-position: 60% 100%; filter: brightness(1); }
        }
        header {
            position: fixed;
            width: 100%;
            top: 0;
            padding: 20px;
            backdrop-filter: blur(10px);
            background: rgba(0,0,0,0.4);
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            border-bottom: 1px solid rgba(0,255,255,0.3);
        }
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #00eaff, #ff00c8, #00ff95);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: logoGlow 2s ease-in-out infinite alternate;
            letter-spacing: 1px;
        }
        @keyframes logoGlow {
            0% { text-shadow: 0 0 8px #00eaff; transform: translateY(0); }
            50% { text-shadow: 0 0 14px #ff00c8; transform: translateY(-2px); }
            100% { text-shadow: 0 0 12px #00ff95; transform: translateY(0); }
        }
        header nav { display: flex; align-items: center; gap: 24px; }
        header ul { list-style: none; display: flex; }
        header ul li { margin-left: 30px; }
        header ul li a {
            color: #00eaff;
            text-decoration: none;
            font-weight: 600;
            transition: 0.3s;
            text-shadow: 0 0 8px #00eaff;
        }
        header ul li a:hover { color: #ff00c8; text-shadow: 0 0 10px #ff00c8; }
        .linkedin-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            background: linear-gradient(90deg, rgba(0,234,255,0.12), rgba(255,0,200,0.06));
            border: 1px solid rgba(0,234,255,0.2);
            color: #00eaff;
            text-decoration: none;
            font-weight: 600;
            border-radius: 999px;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
            font-size: 0.9rem;
        }
        .linkedin-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 18px rgba(255,0,200,0.12);
            background: linear-gradient(90deg, #00eaff, #ff00c8);
            color: #fff;
        }
        .linkedin-btn svg { width: 18px; height: 18px; }
        #hero {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding-top: 80px;
        }
        #mainName {
            font-size: 4rem;
            font-weight: 800;
            background: linear-gradient(45deg, #00eaff, #ff00c8, #00ff95);
            -webkit-text-fill-color: transparent;
            -webkit-background-clip: text;
            animation: neonGlow 1.5s infinite alternate;
        }
        @keyframes neonGlow {
            from { filter: drop-shadow(0px 0px 10px #00eaff); }
            to { filter: drop-shadow(0px 0px 20px #ff00c8); }
        }
        .hero-subtitle {
            font-size: 1.3rem;
            margin-top: 10px;
            color: #d6f6ff;
            text-shadow: 0 0 8px #00eaff;
        }
        .cta {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 30px;
            background: #00eaff;
            color: #000;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: 0.3s;
            box-shadow: 0 0 12px #00eaff;
        }
        .cta:hover { background: #ff00c8; color: #fff; box-shadow: 0 0 15px #ff00c8; }
        #about {
            padding: 100px 0;
            background: rgba(0,0,0,0.35);
            border-top: 1px solid rgba(0,255,255,0.3);
            border-bottom: 1px solid rgba(0,255,255,0.3);
        }
        #about .container {
            width: 85%;
            margin: auto;
            text-align: center;
        }
        .profile-pic {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid #00eaff;
            margin-bottom: 20px;
            box-shadow: 0 0 30px #00eaff;
            transition: 0.5s;
        }
        .profile-pic:hover {
            transform: scale(1.08);
            box-shadow: 0 0 35px #ff00c8;
        }
        .projects-list {
            list-style: none;
            padding: 0;
        }
        .project-item {
            margin-bottom: 10px;
            position: relative;
        }
        .project-link {
            color: #fff;
            text-decoration: none;
            font-weight: 600;
            cursor: pointer;
            transition: color 0.3s;
        }
        .project-link:hover {
            color: #00eaff;
        }
        .project-details {
            display: none;
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            width: 85%;
            max-width: 650px;
            background: rgba(0,0,0,0.95);
            border: 1px solid #00eaff;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 0 25px rgba(0,255,255,0.4);
            z-index: 10;
            animation: slideIn 0.4s ease-out;
            text-align: left;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-50%) translateY(-15px); }
            to { opacity: 1; transform: translateX(-50%) translateY(0); }
        }
        .project-item:hover .project-details {
            display: block;
        }
        .project-caption {
            font-size: 0.95rem;
            color: #e0f7ff;
            line-height: 1.5;
            text-shadow: 0 0 4px rgba(0,234,255,0.3);
        }
        .project-caption h4 {
            color: #00eaff;
            margin-top: 10px;
            margin-bottom: 5px;
            font-size: 1.05rem;
        }
        .project-caption ul {
            margin-left: 20px;
            margin-bottom: 10px;
        }
        .project-caption li {
            margin-bottom: 5px;
        }
        .project-images {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 15px;
        }
        .project-images img {
            width: 170px;
            height: 170px;
            object-fit: cover;
            border-radius: 12px;
            border: 2px solid #00eaff;
            transition: transform 0.3s;
        }
        .project-images img:hover {
            transform: scale(1.05);
        }
        .project-video video {
            width: 100%;
            max-width: 550px;
            border-radius: 12px;
            border: 2px solid #00eaff;
            box-shadow: 0 0 15px rgba(0,234,255,0.3);
            margin-top: 12px;
        }
        #skills {
            padding: 100px;
            text-align: center;
        }
        .skills-grid {
            display: grid;
            margin-top: 40px;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 20px;
        }
        .skill-box {
            background: rgba(0,255,255,0.1);
            padding: 20px;
            border-radius: 20px;
            font-size: 1.2rem;
            font-weight: 600;
            border: 1px solid #00eaff;
            color: #00eaff;
            text-shadow: 0 0 8px #00eaff;
            transition: 0.3s;
        }
        .skill-box:hover {
            transform: translateY(-8px);
            box-shadow: 0 0 20px #ff00c8;
            color: #ff00c8;
        }
        #achievements {
            padding: 100px;
        }
        .achievements-list {
            width: 75%;
            margin: auto;
        }
        .achievements-list li {
            background: rgba(0,255,255,0.1);
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 12px;
            font-weight: 600;
            border: 1px solid #00eaff;
            color: #d9faff;
            text-shadow: 0 0 6px #00eaff;
            transition: 0.3s;
        }
        .achievements-list li:hover {
            transform: translateX(10px);
            box-shadow: 0 0 12px #ff00c8;
            border-color: #ff00c8;
        }
        #contact {
            padding: 80px;
            text-align: center;
            color: #d7ffff;
        }
        .contact-form {
            max-width: 600px;
            margin: 30px auto;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .contact-form input, .contact-form textarea {
            background: rgba(0,0,0,0.6);
            border: 1px solid #00eaff;
            padding: 12px 18px;
            border-radius: 40px;
            color: white;
            font-size: 1rem;
            outline: none;
        }
        .contact-form input:focus, .contact-form textarea:focus {
            box-shadow: 0 0 10px #00eaff;
        }
        .contact-form button {
            background: #00eaff;
            color: black;
            border: none;
            padding: 12px;
            border-radius: 40px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            font-size: 1rem;
        }
        .contact-form button:hover {
            background: #ff00c8;
            color: white;
            box-shadow: 0 0 15px #ff00c8;
        }
        #formStatus {
            margin-top: 15px;
            font-weight: bold;
        }
        footer {
            text-align: center;
            padding: 20px;
            margin-top: 30px;
            background: rgba(0,0,0,0.7);
            border-top: 1px solid #00eaff;
            color: #9efcff;
        }
        @media (max-width: 720px) {
            #mainName { font-size: 2.2rem; }
            header ul li { margin-left: 12px; }
            .linkedin-btn { padding: 6px 8px; font-size: 0.75rem; }
            .project-details {
                position: static;
                width: 95%;
                margin: 15px auto 0;
                transform: none;
            }
            .project-item:hover .project-details {
                display: block;
            }
            #skills, #achievements { padding: 50px 20px; }
            .skills-grid { grid-template-columns: 1fr; }
            .achievements-list { width: 95%; }
        }
        hr {
            border-color: rgba(0,234,255,0.3);
            margin: 10px 0;
        }
        .tech-badge {
            display: inline-block;
            background: rgba(0,234,255,0.2);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            margin: 4px 4px 0 0;
            color: #00eaff;
        }
    </style>
</head>
<body>
<header>
    <div style="display:flex; align-items:center; gap:18px;">
        <div class="logo">Dipanjan Khatua</div>
    </div>
    <nav>
        <ul>
            <li><a href="#hero">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#achievements">Achievements</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
        <a class="linkedin-btn" href="https://www.linkedin.com/in/dipanjan-khatua-4887282a4/" target="_blank">
            <svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
                <path fill="currentColor" d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.8 0 54.3a53.85 53.85 0 01107.7 0c0 29.5-24.1 53.8-53.91 53.8zM447.9 448h-92.4V302.4c0-34.7-.7-79.4-48.4-79.4-48.4 0-55.8 37.8-55.8 76.8V448h-92.9V148.9h89.2v40.7h1.3c12.4-23.6 42.6-48.4 87.7-48.4 93.8 0 111.1 61.8 111.1 142.3V448z"/>
            </svg>
            <span>LinkedIn</span>
        </a>
    </nav>
</header>

<section id="hero">
    <div>
        <h1 id="mainName">DIPANJAN KHATUA</h1>
        <p class="hero-subtitle">Tech Enthusiast | Robotics | AI | Developer</p>
        <a href="#about" class="cta">Explore More</a>
    </div>
</section>

<section id="about">
    <div class="container">
        <img src="/profile-photo" class="profile-pic" alt="Profile Picture">
        <h2>About Me</h2>
        <p>
            I am a passionate Computer Science student with hands-on experience in Robotics, AI,
            Automation and Software Development.
        </p>
        <h2 style="margin-top:40px;">My Projects</h2>
        <ul class="projects-list">
            <!-- Project 1: KrishiMitra AI -->
            <li class="project-item">- <span class="project-link">KrishiMitra AI – Smart IoT & AI Based Farmer Support System</span>
                <div class="project-details">
                    <div class="project-caption">
                        <strong style="color:#00eaff;">🌾 KrishiMitra AI</strong> – Award-winning intelligent system for farmers.<br><br>
                        <strong>📌 Problem:</strong> Farmers lack real-time soil health data and crop disease prediction.<br>
                        <strong>💡 Solution:</strong> IoT sensors + AI that provides instant recommendations and disease detection.<br><br>                      
                        <strong>🔧 Tech Stack:</strong> ESP32, Soil NPK/pH sensors, OpenAI API, AWS Cloud, Python, Flask, OpenCV.<br>
                        <strong>✨ Features:</strong>
                        <ul>
                            <li>Real-time soil moisture, NPK, pH monitoring</li>
                            <li>AI-based crop disease detection from leaf images</li>
                            <li>Automated irrigation alerts</li>
                            <li>Voice-based advisory in regional languages</li>
                        </ul>
                    </div>
                    <div class="project-video">
                        <video controls preload="metadata">
                            <source src="/videos/krishi_mitra_demo.mp4" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                    </div>
                </div>
            </li>

            <!-- Project 2: RAKSHAK - Multipurpose Robotics System -->
            <li class="project-item">- <span class="project-link">RAKSHAK – Multi-Terrain Amphibious Defense Bot</span>
                <div class="project-details">
                    <div class="project-caption">
                        <strong style="color:#00eaff;">🚀 RAKSHAK</strong> – Made for Indian Army by Team Rudra.<br><br>
                        <strong>📌 Problem:</strong> Existing military robots are expensive, not amphibious, and have low payload.<br>
                        <strong>💡 Solution:</strong> A powerful amphibious bot that operates on land and water, carries high payload, and aids surveillance.<br><br>
                        <strong>🔧 Tech Stack:</strong> Arduino, ESP32, Motor Drivers, Python, OpenCV, Tkinter, MySQL.<br>
                        <strong>✨ Capabilities:</strong>
                        <ul>
                            <li>Multi-terrain (land + water) navigation</li>
                            <li>High payload capacity for supply delivery</li>
                            <li>Real-time video streaming</li>
                            <li>Remote controlled with long range</li>
                        </ul>
                        🇮🇳 <em>Proud to contribute to defense innovation.</em>
                    </div>
                    <div class="project-images">
                        <img src="/images/WhatsApp%20Image%202025-12-07%20at%2012.47.46%20PM.jpeg" alt="RAKSHAK 1">
                        <img src="/images/WhatsApp%20Image%202025-12-07%20at%2012.52.23%20PM.jpeg" alt="RAKSHAK 2">
                    </div>
                </div>
            </li>

            <!-- Project 3: Face Recognition Attendance System -->
            <li class="project-item">- <span class="project-link">Face Recognition Based Attendance Management System</span>
                <div class="project-details">
                    <div class="project-caption">
                        <strong style="color:#00eaff;">👤 AI-Powered Attendance System</strong><br><br>
                        <strong>📌 Problem:</strong> Manual attendance is time-consuming and prone to errors.<br>
                        <strong>💡 Solution:</strong> Real-time face detection and automated attendance logging with a full student management dashboard.<br><br>
                        <strong>🔧 Tech Stack:</strong> Python, OpenCV, Face Recognition Library, MySQL, Tkinter.<br>
                        <strong>✨ Features:</strong>
                        <ul>
                            <li>Real-time face detection and recognition</li>
                            <li>Automated attendance marking with timestamp</li>
                            <li>Student database management</li>
                            <li>Export attendance reports (CSV)</li>
                        </ul>
                        #AI #FaceRecognition #Python #OpenCV
                    </div>
                    <div class="project-images">
                        <img src="/images/Screenshot%202025-08-05%20103544.png" alt="FaceRec 1">
                        <img src="/images/Screenshot%202025-05-05%20194733.png" alt="FaceRec 2">
                    </div>
                </div>
            </li>


            <!-- Project 5: Waste Segregation Monitoring System -->
            <li class="project-item">- <span class="project-link">IoT-Based Smart Waste Segregation System</span>
                <div class="project-details">
                    <div class="project-caption">
                        <strong style="color:#00eaff;">♻️ Smart Waste Management for Cleaner Cities</strong><br><br>
                        <strong>📌 Problem:</strong> Manual waste segregation is inefficient and unhygienic.<br>
                        <strong>💡 Solution:</strong> IoT-enabled bin that automatically separates wet and dry waste and sends real-time fill-level data to the cloud.<br><br>
                        <strong>🔧 Tech Stack:</strong> ESP8266, Moisture sensors, Servo motors, Blynk/ThingSpeak, Arduino IDE.<br>
                        <strong>✨ Features:</strong>
                        <ul>
                            <li>Automatic wet/dry waste separation</li>
                            <li>Real-time bin fill level monitoring</li>
                            <li>Cloud dashboard for municipal authorities</li>
                            <li>SMS/email alerts when bin is full</li>
                        </ul>
                        #IoT #SmartCity #Sustainability
                    </div>
                    <div class="project-images">
                        <img src="/images/Dustbin.jpeg" alt="Waste Segregation 1">
                        <img src="/images/1764569282581.jpeg" alt="Waste Segregation 2">
                    </div>
                </div>
            </li>

            <!-- Project 6: Autonomous Line-Following Robot -->
            <li class="project-item">- <span class="project-link">Autonomous Line-Following Robot</span>
                <div class="project-details">
                    <div class="project-caption">
                        <strong style="color:#00eaff;">🤖 Precision Line Follower Robot</strong><br><br>
                        <strong>📌 Problem:</strong> Understanding autonomous navigation fundamentals.<br>
                        <strong>💡 Solution:</strong> Built an Arduino-based robot that detects and follows a line with high accuracy.<br><br>
                        <strong>🔧 Tech Stack:</strong> Arduino UNO, IR sensor array, L298N motor driver, DC motors.<br>
                        <strong>✨ Learnings:</strong>
                        <ul>
                            <li>Embedded systems and sensor calibration</li>
                            <li>PID logic for smooth path following</li>
                            <li>Motor control and speed regulation</li>
                        </ul>
                        <em>This project laid the foundation for advanced robotics and autonomous vehicles.</em><br>
                        #Arduino #LineFollower #Robotics
                    </div>
                    <div class="project-images">
                        <img src="/images/1745818860109.jpeg" alt="Line Follower 1">
                        <img src="/images/1745818859975.jpeg" alt="Line Follower 2">
                    </div>
                </div>
            </li>
        </ul>
    </div>
</section>

<section id="skills">
    <h2>My Skills</h2>
    <div class="skills-grid">
        <div class="skill-box">C / C++</div>
        <div class="skill-box">Python</div>
        <div class="skill-box">SQL / MySQL</div>
        <div class="skill-box">JavaScript</div>
        <div class="skill-box">HTML5 / CSS3</div>
        <div class="skill-box">Flask / Django</div>
        <div class="skill-box">OpenCV</div>
        <div class="skill-box">IoT / Arduino</div>
        <div class="skill-box">Git & GitHub</div>
        <div class="skill-box">REST APIs</div>
    </div>
</section>

<section id="achievements">
    <h2 style="text-align:center;">🏆 Achievements</h2>
    <ul class="achievements-list">
        <li>🥇 1st Place – IEEE R10 Robotics Competition 2025 </li>
        <li>🥇 1st Place – Roborace in srijan techfest in Jadavpur University</li>
        <li>🥇 1st Place – Line Follower in Tronix in The Neotia university</li>
        <li>🥇 1st Place – Roborace in Sankalp innovation fest in The Neotia Univesity</li>
        <li>🥇 1st Place – Hackathon (Parikalpana Tech Fest)</li>
        <li>🥇 1st Place – Project showcase in Sankalp innovation fest in The Neotia University</li>
        <li>🥈 2nd Place – Robo Race in Innovacion in IEM Tech Fest</li>
    </ul>
</section>

<section id="contact">
    <h2>Contact Me</h2>
    <form id="contactForm" class="contact-form">
        <input type="text" id="name" placeholder="Your Full Name" required>
        <input type="email" id="email" placeholder="Your Email Address" required>
        <textarea id="message" rows="5" placeholder="Your Message..." required></textarea>
        <button type="submit">Send Message ✉️</button>
    </form>
    <div id="formStatus"></div>
    <p style="margin-top: 25px;">📧 <b style="color:#00eaff;">dipanjankhatua3@gmail.com</b> &nbsp; | &nbsp;
    📞 <b style="color:#ff00c8;">+91 6006381851</b></p>
</section>

<footer>
    © 2025 Dipanjan Khatua | All Rights Reserved
</footer>

<script>
    document.getElementById('contactForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;
        const statusDiv = document.getElementById('formStatus');
        statusDiv.innerHTML = "Sending...";
        statusDiv.style.color = "#00eaff";
        try {
            const response = await fetch('/send_message', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, message })
            });
            const data = await response.json();
            if (response.ok) {
                statusDiv.innerHTML = "✅ Message sent successfully! I'll get back to you soon.";
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

# ============================================================================
# 5. FLASK ROUTES
# ============================================================================
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/profile-photo')
def profile_photo():
    if os.path.exists(PROFILE_PHOTO_PATH):
        return send_file(PROFILE_PHOTO_PATH, mimetype='image/jpeg')
    return "Profile photo not found", 404

@app.route('/resume')
def download_resume():
    if os.path.exists(RESUME_PATH):
        return send_file(RESUME_PATH, as_attachment=True)
    return "Resume not found", 404

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
        return jsonify({'success': True, 'note': 'Email disabled but message logged.'})
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
        return jsonify({'error': 'Failed to send email. Check server logs.'}), 500

# ============================================================================
# 6. RUN THE APPLICATION
# ============================================================================
if __name__ == '__main__':
    print("=" * 65)
    print("🚀 PORTFOLIO IS RUNNING AT: http://localhost:5000")
    print("📌 MAKE SURE THE FOLLOWING FILES EXIST (edit paths if needed):")
    print(f"   Profile photo: {PROFILE_PHOTO_PATH}")
    print(f"   Resume PDF: {RESUME_PATH}")
    print(f"   Image folder: {IMAGE_BASE_FOLDER}")
    print(f"   KrishiMitra video: {KRISHI_VIDEO_PATH}")
    print("📧 TO ENABLE EMAIL: Replace YOUR_PASSWORD with a Gmail App Password")
    print("=" * 65)
    

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)