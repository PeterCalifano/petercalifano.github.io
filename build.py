"""Build the dependency-free GitHub Pages website: python3 build.py."""
from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parent
TAG_GROUPS = json.loads((ROOT/'content/tags.json').read_text())
ALLOWED_TAGS = {tag for group in TAG_GROUPS.values() for tag in group}
BASE = 'https://petercalifano.github.io'
GH = 'https://github.com/PeterCalifano'
RESEARCH_MEDIA = 'https://github.com/PeterCalifano/petercalifano.github.io/releases/download/research-showcase-2026-10-10'
LINKEDIN = 'https://www.linkedin.com/in/pietro-califano-a46b7b199/'
SCHOLAR = 'https://scholar.google.com/citations?user=Yvol8yQAAAAJ&hl=en'
NAV = [('index.html','Home'),('research.html','Research'),('publications.html','Publications'),('projects.html','Projects'),('about.html','Background'),('beyond.html','Beyond work'),('index.html#contacts','Contacts')]

def a(url,label,cls=''):
    return f'<a href="{e(url,quote=True)}"'+(f' class="{cls}"' if cls else '')+f'>{label}</a>'

def tags(items):
    unknown = set(items) - ALLOWED_TAGS
    if unknown:
        raise ValueError(f'Unknown tags: {sorted(unknown)}. Choose from content/tags.json.')
    if len(items) != len(set(items)):
        raise ValueError(f'Duplicate tags: {items}')
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
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="stylesheet" href="assets/site.css"><link rel="stylesheet" href="assets/home.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html"><span class="monogram" aria-hidden="true">PC</span><span>Pietro Califano</span></a><nav class="nav" aria-label="Main navigation">{nav}</nav></div></header>
<main id="main" class="wrap">{body}</main>
<footer class="footer"><div class="wrap"><span>© 2026 Pietro Califano</span><div class="footer-links">{a('https://dart.polimi.it/','DART · Politecnico di Milano')}{a(GH,'GitHub')}{a(LINKEDIN,'LinkedIn')}{a('index.html#contacts','Contacts')}</div></div></footer></body></html>'''
    (ROOT/filename).write_text(html,encoding='utf-8')

home='''<section class="hero"><div><p class="eyebrow">AEROSPACE ENGINEERING / AUTONOMOUS NAVIGATION</p><h1>Pietro Califano<span style="color:var(--accent)">.</span></h1><p class="role">PhD in Aerospace Engineering</p><p class="lead">Visual navigation, SLAM, and multi-sensor state estimation.</p><div class="links">'''+a('research.html','Research','button primary')+a('about.html','Background &amp; skills')+'''</div></div><figure class="portrait"><img src="assets/portrait.png" width="250" height="250" alt="Portrait of Pietro Califano"></figure></section>
<section class="home-about" aria-labelledby="about-heading"><h2 id="about-heading">About</h2><div><p>Pietro Califano is a PhD candidate at DART Lab, Politecnico di Milano, and a guest researcher at the DFKI Robotics Innovation Center. His research focuses on the development of autonomous navigation and computer vision algorithms and software for space applications, with particular emphasis on challenging scenarios involving uncooperative and poorly characterized targets, especially in small-body missions. Previously, he worked on guidance, navigation, and control for ESA's Hera mission during a six-month internship at ESTEC and contributed to the PoliSpace 6S CubeSat project during his MSc studies.</p></div></section>
<section class="home-experience" aria-labelledby="experience-heading"><div class="section-head"><h2 id="experience-heading">Experience</h2>'''+a('about.html#experience','Background &amp; details')+'''</div><ol class="career-timeline">
<li><span class="career-date">May–Nov 2026</span><div><h3><a href="about.html#dfki">Guest researcher</a></h3><p>DFKI Robotics Innovation Center</p></div></li>
<li><span class="career-date">Dec 2023–present</span><div><h3><a href="about.html#dart">PhD researcher</a></h3><p>DART Lab · Politecnico di Milano</p></div></li>
<li><span class="career-date">Apr–Sep 2023</span><div><h3><a href="about.html#esa">GNC intern · Hera mission</a></h3><p>European Space Agency · ESTEC</p></div></li>
<li><span class="career-date">Dec 2021–Dec 2023</span><div><h3><a href="about.html#polispace">AOCS team member, then team leader</a></h3><p>PoliSpace · 6S CubeSat</p></div></li>
</ol></section>
<section class="home-highlight" aria-labelledby="research-highlight-heading"><div class="section-head"><h2 id="research-highlight-heading">Research highlight</h2></div><div class="highlight-grid"><div><p>Closed-loop spacecraft navigation around small bodies, combining visual measurements, state estimation, guidance and mapping.</p><div class="links">'''+a('research.html#navigation','Explore the research')+'''</div></div><a class="highlight-preview" href="research.html#navigation"><img src="'''+RESEARCH_MEDIA+'''/bennu_overview_poster.png" width="1600" height="1600" loading="lazy" decoding="async" alt="Explore the Bennu research showcase: spacecraft trajectory, camera view and SLAM map"></a></div></section>
<section id="contacts" class="contact"><h2>Contacts</h2><div><div class="links">'''+a('mailto:pietro.califano@polimi.it','pietro.califano@polimi.it')+a('mailto:petercalifano.gs@gmail.com','petercalifano.gs@gmail.com')+a(LINKEDIN,'LinkedIn')+a('assets/pietro-califano-qr.png','Website QR code')+'''</div></div></section>'''
page('index.html','Autonomous navigation, SLAM & research software','Pietro Califano, PhD researcher at DART Lab, Politecnico di Milano. Visual navigation, SLAM, spacecraft GNC, and research software.',home)

def research_video(name, label, ident):
    return (f'<div class="research-showcase" id="{ident}"><figure>'
            f'<video controls muted playsinline preload="metadata" poster="{RESEARCH_MEDIA}/{name}_poster.png" aria-label="{e(label,quote=True)}">'
            f'<source src="{RESEARCH_MEDIA}/{name}.mp4" type="video/mp4">'
            f'{a(RESEARCH_MEDIA+"/"+name+".mp4", "Download the video")}</video>'
            '</figure></div>')

research=head('01 / RESEARCH','Research interests','Visual navigation, mapping, and multi-sensor state estimation for spacecraft and robots operating with limited prior knowledge of their surroundings.')
research+='<section id="navigation">'+row('Navigation &amp; mapping','SLAM for small-body exploration','<ul class="research-points"><li>Joint estimation of spacecraft motion and environmental geometry from visual observations.</li><li>Integration of factor-graph smoothing, recursive filtering, and orbital dynamics for proximity navigation.</li><li>Metric-scale observability and uncertainty under target rotation, variable illumination, and uncertain dynamics.</li><li>Computational efficiency and estimation consistency within onboard processing constraints.</li></ul>','PRIMARY RESEARCH',('Visual SLAM','Factor graphs','Recursive filtering','Orbital dynamics'))
research+=research_video('bennu_overview','Bennu trajectory above synchronized camera and SLAM backend views','slam-showcase')
research+=research_video('apophis_overview','Apophis filter-only trajectory and synchronized camera view','apophis-showcase')+'</section>'
research+=row('Perception','Visual measurements for navigation','<ul class="research-points"><li>Feature tracking and multi-view geometry for motion estimation and scene reconstruction.</li><li>Photometric modelling of visual measurements under variable illumination and viewing geometry.</li><li>Learning-based correction of image-derived navigation measurements, including target centroid estimates.</li><li>Event-based vision for odometry and localization.</li></ul>','VISION &amp; LEARNING',('Computer vision','Photometric modelling','Machine learning','Event-based vision'))
research+=f'<div class="research-showcase research-tracking" id="feature-tracking-showcase"><figure><img src="{RESEARCH_MEDIA}/feature_tracking.gif" alt="Feature tracking across Itokawa camera images" loading="lazy"></figure></div>'
research+=row('Multi-sensor estimation','State estimation for robotic platforms','<ul class="research-points"><li>Tightly coupled fusion of visual, inertial, joint-state, and contact measurements.</li><li>Motion estimation for humanoids with free-floating or underactuated bases.</li><li>Complementary geometric, kinematic, and contact constraints for localization.</li><li>Assessment of sensor contributions, estimation accuracy, and uncertainty.</li></ul>','ROBOTICS',('Sensor fusion','Inertial sensing','Contact measurements','Visual navigation'))
research+='<section id="simulation">'+row('Simulation &amp; validation','Modelling and evaluation of navigation systems','<ul class="research-points"><li>Spacecraft dynamics models with gravity, solar-radiation pressure, and manoeuvres.</li><li>Synthetic sensor measurements for navigation-system development and validation.</li><li>Spectral and radiometric rendering under variable illumination, surface properties, and viewing geometry.</li><li>Monte Carlo assessment of estimation errors, uncertainty, and computational cost.</li></ul>','SIMULATION &amp; VALIDATION',('Dynamical modelling','Sensor simulation','Physically based rendering','Monte Carlo analysis'))+'</section>'
research+='<div class="section"><div class="links">'+a('publications.html','Publications','button primary')+a('https://dart.polimi.it/','DART Lab')+'</div></div>'
page('research.html','Research','Visual SLAM, factor-graph estimation, multi-sensor fusion, perception, and simulation for spacecraft and robots.',research)

publications=json.loads((ROOT/'content/publications.json').read_text())
record_labels={'Journal': 'Publication record', 'Conference': 'Conference record', 'Dataset': 'Dataset record'}
pubbody=head('02 / PUBLICATIONS','Publications','Journal articles, conference contributions, and datasets.')
pubbody+='<div class="links" style="margin-bottom:45px">'+a(SCHOLAR,'Google Scholar')+a('https://re.public.polimi.it/cris/rp/rp241375','RE.PUBLIC@Polimi')+a('https://orcid.org/0009-0003-6157-3515','ORCID')+a('https://dart.polimi.it/publications/','DART publications')+'</div>'
for year in sorted({p['year'] for p in publications}, reverse=True):
    pubbody+=f'<section class="publication-group"><h2>{year}</h2>'
    for p in publications:
        if p['year']!=year: continue
        authors=e(p['authors']).replace('P. Califano','<strong>P. Califano</strong>')
        link='<div class="links">'+a(p['url'],record_labels[p['type']])+'</div>' if p.get('url') else ''
        pubbody+=f'<article class="pub"><div class="meta">{p["year"]}</div><div><span class="label">{e(p["type"])}</span><h3>{e(p["title"])}</h3><p>{authors}</p><p>{e(p["venue"])}</p>{link}</div></article>'
    pubbody+='</section>'
page('publications.html','Publications','Journal articles, conference contributions, and datasets by Pietro Califano and collaborators.',pubbody)

projects=head('03 / PROJECTS','Selected projects','Contributions to mission software, navigation algorithms, simulation facilities, and research libraries.')
projects+='<section id="missions"><div class="section-head"><h2>Space missions</h2></div>'
projects+=row('RAMSES Farinella','Navigation-filter development','<p class="meta">Project phases: A/B/C (completed); D/E1 (in progress).</p><p>Designed and validated the navigation filter for the RAMSES RCS-1 (Farinella) CubeSat, combining centroiding and LiDAR measurements.</p><p>'+a('https://dart.polimi.it/projects/#_farinella','Project page')+'</p>','2025–PRESENT',('Navigation filtering','Centroiding','LiDAR'))
projects+=row('FUTURE','Navigation-filter and software integration','<p class="meta">Project phase: C/D/E1.</p><p>Designed and integrated the navigation filter and image-processing interfaces for the ASI FUTURE payload, supporting autonomous navigation from visual observations.</p><p>'+a('https://dart.polimi.it/projects/#_future','Project page')+'</p>','2024–PRESENT',('MATLAB','Simulink','C++','Jetson Orin NX'))
projects+=row('Hera Milani','GNC software &amp; navigation experiments','<p class="meta">Operations preparation and CNES support.</p><p>Contributed to GNC and image-processing software validation for the Hera Milani CubeSat, including navigation experiments and GNC commissioning.</p><p>'+a('https://dart.polimi.it/projects/#_milani','Project page')+'</p>','2024–PRESENT',('GNC','Image processing','Commissioning','Software validation'))
projects+='</section><section id="software" class="section"><div class="section-head"><h2>Software &amp; simulation</h2>'+a(GH+'?tab=repositories','All repositories')+'</div><div class="project-grid">'
cards=[
('STATE ESTIMATION','EstimationGears for SpaceNav','A library of state-estimation methods for spacecraft navigation.',['State estimation','MATLAB','C++'],GH+'/EstimationGears_for_SpaceNav'),
('COMPUTER VISION','slam-primitives','Shared types and primitives for SLAM and computer vision.',['Computer vision','SLAM'],GH+'/slam-primitives'),
('MACHINE LEARNING','pyTorchAutoForge','A framework for training and evaluating machine-learning models.',['Python','PyTorch','ONNX','TensorRT'],GH+'/pyTorchAutoForge'),
('MACHINE LEARNING','torchAutoForge-deploy','Tools for deploying trained machine-learning models in inference applications.',['Machine learning inference','Model deployment'],GH+'/torchAutoForge-deploy'),
('COMPUTER VISION','v2e-extended','An extension of v2e for simulating event-camera measurements from conventional video.',['Event-based vision','Python'],GH+'/v2e-extended'),
('SIMULATION','Spectral & radiometric renderer','Spectral and radiometric rendering for synthetic navigation imagery and sensor simulation.',['Radiometry','C++','CUDA','OptiX'],None),
('ROBOTICS','COSMICA–RAFFAELLO','Robot-control and planning software for hardware-in-the-loop validation of spacecraft navigation and image processing.',['MATLAB','C++','ROS 2','MoveIt 2'],None)]
for kind,title,desc,tech,url in cards:
    link=a(url,'Repository') if url else '<span class="muted">Currently not published</span>'
    projects+=f'<article class="project"><span class="label">{e(kind)}</span><h3>{e(title)}</h3><p>{e(desc)}</p>{tags(tech)}<div class="links">{link}</div></article>'
projects+='</div><p class="muted">Some research software remains private while work is in development or under review. '+a('mailto:pietro.califano@polimi.it','Contact')+' for access enquiries related to research collaborations.</p></section>'
page('projects.html','Projects','Mission contributions, navigation software, machine-learning tools, rendering, and robotics facilities.',projects)

about=head('04 / BACKGROUND','Background &amp; experience','Research appointments, education, and technical skills.')
about+='<section id="experience" class="timeline"><div class="section-head"><h2>Research &amp; engineering</h2></div>'
experiences=[('May–Nov 2026','Guest researcher','DFKI Robotics Innovation Center · Underactuated Robotics Lab','Extending visual navigation and state estimation to humanoid platforms, with tightly coupled IMU, joint-state, contact, and vision measurements.'),('Dec 2023–present','PhD researcher','DART Lab · Politecnico di Milano','Developing factor-graph SLAM and recursive filtering methods for small-body missions. Implementing and validating navigation software.'),('Apr–Sep 2023','GNC intern · Hera mission','European Space Agency · ESTEC','Reviewed and tested Hera GNC simulation models in MATLAB/Simulink and developed trajectory-safety failure-detection algorithms.'),('Dec 2021–Dec 2023','AOCS team member, then team leader','PoliSpace · 6S CubeSat','Contributed to mission phases A and B and ESA’s Fly Your Satellite! Design Booster programme. Led the AOCS team from June to December 2023, following work on requirements, models, and analysis tools.')]
for anchor,(dates,title,org,desc) in zip(['dfki','dart','esa','polispace'],experiences):
    about+=f'<article class="row" id="{anchor}"><p class="meta">{dates}</p><div><h3>{title}</h3><p class="org">{org}</p><p>{desc}</p></div></article>'
about+='</section><section class="section"><div class="section-head"><h2>Education</h2></div>'
about+=row('2023–2027','PhD in Aerospace Engineering','<p>Politecnico di Milano, Department of Aerospace Science and Technology. Doctoral programme started in December 2023.</p>','EXPECTED MARCH 2027')
about+=row('2021–2023','MSc in Space Engineering','<p>Politecnico di Milano. Thesis: Hera mission trajectory-safety assessment through onboard failure detection. Final grade: 110/110.</p>')
about+=row('2018–2021','BSc in Aerospace Engineering','<p>University of Naples Federico II. Thesis: comparison of control laws for LiDAR pointing in close-proximity operations. Final grade: 110/110.</p>')
about+='</section><section id="skills"><h2>Methods &amp; tools</h2><div class="skill-grid">'
skills=[('Estimation & navigation','Visual SLAM, factor graphs, iSAM2/GTSAM, EKF/MEKF, bundle adjustment, multi-view geometry, spacecraft GNC.'),('Programming','C++20, Python, MATLAB/Simulink, Bash.'),('Vision & machine learning','OpenCV, KLT/ORB feature tracking, image segmentation, photometric modelling, PyTorch, ONNX Runtime, TensorRT.'),('Rendering & simulation','CUDA/OptiX ray tracing, spectral rendering, BRDF/Hapke models, synthetic datasets, reproducible Monte Carlo analysis.'),('Software & deployment','Linux, CMake, Git/GitHub Actions, CUDA, ROS 2, MoveIt 2, code generation, TCP services, profiling, and testing.'),('Hardware','NVIDIA Jetson Orin NX, Raspberry Pi, ARM Cortex-A9, Zynq-7000 ZedBoard, event and depth cameras.')]
for title,desc in skills: about+=f'<div><h3>{e(title)}</h3><p>{e(desc)}</p></div>'
about+='</div></section><div class="callout"><div><h2>Research profiles &amp; contact</h2><p>Italian (native). English: C1 spoken and written, C2 reading.</p><div class="links" style="margin-top:20px">'+a(LINKEDIN,'LinkedIn')+a(SCHOLAR,'Google Scholar')+a('https://orcid.org/0009-0003-6157-3515','ORCID')+a('https://www.aero.polimi.it/en/staff/pietro.califano','Politecnico profile')+a('mailto:pietro.califano@polimi.it','Email')+'</div></div></div>'
page('about.html','Background & skills','Experience at DART Lab, DFKI, ESA ESTEC, and PoliSpace; education and technical skills.',about)

beyond=head('05 / BEYOND WORK','Personal interests','Pietro, also known as PC or PeterC. '+a('https://steamcommunity.com/id/maxermast/','Maxermast on Steam')+'.')
beyond+='<blockquote class="quote quote-small"><p>“Study hard what interests you the most in the most undisciplined, irreverent and original manner possible.”</p><cite>Richard P. Feynman</cite></blockquote>'
beyond+='<blockquote class="quote quote-small"><p>“Wonder is anywhere, if you are curious enough to discover it.”</p><cite>Personal motto</cite></blockquote><div class="hobby-grid">'
for num,title,desc in [('01','Running','Regular running and time outdoors.'),('02','Anime & videogames','Watching anime, playing videogames, and discussing both. Favourite anime: special — <em>Neon Genesis Evangelion</em>; best overall — <em>Sōsō no Frieren</em>.'),('03','Learning <span lang="ja">日本語</span>','Learning to read, write, and speak Japanese.'),('04','Reading','Science, philosophy, and a bit of fiction. Evolutionary biology is a favourite topic. Some favourite books: <em>Slaughterhouse-Five</em> by Kurt Vonnegut, <em>Chance and Necessity</em> by Jacques Monod, <em>Solaris</em> by Stanisław Lem, <em>Do Androids Dream of Electric Sheep?</em> by Philip K. Dick, <em>Blindness</em> by José Saramago, <em>The Art of Statistics</em> by David Spiegelhalter, <em>Thinking, Fast and Slow</em> by Daniel Kahneman, and <em>Guns, Germs, and Steel</em> by Jared Diamond.'),('05','Hardware &amp; Linux','PC hardware, Linux, and other computing interests.'),('06','Building things','Computer graphics, ray tracing, and small software tools.')]:
    beyond+=f'<section class="hobby"><span class="number">{num}</span><h2>{title}</h2>'+('<p class="meta">Nihongo · Japanese</p>' if num=='03' else '')+f'<p>{desc}</p></section>'
beyond+='</div><blockquote class="quote"><p>“Give me a task and I will code a SW library to automate it.”</p><cite>Coding motto</cite></blockquote><section id="contacts" class="contact"><h2>Contacts</h2><div><div class="links">'+a('mailto:petercalifano.gs@gmail.com','petercalifano.gs@gmail.com')+a('https://t.me/peter_califano','Telegram')+a(LINKEDIN,'LinkedIn')+'</div></div></section>'
page('beyond.html','Beyond work','Personal interests: reading, running, anime, videogames, Japanese, PC hardware, Linux, and software projects.',beyond)
page('404.html','Page not found','This page could not be found.',head('404 / PAGE NOT FOUND','Page not found','The requested page is unavailable.')+'<div class="section">'+a(BASE+'/','Back to home','button primary')+'</div>')
print('Built 7 HTML pages.')
