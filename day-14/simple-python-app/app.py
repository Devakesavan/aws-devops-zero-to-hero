from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template with DevOps theme
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            line-height: 1.6;
            color: #00ff41;
            background: #0d1117;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Matrix rain effect */
        .matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.1;
        }

        /* Header Styles */
        header {
            background: rgba(13, 17, 23, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 2px solid #00ff41;
            box-shadow: 0 2px 20px rgba(0, 255, 65, 0.3);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: #00ff41;
            text-decoration: none;
            text-shadow: 0 0 10px #00ff41;
            font-family: 'Courier New', monospace;
        }

        .logo::before {
            content: '$ ';
            color: #ff6b35;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: #00ff41;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            position: relative;
            padding: 5px 10px;
            border: 1px solid transparent;
        }

        .nav-links a:hover {
            border: 1px solid #00ff41;
            box-shadow: 0 0 15px rgba(0, 255, 65, 0.5);
            background: rgba(0, 255, 65, 0.1);
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: #00ff41;
            position: relative;
            background: radial-gradient(circle at 50% 50%, rgba(0, 255, 65, 0.1) 0%, transparent 70%);
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .terminal-window {
            background: #0d1117;
            border: 2px solid #00ff41;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 0 30px rgba(0, 255, 65, 0.3);
            max-width: 800px;
        }

        .terminal-header {
            display: flex;
            gap: 10px;
            margin-bottom: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #00ff41;
        }

        .terminal-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }

        .dot-red { background: #ff5f56; }
        .dot-yellow { background: #ffbd2e; }
        .dot-green { background: #27ca3f; }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            opacity: 0;
            animation: typewriter 2s steps(20) 0.5s forwards;
            font-family: 'Courier New', monospace;
            border-right: 2px solid #00ff41;
            white-space: nowrap;
            overflow: hidden;
        }

        @keyframes typewriter {
            from { width: 0; opacity: 1; }
            to { width: 100%; opacity: 1; }
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0;
            animation: fadeIn 1s ease 2.5s forwards;
            color: #8cc8ff;
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }

        .btn {
            display: inline-block;
            padding: 15px 30px;
            background: transparent;
            color: #00ff41;
            text-decoration: none;
            border: 2px solid #00ff41;
            border-radius: 4px;
            font-weight: bold;
            transition: all 0.3s ease;
            font-family: 'Courier New', monospace;
            opacity: 0;
            animation: fadeIn 1s ease 3s forwards;
            margin: 0 10px;
        }

        .btn:hover {
            background: #00ff41;
            color: #0d1117;
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.5);
            transform: translateY(-2px);
        }

        .btn-secondary {
            border-color: #ff6b35;
            color: #ff6b35;
        }

        .btn-secondary:hover {
            background: #ff6b35;
            color: #0d1117;
            box-shadow: 0 0 20px rgba(255, 107, 53, 0.5);
        }

        /* DevOps Tools Section */
        .tools {
            padding: 100px 0;
            background: linear-gradient(45deg, #161b22 0%, #0d1117 100%);
        }

        .tools h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #00ff41;
            font-family: 'Courier New', monospace;
        }

        .tools h2::before {
            content: '# ';
            color: #ff6b35;
        }

        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .tool-card {
            background: #161b22;
            padding: 2rem;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #30363d;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .tool-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00ff41, transparent);
            transition: left 0.5s ease;
        }

        .tool-card:hover::before {
            left: 100%;
        }

        .tool-card:hover {
            border-color: #00ff41;
            box-shadow: 0 10px 30px rgba(0, 255, 65, 0.2);
            transform: translateY(-5px);
        }

        .tool-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #00ff41, #8cc8ff);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1rem;
            font-size: 2rem;
            color: #0d1117;
            font-weight: bold;
        }

        .tool-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #00ff41;
            font-family: 'Courier New', monospace;
        }

        .tool-card p {
            color: #8cc8ff;
            line-height: 1.6;
        }

        /* Pipeline Section */
        .pipeline {
            padding: 100px 0;
            background: #0d1117;
            color: #00ff41;
        }

        .pipeline-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .pipeline-text h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            font-family: 'Courier New', monospace;
        }

        .pipeline-text h2::before {
            content: '> ';
            color: #ff6b35;
        }

        .pipeline-text p {
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 1.5rem;
            color: #8cc8ff;
        }

        .pipeline-visual {
            background: #161b22;
            border: 2px solid #30363d;
            border-radius: 8px;
            padding: 2rem;
            position: relative;
        }

        .pipeline-step {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
            padding: 10px;
            background: rgba(0, 255, 65, 0.1);
            border-left: 3px solid #00ff41;
            border-radius: 4px;
        }

        .step-icon {
            margin-right: 1rem;
            font-size: 1.2rem;
        }

        .step-text {
            font-family: 'Courier New', monospace;
            color: #00ff41;
        }

        /* Metrics Section */
        .metrics {
            padding: 100px 0;
            background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        }

        .metrics h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #00ff41;
            font-family: 'Courier New', monospace;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }

        .metric-card {
            background: #0d1117;
            border: 2px solid #00ff41;
            border-radius: 8px;
            padding: 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .metric-number {
            font-size: 3rem;
            font-weight: bold;
            color: #00ff41;
            font-family: 'Courier New', monospace;
            text-shadow: 0 0 10px #00ff41;
        }

        .metric-label {
            color: #8cc8ff;
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }

        /* Footer */
        footer {
            background: #0d1117;
            color: #00ff41;
            text-align: center;
            padding: 3rem 0;
            border-top: 2px solid #30363d;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .footer-section h3 {
            margin-bottom: 1rem;
            font-family: 'Courier New', monospace;
        }

        .footer-section p, .footer-section a {
            color: #8cc8ff;
            text-decoration: none;
            line-height: 1.8;
        }

        .footer-section a:hover {
            color: #00ff41;
            text-shadow: 0 0 5px #00ff41;
        }

        .social-links {
            margin: 2rem 0;
        }

        .social-links a {
            color: #00ff41;
            font-size: 1.5rem;
            margin: 0 1rem;
            transition: all 0.3s ease;
        }

        .social-links a:hover {
            transform: translateY(-3px);
            text-shadow: 0 0 15px #00ff41;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                font-size: 2rem;
            }

            .pipeline-content {
                grid-template-columns: 1fr;
            }

            .tools-grid {
                grid-template-columns: 1fr;
            }

            .metrics-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        /* Scroll animations */
        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease;
        }

        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Code block styling */
        .code-block {
            background: #0d1117;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 1rem;
            margin: 1rem 0;
            font-family: 'Courier New', monospace;
            color: #00ff41;
            overflow-x: auto;
        }

        .code-block::before {
            content: '$ ';
            color: #ff6b35;
        }
    </style>
</head>
<body>
    <canvas class="matrix-bg" id="matrix"></canvas>
    
    <header>
        <nav class="container">
            <a href="#" class="logo">{{ company_name }}</a>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#tools">Tools</a></li>
                <li><a href="#pipeline">Pipeline</a></li>
                <li><a href="#metrics">Metrics</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="home" class="hero">
        <div class="hero-content">
            <div class="terminal-window">
                <div class="terminal-header">
                    <div class="terminal-dot dot-red"></div>
                    <div class="terminal-dot dot-yellow"></div>
                    <div class="terminal-dot dot-green"></div>
                </div>
                <h1>DevOps Excellence</h1>
                <p>Streamline your development lifecycle with cutting-edge automation and monitoring</p>
                <div class="code-block">kubectl get pods --all-namespaces</div>
                <a href="#tools" class="btn">Explore Tools</a>
                <a href="#pipeline" class="btn btn-secondary">View Pipeline</a>
            </div>
        </div>
    </section>

    <section id="tools" class="tools">
        <div class="container">
            <h2 class="fade-in">DevOps Toolkit</h2>
            <div class="tools-grid">
                <div class="tool-card fade-in">
                    <div class="tool-icon">🐳</div>
                    <h3>Docker</h3>
                    <p>Containerization platform for consistent deployments across environments with lightweight, portable containers.</p>
                </div>
                <div class="tool-card fade-in">
                    <div class="tool-icon">☸️</div>
                    <h3>Kubernetes</h3>
                    <p>Container orchestration at scale with automated deployment, scaling, and management of containerized applications.</p>
                </div>
                <div class="tool-card fade-in">
                    <div class="tool-icon">🔧</div>
                    <h3>Jenkins</h3>
                    <p>Continuous integration and deployment automation with powerful pipeline capabilities and extensive plugin ecosystem.</p>
                </div>
                <div class="tool-card fade-in">
                    <div class="tool-icon">📊</div>
                    <h3>Prometheus</h3>
                    <p>Advanced monitoring and alerting toolkit with time-series database and powerful query language.</p>
                </div>
                <div class="tool-card fade-in">
                    <div class="tool-icon">🏗️</div>
                    <h3>Terraform</h3>
                    <p>Infrastructure as Code for provisioning and managing cloud resources with declarative configuration files.</p>
                </div>
                <div class="tool-card fade-in">
                    <div class="tool-icon">🔄</div>
                    <h3>Ansible</h3>
                    <p>Configuration management and automation platform for deploying applications and managing systems at scale.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="pipeline" class="pipeline">
        <div class="container">
            <div class="pipeline-content">
                <div class="pipeline-text fade-in">
                    <h2>CI/CD Pipeline</h2>
                    <p>Automated continuous integration and deployment pipeline that ensures code quality, security, and rapid delivery.</p>
                    <p>From commit to production in minutes, not hours. Our pipeline includes automated testing, security scanning, and zero-downtime deployments.</p>
                    <a href="#metrics" class="btn">View Metrics</a>
                </div>
                <div class="pipeline-visual fade-in">
                    <div class="pipeline-step">
                        <span class="step-icon">📝</span>
                        <span class="step-text">Code Commit</span>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-icon">🔍</span>
                        <span class="step-text">Automated Testing</span>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-icon">🛡️</span>
                        <span class="step-text">Security Scan</span>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-icon">🏗️</span>
                        <span class="step-text">Build & Package</span>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-icon">🚀</span>
                        <span class="step-text">Deploy to Production</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="metrics" class="metrics">
        <div class="container">
            <h2 class="fade-in">Performance Metrics</h2>
            <div class="metrics-grid">
                <div class="metric-card fade-in">
                    <div class="metric-number">99.9%</div>
                    <div class="metric-label">Uptime</div>
                </div>
                <div class="metric-card fade-in">
                    <div class="metric-number">15s</div>
                    <div class="metric-label">Deploy Time</div>
                </div>
                <div class="metric-card fade-in">
                    <div class="metric-number">50+</div>
                    <div class="metric-label">Daily Deployments</div>
                </div>
                <div class="metric-card fade-in">
                    <div class="metric-number">0</div>
                    <div class="metric-label">Downtime Events</div>
                </div>
            </div>
        </div>
    </section>

    <footer id="contact">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>DevOps Services</h3>
                    <p>Infrastructure Automation</p>
                    <p>CI/CD Pipeline Setup</p>
                    <p>Container Orchestration</p>
                    <p>Monitoring & Alerting</p>
                </div>
                <div class="footer-section">
                    <h3>Technologies</h3>
                    <p>AWS, Azure, GCP</p>
                    <p>Docker & Kubernetes</p>
                    <p>Jenkins, GitLab CI</p>
                    <p>Terraform, Ansible</p>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <p>devops@{{ company_name|lower }}.com</p>
                    <p>+1 (555) 123-4567</p>
                    <p>24/7 Support Available</p>
                </div>
            </div>
            <div class="social-links">
                <a href="#">🐙</a>
                <a href="#">💼</a>
                <a href="#">📧</a>
                <a href="#">🐦</a>
            </div>
            <p>&copy; 2025 {{ company_name }}. All rights reserved. | DevOps Excellence</p>
        </div>
    </footer>

    <script>
        // Matrix rain effect
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%+-/~{[|`]}";
        const matrixArray = matrix.split("");

        const fontSize = 10;
        const columns = canvas.width / fontSize;

        const drops = [];
        for (let x = 0; x < columns; x++) {
            drops[x] = 1;
        }

        function drawMatrix() {
            ctx.fillStyle = 'rgba(13, 17, 23, 0.04)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#00ff41';
            ctx.font = fontSize + 'px monospace';

            for (let i = 0; i < drops.length; i++) {
                const text = matrixArray[Math.floor(Math.random() * matrixArray.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }

        setInterval(drawMatrix, 35);

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.fade-in').forEach(el => {
            observer.observe(el);
        });

        // Resize canvas on window resize
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, 
                                title="DevOps Solutions - Professional Services", 
                                company_name="DevOpsTech")

@app.route('/tools')
def tools():
    return render_template_string(html_template, 
                                title="DevOps Tools - DevOpsTech", 
                                company_name="DevOpsTech")

@app.route('/pipeline')
def pipeline():
    return render_template_string(html_template, 
                                title="CI/CD Pipeline - DevOpsTech", 
                                company_name="DevOpsTech")

@app.route('/metrics')
def metrics():
    return render_template_string(html_template, 
                                title="Performance Metrics - DevOpsTech", 
                                company_name="DevOpsTech")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
