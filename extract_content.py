#!/usr/bin/env python3
"""
Extract content from archived HTML files and structure it for rebuilding.
"""
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

def clean_text(text):
    """Clean extracted text."""
    if not text:
        return ""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_images(soup, base_url):
    """Extract image URLs from the page."""
    images = []
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and 'homeImage' in src or 'wp-content' in src:
            # Extract original URL from wayback URL
            if 'web.archive.org' in src:
                # Pattern: https://web.archive.org/web/20230922223551im_/http://www.orchardsa.com/...
                match = re.search(r'/(im_|cs_|js_)/http://www\.orchardsa\.com/(.+)', src)
                if match:
                    original_path = match.group(2)
                    images.append({
                        'wayback_url': src,
                        'original_path': original_path,
                        'alt': img.get('alt', ''),
                        'class': img.get('class', [])
                    })
            else:
                images.append({
                    'wayback_url': src,
                    'original_path': src,
                    'alt': img.get('alt', ''),
                    'class': img.get('class', [])
                })
    return images

def extract_page_content(html_file):
    """Extract structured content from an HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Remove wayback machine toolbar and scripts
    for script in soup.find_all('script', src=re.compile('archive.org')):
        script.decompose()
    for div in soup.find_all('div', id=re.compile('wm-ipp')):
        div.decompose()
    
    page_data = {
        'title': '',
        'meta_description': '',
        'headings': [],
        'body_text': [],
        'images': [],
        'navigation': [],
        'footer': ''
    }
    
    # Extract title
    title_tag = soup.find('title')
    if title_tag:
        page_data['title'] = clean_text(title_tag.get_text())
    
    # Extract meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        page_data['meta_description'] = meta_desc.get('content', '')
    
    # Extract main content
    main = soup.find('main') or soup.find('div', id='primary') or soup.find('article')
    if main:
        # Extract headings
        for heading in main.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            text = clean_text(heading.get_text())
            if text:
                page_data['headings'].append({
                    'level': heading.name,
                    'text': text
                })
        
        # Extract paragraphs
        for p in main.find_all('p'):
            text = clean_text(p.get_text())
            if text and len(text) > 10:  # Filter out very short text
                page_data['body_text'].append(text)
    
    # Extract images
    page_data['images'] = extract_images(soup, '')
    
    # Extract navigation
    nav = soup.find('nav') or soup.find('div', class_=re.compile('navigation'))
    if nav:
        for link in nav.find_all('a'):
            href = link.get('href', '')
            text = clean_text(link.get_text())
            if text and href:
                page_data['navigation'].append({
                    'text': text,
                    'href': href
                })
    
    # Extract footer
    footer = soup.find('footer')
    if footer:
        page_data['footer'] = clean_text(footer.get_text())
    
    return page_data

def main():
    archive_dir = Path('archive_raw')
    output_file = Path('archive_raw/extracted_content.json')
    
    pages = {
        'home': 'index.html',
        'about': 'about.html',
        'executive-team': 'leadership.html',  # Leadership page
        'mission-vision-values': 'mission-vision-values.html',
        'business-development': 'business-development.html',
        'venture-capital': 'venture-capital.html',
        'property-investment': 'property-investment.html',
        'contact': 'contact.html'
    }
    
    all_content = {}
    
    for page_name, html_file in pages.items():
        html_path = archive_dir / html_file
        if html_path.exists():
            print(f"Extracting content from {html_file}...")
            all_content[page_name] = extract_page_content(html_path)
        else:
            print(f"Warning: {html_file} not found")
    
    # Save extracted content
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_content, f, indent=2, ensure_ascii=False)
    
    print(f"\nExtracted content saved to {output_file}")
    
    # Print summary
    print("\nContent Summary:")
    for page_name, content in all_content.items():
        print(f"  {page_name}:")
        print(f"    Title: {content['title']}")
        print(f"    Headings: {len(content['headings'])}")
        print(f"    Paragraphs: {len(content['body_text'])}")
        print(f"    Images: {len(content['images'])}")

if __name__ == '__main__':
    main()

