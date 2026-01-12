#!/usr/bin/env python3
"""Generate HTML pages from extracted content matching original structure."""
import json
import os

def get_nav_html(current_page=""):
    """Generate navigation HTML."""
    nav_items = {
        "home": ("/", "Home", False),
        "about": ("/about/", "About", False),
        "leadership": ("/leadership/", "Executive Team", False),
        "mission": ("/mission-vision-values/", "Mission, Vision & Values", False),
        "business": ("/structured-finance-advisory/", "Business Development & Advisory Services", False),
        "venture": ("/business-development-investment/", "Venture Capital Funding", False),
        "property": ("/commercial-property-lending-investment/", "Property Investment", False),
        "contact": ("/contact/", "Contact", False),
    }
    
    home_class = 'current-menu-item' if current_page == 'home' else ''
    about_class = 'current-menu-item' if current_page == 'about' else ''
    leadership_class = 'current-menu-item' if current_page == 'leadership' else ''
    mission_class = 'current-menu-item' if current_page == 'mission' else ''
    business_class = 'current-menu-item' if current_page == 'business' else ''
    venture_class = 'current-menu-item' if current_page == 'venture' else ''
    property_class = 'current-menu-item' if current_page == 'property' else ''
    contact_class = 'current-menu-item' if current_page == 'contact' else ''
    
    return f'''<div id="nav">
<div class="menu-menu-1-container"><ul id="menu-menu-1" class="menu">
<li class="menu-item {home_class}"><a href="/">Home</a></li>
<li class="menu-item menu-item-has-children"><a href="#">Who We Are</a>
<ul class="sub-menu">
	<li class="menu-item {about_class}"><a href="/about/">About</a></li>
	<li class="menu-item {leadership_class}"><a href="/leadership/">Executive Team</a></li>
	<li class="menu-item {mission_class}"><a href="/mission-vision-values/">Mission, Vision & Values</a></li>
</ul>
</li>
<li class="menu-item menu-item-has-children"><a href="#">What We Do</a>
<ul class="sub-menu">
	<li class="menu-item {business_class}"><a href="/structured-finance-advisory/">Business Development & Advisory Services</a></li>
	<li class="menu-item {venture_class}"><a href="/business-development-investment/">Venture Capital Funding</a></li>
	<li class="menu-item {property_class}"><a href="/commercial-property-lending-investment/">Property Investment</a></li>
</ul>
</li>
<li class="menu-item {contact_class}"><a href="/contact/">Contact</a></li>
</ul></div></div>'''

def get_header_html():
    """Generate header HTML."""
    return '''<header id="masthead" class="site-header" role="banner">
		<div class="container">
			<div class="site-branding">
				<h1 class="site-title">
					<a href="/" title="Orchard Strategic Advisors" rel="home">
						<img src="/images/logo.png" alt="Orchard Strategic Advisors"/>
					</a>
				</h1>
			</div>
		
			<nav id="site-navigation" class="main-navigation" role="navigation">
				<h1 class="menu-toggle"><i class="icon-reorder">☰</i></h1>
				<div class="screen-reader-text skip-link"><a href="#content" title="Skip to content">Skip to content</a></div>

				<div class="menu-menu-1-container">
					<ul id="menu-menu-2" class="menu">
						<li class="menu-item"><a href="/">Home</a></li>
						<li class="menu-item menu-item-has-children"><a href="#">Who We Are</a>
							<ul class="sub-menu">
								<li class="menu-item"><a href="/about/">About</a></li>
								<li class="menu-item"><a href="/leadership/">Executive Team</a></li>
								<li class="menu-item"><a href="/mission-vision-values/">Mission, Vision & Values</a></li>
							</ul>
						</li>
						<li class="menu-item menu-item-has-children"><a href="#">What We Do</a>
							<ul class="sub-menu">
								<li class="menu-item"><a href="/structured-finance-advisory/">Business Development & Advisory Services</a></li>
								<li class="menu-item"><a href="/business-development-investment/">Venture Capital Funding</a></li>
								<li class="menu-item"><a href="/commercial-property-lending-investment/">Property Investment</a></li>
							</ul>
						</li>
						<li class="menu-item"><a href="/contact/">Contact</a></li>
					</ul>
				</div>
			</nav><!-- #site-navigation -->
		</div><!-- .container -->
	</header><!-- #masthead -->'''

def get_footer_html():
    """Generate footer HTML."""
    return '''<footer id="colophon" class="site-footer" role="contentinfo">
		<div class="container">
			<div class="site-info">
				&copy; 2023 Orchard Strategic Advisors
			</div><!-- .site-info -->
		</div><!-- .container -->
	</footer><!-- #colophon -->'''

# Read extracted content
with open('archive_raw/extracted_content.json', 'r') as f:
    content = json.load(f)

# Generate pages
pages = {
    'leadership': {
        'title': 'Executive Team | Orchard Strategic Advisors',
        'body_class': 'page leadership',
        'current': 'leadership',
        'content': content['executive-team']
    },
    'mission-vision-values': {
        'title': 'Mission, Vision & Values | Orchard Strategic Advisors',
        'body_class': 'page',
        'current': 'mission',
        'content': content['mission-vision-values']
    },
    'structured-finance-advisory': {
        'title': 'Business Development & Advisory Services | Orchard Strategic Advisors',
        'body_class': 'page',
        'current': 'business',
        'content': content['business-development']
    },
    'business-development-investment': {
        'title': 'Venture Capital Funding | Orchard Strategic Advisors',
        'body_class': 'page',
        'current': 'venture',
        'content': content['venture-capital']
    },
    'commercial-property-lending-investment': {
        'title': 'Property Investment | Orchard Strategic Advisors',
        'body_class': 'page',
        'current': 'property',
        'content': content['property-investment']
    }
}

for page_path, page_data in pages.items():
    os.makedirs(f'public/{page_path}', exist_ok=True)
    
    html = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{page_data['title']}</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body class="{page_data['body_class']}">

<div id="wrapper">

{get_nav_html(page_data['current'])}

<div id="page" class="hfeed site">
	{get_header_html()}

	<div id="content" class="site-content">
		<div class="container">

	<div id="primary" class="content-area">
		<main id="main" class="site-main" role="main">
			<article class="page type-page status-publish hentry">
				<header class="entry-header">
					<h1 class="entry-title">{page_data['content']['headings'][0]['text'] if page_data['content']['headings'] else ''}</h1>
				</header><!-- .entry-header -->

				<div class="entry-content">
'''
    
    # Add body text
    for para in page_data['content']['body_text']:
        html += f'\t\t\t\t\t<p>{para}</p>\n'
    
    html += '''				</div><!-- .entry-content -->
			</article><!-- #post-## -->
		</main><!-- #main -->
	</div><!-- #primary -->

	<div id="secondary" class="widget-area" role="complementary">
	</div><!-- #secondary -->

		</div><!-- .container -->
	</div><!-- #content -->

	{get_footer_html()}
</div><!-- #page -->
</div><!-- #wrapper -->

<script type="text/javascript" src="/js/jquery-1.10.2.min.js"></script>
<script type="text/javascript" src="/js/custom.js"></script>
</body>
</html>'''
    
    with open(f'public/{page_path}/index.html', 'w') as f:
        f.write(html)
    
    print(f"Generated {page_path}/index.html")

print("Done!")

