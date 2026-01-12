# Orchard Strategic Advisors Website

A static website rebuilt from Wayback Machine archives, optimized for Cloudflare Pages deployment.

## Project Structure

```
orchard-sa-website/
├── archive_raw/          # Archived HTML files and extracted content
├── public/               # Static site files (deploy this to Cloudflare Pages)
│   ├── index.html
│   ├── about/
│   ├── leadership/
│   ├── mission-vision-values/
│   ├── structured-finance-advisory/
│   ├── business-development-investment/
│   ├── commercial-property-lending-investment/
│   ├── contact/
│   ├── css/
│   ├── js/
│   └── images/
└── README.md
```

## Deployment to Cloudflare Pages

### Option 1: Direct Upload

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Navigate to **Pages** → **Create a project**
3. Select **Upload assets**
4. Upload the entire `public/` directory
5. Your site will be live at `your-project.pages.dev`

### Option 2: Git Integration

1. Push this repository to GitHub/GitLab
2. In Cloudflare Pages, connect your repository
3. Set build settings:
   - **Build command**: (leave empty - static site)
   - **Build output directory**: `public`
   - **Root directory**: (leave as root)
4. Deploy!

## Local Development

To preview the site locally:

```bash
# Using Python's built-in server
cd public
python3 -m http.server 8000

# Or using Node.js http-server
npx http-server public -p 8000
```

Then visit `http://localhost:8000`

## Contact Form

The contact form is currently set up to use Web3Forms. To enable it:

1. Sign up at [Web3Forms](https://web3forms.com/)
2. Get your access key
3. Update `public/contact/index.html` and replace `YOUR_WEB3FORMS_KEY` with your actual key

Alternatively, you can:
- Use Cloudflare Forms (requires Cloudflare Pages)
- Use a different form service
- Replace with a simple mailto link

## Features

- ✅ Responsive design (mobile-friendly)
- ✅ Hero image slider with auto-advance
- ✅ Dropdown navigation menus
- ✅ All pages from original site
- ✅ Clean, modern CSS
- ✅ Optimized for Cloudflare Pages

## Notes

- Images are downloaded from Wayback Machine archives
- All content extracted from archived pages dated September 2023
- Site structure matches original navigation
- Footer copyright shows 2023 (update as needed)

## License

Content belongs to Orchard Strategic Advisors.

