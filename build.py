"""Build the dependency-free GitHub Pages website: python3 build.py."""
from pathlib import Path
from html import escape as e
import json
import re

ROOT = Path(__file__).resolve().parent
TAG_GROUPS = json.loads((ROOT/'content/tags.json').read_text())
ALLOWED_TAGS = {tag for group in TAG_GROUPS.values() for tag in group}
BASE = 'https://petercalifano.github.io'
GH = 'https://github.com/PeterCalifano'
RESEARCH_MEDIA = 'https://github.com/PeterCalifano/petercalifano.github.io/releases/download/research-showcase-2026-10-10'
LINKEDIN = 'https://www.linkedin.com/in/pietro-califano-a46b7b199/'
SCHOLAR = 'https://scholar.google.com/citations?user=Yvol8yQAAAAJ&hl=en'
NAV = [('index.html','Home'),('research.html','Research'),('publications.html','Publications'),('projects.html','Projects'),('about.html','Background'),('beyond.html','Beyond work'),('index.html#contacts','Contacts')]

# EDITING TEXT: content/home.md, research.md, projects.md, about.md, beyond.md.
# Keep the ## section names; edit their paragraphs and bullets freely.
# Layout, navigation labels, dates, tags and links are defined below.
def load_copy(name):
    path = ROOT / "content" / f"{name}.md"
    sections = {}
    heading = None
    source = path.read_text(encoding="utf-8")
    source = re.sub(r"<!--.*?-->", "", source, flags=re.DOTALL)
    if "<!--" in source:
        raise ValueError(f"{path}: unclosed <!-- editing comment")
    for line in source.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            if heading in sections:
                raise ValueError(f"{path}: duplicate section {heading!r}")
            sections[heading] = []
        elif line.startswith("# ") and heading is None:
            continue
        elif heading is not None:
            sections[heading].append(line)
        elif line.strip():
            raise ValueError(f"{path}: text must follow a ## section heading")
    return {key: "\n".join(lines).strip() for key, lines in sections.items()}


COPY = {name: load_copy(name) for name in ("home", "research", "projects", "about", "beyond")}


def copy_text(page_name, section):
    """Plain text for fields that the existing renderer already escapes."""
    try:
        value = COPY[page_name][section]
    except KeyError as exc:
        raise ValueError(f"content/{page_name}.md: missing section {section!r}") from exc
    return " ".join(value.split())


def inline_text(value):
    """Escape prose; support *italic* text for book and film titles."""
    return re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", e(value, quote=False))


def copy_inline(page_name, section):
    return inline_text(copy_text(page_name, section))


def copy_html(page_name, section):
    """Render blank-line-separated paragraphs or a list with one '- ' per item."""
    copy_text(page_name, section)  # Report missing sections with the source path.
    value = COPY[page_name][section]
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    if lines and lines[0].startswith("- "):
        items = []
        for line in lines:
            if line.startswith("- "):
                items.append(line[2:])
            else:
                items[-1] += " " + line
        return '<ul class="research-points">' + ''.join(
            '<li>' + inline_text(item) + '</li>' for item in items
        ) + '</ul>'
    return ''.join('<p>' + inline_text(' '.join(part.split())) + '</p>'
                   for part in re.split(r"\n\s*\n", value) if part.strip())


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

home=('<section class="hero"><div><p class="eyebrow">AEROSPACE ENGINEERING / AUTONOMOUS NAVIGATION</p><h1>Pietro Califano<span style="color:var(--accent)">.</span></h1>' + ('<p class="role">' + copy_inline("home", 'Role') + '</p>') + ('<p class="lead">' + copy_inline("home", 'Lead') + '</p>') + '<div class="links">')+a('research.html','Research','button primary')+a('about.html','Background &amp; skills')+('</div></div><figure class="portrait"><img src="assets/portrait.png" width="250" height="250" alt="Portrait of Pietro Califano"></figure></section>\n<section class="home-about" aria-labelledby="about-heading"><h2 id="about-heading">About</h2><div>' + (copy_html("home", "About")) + '</div></section>\n<section class="home-experience" aria-labelledby="experience-heading"><div class="section-head"><h2 id="experience-heading">Experience</h2>')+a('about.html#experience','Background &amp; details')+('</div><ol class="career-timeline">\n<li><span class="career-date">May–Nov 2026</span><div><h3><a href="about.html#dfki">Guest researcher</a></h3><p>DFKI Robotics Innovation Center</p></div></li>\n<li><span class="career-date">Nov 2025–Apr 2026</span><div><h3><a href="about.html#tyvak">GNC engineer · internship</a></h3><p>Tyvak International</p></div></li>\n<li><span class="career-date">Dec 2023–present</span><div><h3><a href="about.html#dart">PhD researcher</a></h3><p>DART Lab · Politecnico di Milano</p></div></li>\n<li><span class="career-date">Apr–Sep 2023</span><div><h3><a href="about.html#esa">GNC intern · Hera mission</a></h3><p>European Space Agency · ESTEC</p></div></li>\n<li><span class="career-date">Dec 2021–Dec 2023</span><div><h3><a href="about.html#polispace">AOCS team member, then team leader</a></h3><p>PoliSpace · 6S CubeSat</p></div></li>\n</ol></section>\n<section class="home-highlight" aria-labelledby="research-highlight-heading"><div class="section-head"><h2 id="research-highlight-heading">Research highlight</h2></div>' + '<p class="highlight-description">' + copy_inline("home", 'Research highlight') + '</p>')+'''<a class="highlight-preview" href="research.html#navigation"><img src="'''+RESEARCH_MEDIA+'''/bennu_overview_poster.png" width="1600" height="1600" loading="lazy" decoding="async" alt="Explore the Bennu research showcase: spacecraft trajectory, camera view and SLAM map"></a><div class="links highlight-links">'''+a('research.html#navigation','Explore the research →')+'''</div></section>
<section id="contacts" class="contact"><h2>Contacts</h2><div><div class="links">'''+a('mailto:pietro.califano@polimi.it','pietro.califano@polimi.it')+a('mailto:petercalifano.gs@gmail.com','petercalifano.gs@gmail.com')+a(LINKEDIN,'LinkedIn')+a('assets/pietro-califano-qr.png','Website QR code')+'''</div></div></section>'''
page('index.html','Autonomous navigation, SLAM & research software','Pietro Califano, PhD candidate at DART Lab, Politecnico di Milano. Visual navigation, SLAM, spacecraft GNC, and research software.',home)

def research_video(name, label, ident):
    return (f'<div class="research-showcase" id="{ident}"><figure>'
            f'<video controls muted playsinline preload="metadata" poster="{RESEARCH_MEDIA}/{name}_poster.png" aria-label="{e(label,quote=True)}">'
            f'<source src="{RESEARCH_MEDIA}/{name}.mp4" type="video/mp4">'
            f'{a(RESEARCH_MEDIA+"/"+name+".mp4", "Download the video")}</video>'
            '</figure></div>')

research=head('01 / RESEARCH','Research interests',copy_inline('research', "Introduction"))
research+='<section id="navigation">'+row('Navigation &amp; mapping','SLAM for small-body exploration',copy_html("research", 'Navigation & mapping'),'PRIMARY RESEARCH',('Visual SLAM','Factor graphs','Recursive filtering','Orbital dynamics'))
research+=research_video('bennu_overview','Bennu trajectory above synchronized camera and SLAM backend views','slam-showcase')
research+=research_video('apophis_overview','Apophis filter-only trajectory and synchronized camera view','apophis-showcase')+'</section>'
research+=row('Perception','Visual measurements for navigation',copy_html("research", 'Perception'),'VISION &amp; LEARNING',('Computer vision','Photometric modelling','Machine learning','Event-based vision'))
research+=f'<div class="research-showcase research-tracking" id="feature-tracking-showcase"><figure><img src="{RESEARCH_MEDIA}/feature_tracking.gif" alt="Feature tracking across Itokawa camera images" loading="lazy"></figure></div>'
research+=row('Multi-sensor estimation','State estimation for robotic platforms',copy_html("research", 'Multi-sensor estimation'),'ROBOTICS',('Sensor fusion','Inertial sensing','Contact measurements','Visual navigation'))
research+='<section id="simulation">'+row('Simulation &amp; validation','Modelling and evaluation of navigation systems',copy_html("research", 'Simulation & validation'),'SIMULATION &amp; VALIDATION',('Dynamical modelling','Sensor simulation','Physically based rendering','Monte Carlo analysis'))+'</section>'
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

projects=head('03 / PROJECTS','Selected projects',copy_inline('projects', "Introduction"))
projects+='<section id="missions"><div class="section-head"><h2>Space missions</h2></div>'
projects+=row('RAMSES Farinella','Navigation-filter development',('<p class="meta">Project phases: A/B/C (completed); D/E1 (in progress).</p>' + (copy_html("projects", 'RAMSES Farinella')) + '<p>')+a('https://dart.polimi.it/projects/#_farinella','Project page')+'</p>','2025–PRESENT',('Navigation filtering','Centroiding','LiDAR'))
projects+=row('FUTURE','Navigation-filter and software integration',('<p class="meta">Project phase: C/D/E1.</p>' + (copy_html("projects", 'FUTURE')) + '<p>')+a('https://dart.polimi.it/projects/#_future','Project page')+'</p>','2024–PRESENT',('MATLAB','Simulink','C++','Jetson Orin NX'))
projects+=row('Hera Milani','GNC software &amp; navigation experiments',('<p class="meta">Operations preparation and CNES support.</p>' + (copy_html("projects", 'Hera Milani')) + '<p>')+a('https://dart.polimi.it/projects/#_milani','Project page')+'</p>','2024–PRESENT',('GNC','Image processing','Commissioning','Software validation'))
projects+='</section><section id="software" class="section"><div class="section-head"><h2>Software &amp; simulation</h2>'+a(GH+'?tab=repositories','All repositories')+'</div><div class="project-grid">'
cards=[
('STATE ESTIMATION','EstimationGears for SpaceNav',copy_text('projects', 'EstimationGears for SpaceNav'),['State estimation','MATLAB','C++'],GH+'/EstimationGears_for_SpaceNav'),
('COMPUTER VISION','slam-primitives',copy_text('projects', 'slam-primitives'),['Computer vision','SLAM'],GH+'/slam-primitives'),
('MACHINE LEARNING','pyTorchAutoForge',copy_text('projects', 'pyTorchAutoForge'),['Python','PyTorch','ONNX','TensorRT'],GH+'/pyTorchAutoForge'),
('MACHINE LEARNING','torchAutoForge-deploy',copy_text('projects', 'torchAutoForge-deploy'),['Machine learning inference','Model deployment'],GH+'/torchAutoForge-deploy'),
('COMPUTER VISION','v2e-extended',copy_text('projects', 'v2e-extended'),['Event-based vision','Python'],GH+'/v2e-extended'),
('SIMULATION','Spectral & radiometric renderer',copy_text('projects', 'Spectral & radiometric renderer'),['Radiometry','C++','CUDA','OptiX'],None),
('ROBOTICS','COSMICA–RAFFAELLO',copy_text('projects', 'COSMICA–RAFFAELLO'),['MATLAB','C++','ROS 2','MoveIt 2'],None)]
for kind,title,desc,tech,url in cards:
    link=a(url,'Repository') if url else '<span class="muted">Currently not published</span>'
    projects+=f'<article class="project"><span class="label">{e(kind)}</span><h3>{e(title)}</h3><p>{e(desc)}</p>{tags(tech)}<div class="links">{link}</div></article>'
projects+='</div><p class="muted">Some research software remains private while work is in development or under review. '+a('mailto:pietro.califano@polimi.it','Contact')+' for access enquiries related to research collaborations.</p></section>'
page('projects.html','Projects','Mission contributions, navigation software, machine-learning tools, rendering, and robotics facilities.',projects)

about=head('04 / BACKGROUND','Background &amp; experience',copy_inline('about', "Introduction"))
about+='<section id="experience" class="timeline"><div class="section-head"><h2>Research &amp; engineering</h2></div>'
experiences=[('May–Nov 2026','Guest researcher','DFKI Robotics Innovation Center · Underactuated Robotics Lab',copy_text('about', 'DFKI Robotics Innovation Center · Underactuated Robotics Lab')),('Nov 2025–Apr 2026','GNC engineer · internship','Tyvak International',copy_text('about', 'Tyvak International')),('Dec 2023–present','PhD researcher','DART Lab · Politecnico di Milano',copy_text('about', 'DART Lab · Politecnico di Milano')),('Apr–Sep 2023','GNC intern · Hera mission','European Space Agency · ESTEC',copy_text('about', 'European Space Agency · ESTEC')),('Dec 2021–Dec 2023','AOCS team member, then team leader','PoliSpace · 6S CubeSat',copy_text('about', 'PoliSpace · 6S CubeSat'))]
for anchor,(dates,title,org,desc) in zip(['dfki','tyvak','dart','esa','polispace'],experiences):
    about+=f'<article class="row" id="{anchor}"><p class="meta">{dates}</p><div><h3>{title}</h3><p class="org">{org}</p><p>{desc}</p></div></article>'
about+='</section><section class="section"><div class="section-head"><h2>Education</h2></div>'
about+=row('2023–2027','PhD in Aerospace Engineering',copy_html("about", 'PhD in Aerospace Engineering'),'DEFENCE EXPECTED FEB–MAR 2027')
about+=row('2021–2023','MSc in Space Engineering',copy_html("about", 'MSc in Space Engineering'))
about+=row('2018–2021','BSc in Aerospace Engineering',copy_html("about", 'BSc in Aerospace Engineering'))
about+='</section><section id="skills"><h2>Experience and tools</h2><div class="skill-grid">'
skills=[('Estimation & navigation',copy_text('about', 'Estimation & navigation')),('Programming',copy_text('about', 'Programming')),('Vision & machine learning',copy_text('about', 'Vision & machine learning')),('Rendering & simulation',copy_text('about', 'Rendering & simulation')),('Software & deployment',copy_text('about', 'Software & deployment')),('Hardware',copy_text('about', 'Hardware'))]
for title,desc in skills: about+=f'<div><h3>{e(title)}</h3><p>{e(desc)}</p></div>'
about+='</div></section><div class="callout"><div><h2>Research profiles &amp; contact</h2><p>Italian (native). English: C1 spoken and written, C2 reading.</p><div class="links" style="margin-top:20px">'+a(LINKEDIN,'LinkedIn')+a(SCHOLAR,'Google Scholar')+a('https://orcid.org/0009-0003-6157-3515','ORCID')+a('https://www.aero.polimi.it/en/staff/pietro.califano','Politecnico profile')+a('mailto:pietro.califano@polimi.it','Email')+'</div></div></div>'
page('about.html','Background & skills','Experience at DART Lab, DFKI, Tyvak International, ESA ESTEC, and PoliSpace; education and technical skills.',about)

beyond=head('05 / BEYOND WORK','Personal interests','Pietro, also known as PC or PeterC. '+a('https://steamcommunity.com/id/maxermast/','Maxermast on Steam')+'.')
beyond+='<blockquote class="quote quote-small"><p>'+copy_inline('beyond','Feynman quote')+'</p><cite>Richard P. Feynman</cite></blockquote>'
beyond+='<blockquote class="quote quote-small"><p>'+copy_inline('beyond','Personal motto')+'</p><cite>Personal motto</cite></blockquote><div class="hobby-grid">'
for num,title,desc in [('01','Running',copy_inline("beyond", 'Running')),('02','Anime & videogames',copy_inline("beyond", 'Anime & videogames')),('03','Learning <span lang="ja">日本語</span>',copy_inline("beyond", 'Learning 日本語')),('04','Reading',copy_inline("beyond", 'Reading')),('05','Hardware &amp; Linux',copy_inline("beyond", 'Hardware & Linux')),('06','Building things',copy_inline("beyond", 'Building things'))]:
    beyond+=f'<section class="hobby"><span class="number">{num}</span><h2>{title}</h2><p>{desc}</p></section>'
beyond+='</div><blockquote class="quote"><p>'+copy_inline('beyond','Coding motto')+'</p><cite>Coding motto</cite></blockquote><section id="contacts" class="contact"><h2>Contacts</h2><div><div class="links">'+a('mailto:petercalifano.gs@gmail.com','petercalifano.gs@gmail.com')+a('https://t.me/peter_califano','Telegram')+a(LINKEDIN,'LinkedIn')+'</div></div></section>'
page('beyond.html','Beyond work','Personal interests: reading, running, anime, videogames, Japanese, PC hardware, Linux, and software projects.',beyond)
page('404.html','Page not found','This page could not be found.',head('404 / PAGE NOT FOUND','Page not found','The requested page is unavailable.')+'<div class="section">'+a(BASE+'/','Back to home','button primary')+'</div>')
print('Built 7 HTML pages.')
