"""Build the dependency-free GitHub Pages website: python3 build.py."""
from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parent
BASE = 'https://petercalifano.github.io'
GH = 'https://github.com/PeterCalifano'
LINKEDIN = 'https://www.linkedin.com/in/pietro-califano-a46b7b199/'
SCHOLAR = 'https://scholar.google.com/citations?user=Yvol8yQAAAAJ&hl=en'
NAV = [('index.html','Home'),('research.html','Research'),('publications.html','Publications'),('projects.html','Projects'),('about.html','Background'),('beyond.html','Beyond work')]

def a(url,label,cls=''):
    return f'<a href="{e(url,quote=True)}"'+(f' class="{cls}"' if cls else '')+f'>{label}</a>'

def tags(items):
    return '<ul class="tags">'+''.join(f'<li>{e(x)}</li>' for x in items)+'</ul>'

def head(n,title,intro):
    return f'<header class="page-head"><p class="eyebrow">{n}</p><h1>{title}</h1><p class="intro">{intro}</p></header>'

def row(label,title,body,meta='',items=()):
    return f'<article class="row"><div><h2>{label}</h2><p class="meta">{meta}</p></div><div><h3>{title}</h3>{body}{tags(items) if items else ""}</div></article>'

def page(filename,title,description,body):
    nav=''.join(f'<a href="{path}"'+(' aria-current="page"' if path==filename else '')+f'>{label}</a>' for path,label in NAV)
    canonical=BASE+'/' + ('' if filename=='index.html' else filename)
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Pietro Califano</title><meta name="description" content="{e(description,quote=True)}">
<link rel="canonical" href="{canonical}"><meta property="og:title" content="{e(title,quote=True)} | Pietro Califano"><meta property="og:description" content="{e(description,quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="stylesheet" href="assets/site.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html"><span class="monogram" aria-hidden="true">PC</span><span>Pietro Califano</span></a><nav class="nav" aria-label="Main navigation">{nav}</nav></div></header>
<main id="main" class="wrap">{body}</main>
<footer class="footer"><div class="wrap"><span>© 2026 Pietro Califano</span><div class="footer-links">{a('https://dart.polimi.it/','DART · Politecnico di Milano')}{a(GH,'GitHub')}{a(LINKEDIN,'LinkedIn')}{a('mailto:pietro.califano@polimi.it','Email')}</div></div></footer></body></html>'''
    (ROOT/filename).write_text(html,encoding='utf-8')

home='''<section class="hero"><div><p class="eyebrow">AEROSPACE ENGINEERING / AUTONOMOUS NAVIGATION</p><h1>Pietro Califano<span style="color:var(--accent)">.</span></h1><p class="role">PhD researcher. Navigation engineer. Software builder.</p><p class="lead">I develop methods that help spacecraft and robots understand where they are, using vision, geometry, and state estimation.</p><div class="links">'''+a('research.html','Explore my research','button primary')+a('about.html','Background &amp; skills')+'''</div></div><figure class="portrait"><img src="assets/portrait.png" width="250" height="250" alt="Portrait of Pietro Califano"><figcaption>Pietro, also known as PC.<br>DART Lab, Politecnico di Milano</figcaption></figure></section>
<div class="affiliation"><span>PhD in Aerospace Engineering · Politecnico di Milano</span><span>Guest researcher · DFKI Robotics Innovation Center · 2026</span></div>
<section class="section"><div class="section-head"><h2>From the algorithm<br>to the spacecraft.</h2>'''+a('projects.html','Selected projects →')+'''</div><div class="grid">
<article class="feature"><a href="research.html#navigation"><span class="number">01 / UNDERSTAND</span><h3>Navigation &amp; SLAM</h3><p>Estimating motion and building maps for autonomous exploration of small bodies and poorly known environments.</p></a></article>
<article class="feature"><a href="projects.html#missions"><span class="number">02 / INTEGRATE</span><h3>Mission engineering</h3><p>Navigation filters, image-processing interfaces, and GNC software for Farinella, FUTURE, and Hera Milani.</p></a></article>
<article class="feature"><a href="projects.html#software"><span class="number">03 / BUILD</span><h3>Research software</h3><p>Reusable tools for estimation, computer vision, machine learning, and physically based simulation.</p></a></article></div></section>
<div class="callout"><div><h2>A byte beyond the research.</h2><p>Running, anime, videogames, and learning Japanese. Curiosity tends to find its way outside the lab, too.</p></div>'''+a('beyond.html','Beyond work','button')+'''</div><section class="contact"><h2>Let’s talk.</h2><div><p>Interested in visual navigation, autonomous exploration, or research software? Get in touch.</p><div class="links">'''+a('mailto:pietro.califano@polimi.it','pietro.califano@polimi.it')+a(LINKEDIN,'LinkedIn')+'''</div></div></section>'''
page('index.html','Autonomous navigation, SLAM & research software','Pietro Califano, PhD researcher at DART Lab, Politecnico di Milano. Visual navigation, SLAM, spacecraft GNC, and research software.',home)

research=head('01 / RESEARCH','Finding a way in<br>unfamiliar places.','My research focuses on visual navigation and multi-sensor state estimation for spacecraft and robots. Small-body exploration is the main application: limited prior maps, uncertain dynamics, and no GNSS.')
research+='<section id="navigation">'+row('Navigation &amp; mapping','SLAM for small-body proximity operations','<p>I designed a navigation architecture that combines monocular factor-graph SLAM with a higher-rate sliding-window extended Kalman filter. The two estimators bring mapping, motion estimation, and orbital dynamics into the navigation process.</p><p>I evaluate the system in Monte Carlo simulations around Itokawa, including weak-observability phases and impulsive manoeuvres, and assess trajectory error, uncertainty, mapping, and execution time.</p>','PRIMARY RESEARCH',('Factor graphs','GTSAM / iSAM2','Sliding-window EKF','Monocular vision'))+'</section>'
research+=row('Multi-sensor estimation','From spacecraft to robots','<p>At the DFKI Robotics Innovation Center, I am extending navigation and estimation methods to humanoid and rover platforms with free-floating or underactuated bases.</p><p>The work combines IMU, joint-state, contact, and vision measurements in a tightly coupled estimator, with evaluation on robotic platforms.</p>','ROBOTICS',('Sensor fusion','Contact measurements','Visual navigation'))
research+=row('Perception','Visual measurements that support navigation','<p>My work spans visual frontends and multi-view geometry, feature tracking, photometric modelling, and machine learning for navigation. Related interests include event-based vision and its use in visual odometry and localization.</p><p>I also co-developed NeuralCOB, a compact neural correction of centroid bias for the RAMSES Farinella mission, evaluated on synthetic Apophis imagery and OSIRIS-REx Bennu images.</p>','VISION &amp; LEARNING',('KLT / ORB','OpenCV','PyTorch','Event cameras'))
research+=row('Simulation &amp; validation','Knowing how an algorithm behaves','<p>I build spacecraft-navigation models and synthetic-image tools to test algorithms under controlled conditions. This includes gravity and solar-radiation-pressure models, finite burns, and regression tests for generated code.</p><p>My rendering work uses C++20, CUDA, and OptiX for spectral and radiometric image simulation, with BRDF models and interfaces for robotics and sensor simulation.</p>','RESEARCH INFRASTRUCTURE',('Monte Carlo analysis','CUDA / OptiX','Sensor simulation'))
research+='<div class="section"><div class="links">'+a('publications.html','Read the publications','button primary')+a('https://dart.polimi.it/','Explore DART Lab')+'</div></div>'
page('research.html','Research','Visual SLAM, factor-graph estimation, multi-sensor fusion, perception, and simulation for spacecraft and robots.',research)

publications=json.loads((ROOT/'content/publications.json').read_text())
pubbody=head('02 / PUBLICATIONS','Papers &amp;<br>work in progress.','Selected publications on autonomous navigation and small-body missions, followed by manuscripts with their current status.')
pubbody+='<div class="links" style="margin-bottom:45px">'+a(SCHOLAR,'Google Scholar')+a('https://orcid.org/0009-0003-6157-3515','ORCID')+a('https://dart.polimi.it/publications/','DART publications')+'</div>'
for group in ['Publications','Manuscripts']:
    pubbody+=f'<section class="publication-group"><h2>{group}</h2>'
    for p in publications:
        if p['group']!=group: continue
        authors=e(p['authors']).replace('P. Califano','<strong>P. Califano</strong>')
        link='<div class="links">'+a(p['url'],p.get('link_label','Publication record'))+'</div>' if p.get('url') else ''
        pubbody+=f'<article class="pub"><div class="meta">{p["year"]}</div><div><span class="label">{e(p["type"])}</span><h3>{e(p["title"])}</h3><p>{authors}</p><p>{e(p["venue"])}</p>{link}</div></article>'
    pubbody+='</section>'
page('publications.html','Publications','Selected conference papers, journal articles, and manuscripts by Pietro Califano and collaborators.',pubbody)

projects=head('03 / PROJECTS','Ideas, implemented.','My work connects navigation algorithms with mission software, simulation facilities, and reusable libraries. Here is a selection of the systems and tools I contribute to.')
projects+='<section id="missions"><div class="section-head"><h2>Spacecraft &amp; mission work</h2></div>'
projects+=row('RAMSES Farinella','Navigation-filter development','<p>Designed, implemented, and validated the navigation filter for the RAMSES RCS-1 (Farinella) CubeSat GNC/IP software from phase 0 through phase D. The work includes centroiding and LiDAR fusion.</p>','2025–PRESENT',('Navigation filtering','Centroiding','LiDAR'))
projects+=row('FUTURE','From prototype to onboard integration','<p>Designed, tested, and integrated navigation-filter and image-processing interfaces for the ASI FUTURE payload from phase B through phase D. Connected MATLAB/Simulink prototypes and generated C++ services for NVIDIA Jetson Orin NX deployment.</p><p>'+a('https://dart.polimi.it/projects/','FUTURE at DART')+'</p>','2024–PRESENT',('MATLAB / Simulink','C++ services','Jetson Orin NX'))
projects+=row('Hera Milani','GNC software &amp; navigation experiments','<p>Maintained, tested, and debugged the Milani CubeSat GNC/IP software, and supported navigation experiments and GNC commissioning during phases D and E.</p>','2024–PRESENT',('GNC / image processing','Commissioning','Software validation'))
projects+='</section><section id="software" class="section"><div class="section-head"><h2>Software &amp; simulation</h2>'+a(GH+'?tab=repositories','All GitHub repositories')+'</div><div class="project-grid">'
cards=[
('ESTIMATION','Small-body SLAM stack','A dual-estimator architecture for mapping and navigation, with dynamics and measurement factors, visual frontends, failure recovery, and trajectory evaluation.',['C++20','GTSAM','MATLAB'],'research.html#navigation','Research overview'),
('OPEN SOURCE','EstimationGears for SpaceNav','General-purpose MATLAB and C++ building blocks for spacecraft-navigation estimators.',['MATLAB','C++','State estimation'],GH+'/EstimationGears_for_SpaceNav','View repository'),
('OPEN SOURCE','slam-primitives','Reusable primitives supporting my work in visual navigation and SLAM.',['Computer vision','SLAM'],GH+'/slam-primitives','View repository'),
('OPEN SOURCE','pyTorchAutoForge','Tools for automating model development, with ONNX Runtime and TensorRT export and execution, parallel preprocessing, and deployment tooling.',['Python','PyTorch','ONNX / TensorRT'],GH+'/pyTorchAutoForge','View repository'),
('OPEN SOURCE','torchAutoForge-deploy','Deployment tooling that connects trained models with inference applications.',['Inference','Deployment'],GH+'/torchAutoForge-deploy','View repository'),
('OPEN SOURCE / FORK','v2e-extended','An extended implementation of v2e for event-stream simulation, including IEBCS and V2CE features and optimizations.',['Python','Event cameras'],GH+'/v2e-extended','View repository'),
('RESEARCH SOFTWARE','Spectral & radiometric renderer','A CUDA/OptiX renderer for synthetic navigation imagery, with spectral and BRDF models, multi-asset scenes, and ROS 2/render-server interfaces.',['C++20','CUDA / OptiX','Radiometry'],'research.html','Research overview'),
('ROBOTIC FACILITY','COSMICA–RAFFAELLO','MATLAB and C++ command/telemetry software, Yaskawa-controller interfaces, and ROS 2/MoveIt 2 monitoring, visualization, and planning tools for the dual-robot rail configuration.',['MATLAB / C++','ROS 2','MoveIt 2'],'https://dart.polimi.it/facilities/','DART facilities')]
for kind,title,desc,tech,url,label in cards:
    projects+=f'<article class="project"><span class="label">{e(kind)}</span><h3>{e(title)}</h3><p>{e(desc)}</p>{tags(tech)}{a(url,label)}</article>'
projects+='</div><p class="muted">Some research software remains private while work is in development or under review. '+a('mailto:pietro.califano@polimi.it','Contact me')+' to discuss access for research collaborations.</p></section>'
page('projects.html','Projects','Mission contributions, navigation software, machine-learning tools, rendering, and robotics facilities.',projects)

about=head('04 / BACKGROUND','Aerospace roots.<br>A wider field of view.','I am an Aerospace Engineering PhD researcher at DART Lab, Politecnico di Milano, and a guest researcher at the DFKI Robotics Innovation Center. My work combines algorithm design, validation, and software development for navigation systems.')
about+='<section class="timeline"><div class="section-head"><h2>Research &amp; engineering</h2></div>'
experiences=[('May–Nov 2026','Guest researcher','DFKI Robotics Innovation Center · Underactuated Robotics Lab','Extending visual navigation and state estimation to humanoid and rover platforms, with tightly coupled IMU, joint-state, contact, and vision measurements.'),('Dec 2023–present','PhD researcher','DART Lab · Politecnico di Milano','Developing visual navigation for small-body missions, from factor-graph SLAM and recursive filtering to simulation, validation, and deployment.'),('Apr–Sep 2023','GNC intern · Hera mission','European Space Agency · ESTEC','Reviewed and tested Hera GNC simulation models in MATLAB/Simulink and developed trajectory-safety failure-detection algorithms.'),('Dec 2021–Dec 2023','AOCS team member, then team leader','PoliSpace · 6S CubeSat','Contributed to mission phases A and B and ESA’s Fly Your Satellite! Design Booster programme. Led the AOCS team from June to December 2023, following work on requirements, models, and analysis tools.')]
for dates,title,org,desc in experiences:
    about+=f'<article class="row"><p class="meta">{dates}</p><div><h3>{title}</h3><p class="org">{org}</p><p>{desc}</p></div></article>'
about+='</section><section class="section"><div class="section-head"><h2>Education</h2></div>'
about+=row('2023–2027','PhD in Aerospace Engineering','<p>Politecnico di Milano. Research on vision-based navigation, SLAM, factor-graph smoothing, recursive filtering, and autonomy for small-body missions.</p>','EXPECTED APRIL 2027')
about+=row('2021–2023','MSc in Space Engineering','<p>Politecnico di Milano. Thesis: Hera mission trajectory-safety assessment through onboard failure detection.</p>')
about+=row('2018–2021','BSc in Aerospace Engineering','<p>University of Naples Federico II. Thesis: comparison of control laws for LiDAR pointing in close-proximity operations. Final grade: 110/110.</p>')
about+='</section><section id="skills"><h2>Methods &amp; tools</h2><div class="skill-grid">'
skills=[('Estimation & navigation','Visual SLAM, factor graphs, iSAM2/GTSAM, EKF/MEKF, bundle adjustment, multi-view geometry, spacecraft GNC.'),('Programming','C++20, Python, MATLAB/Simulink, Bash.'),('Vision & machine learning','OpenCV, KLT/ORB feature tracking, image segmentation, photometric modelling, PyTorch, ONNX Runtime, TensorRT.'),('Rendering & simulation','CUDA/OptiX ray tracing, spectral rendering, BRDF/Hapke models, synthetic datasets, reproducible Monte Carlo analysis.'),('Software & deployment','Linux, CMake, Git/GitHub Actions, CUDA, ROS 2, MoveIt 2, code generation, TCP services, profiling, and testing.'),('Hardware','NVIDIA Jetson Orin NX, Raspberry Pi, ARM Cortex-A9, Zynq-7000 ZedBoard, event and depth cameras.')]
for title,desc in skills: about+=f'<div><h3>{e(title)}</h3><p>{e(desc)}</p></div>'
about+='</div></section><div class="callout"><div><h2>Research profiles &amp; contact</h2><p>Italian (native). English: C1 spoken and written, C2 reading.</p><div class="links" style="margin-top:20px">'+a(LINKEDIN,'LinkedIn')+a(SCHOLAR,'Google Scholar')+a('https://orcid.org/0009-0003-6157-3515','ORCID')+a('https://www.aero.polimi.it/en/staff/pietro.califano','Politecnico profile')+a('mailto:pietro.califano@polimi.it','Email')+'</div></div></div>'
page('about.html','Background & skills','Experience at DART Lab, DFKI, ESA ESTEC, and PoliSpace; education and technical skills.',about)

beyond=head('05 / BEYOND WORK','A byte about me.','Curiosity is a common thread, whether I am working on a navigation problem, learning a language, or spending time away from the computer.')
beyond+='<blockquote class="quote"><p>“Wonder is anywhere, if you are curious enough to discover it.”</p><cite>My motto</cite></blockquote><div class="hobby-grid">'
for num,title,desc in [('01','Running','Running is part of my life outside research. A change of pace, and a reason to spend time outdoors.'),('02','Anime & videogames','Two interests that have a place alongside the technical work. I enjoy spending time with stories and games, as well as discussing them.'),('03','Learning Japanese','I am learning Japanese, getting to grips with the writing systems, pronunciation, and grammar.'),('04','Building things','The software habit does not always switch off after work. Computer graphics, ray tracing, and small tools often become projects of their own.')]:
    beyond+=f'<section class="hobby"><span class="number">{num}</span><h2>{title}</h2>'+('<span class="japanese" lang="ja">日本語</span><p class="meta">Nihongo · Japanese</p>' if num=='03' else '')+f'<p>{desc}</p></section>'
beyond+='</div><blockquote class="quote"><p>“Give me a task and I will code a SW library to automate it.”</p><cite>My coding motto</cite></blockquote><section class="contact"><h2>Say hello.</h2><div><div class="links">'+a('mailto:petercalifano.gs@gmail.com','petercalifano.gs@gmail.com')+a('https://t.me/peter_califano','Telegram')+a(LINKEDIN,'LinkedIn')+'</div></div></section>'
page('beyond.html','Beyond work','A byte about Pietro Califano: running, anime, videogames, learning Japanese, and building things.',beyond)
page('404.html','Page not found','This page could not be found.',head('404 / PAGE NOT FOUND','Off the mapped path.','The page may have moved. Head back to the homepage to find research, publications, and projects.')+'<div class="section">'+a(BASE+'/','Back to home','button primary')+'</div>')
print('Built 7 HTML pages.')
