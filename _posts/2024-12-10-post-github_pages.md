---
title: "Configuring My Personal Portfolio Blog with Jekyll and Minimal Mistakes"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - GitHub Pages
  - Jekyll
  - Minimal Mistakes
  - Personal Website
  - Setup Guide
---

Welcome to my personal blog! In this post, I'll walk you through the configuration of my GitHub Pages site, which I built using Jekyll and the [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) theme. Whether you're a fellow developer looking to set up your own portfolio or simply curious about customizing Jekyll themes, this guide should provide valuable insights.

## Why Jekyll and Minimal Mistakes?

Before diving into the configuration, here's a quick overview of why I chose Jekyll and the Minimal Mistakes theme:

- **Jekyll**: A static site generator that's seamlessly integrated with GitHub Pages, making deployment straightforward.
- **Minimal Mistakes**: A versatile and feature-rich Jekyll theme that offers a clean design, extensive customization options, and excellent documentation.

## Overview of the `_config.yml`

The `_config.yml` file is the heart of any Jekyll site. It controls everything from site metadata to theme settings and plugins. Below, I'll highlight the key sections and configurations I used for my portfolio.

### 1. Site Settings

```yaml
title: "Gordon YFG's Portfolio"
email: "gordon.yeung.toa@gmail.com"
description: "A showcase of my projects and a personal blog documenting my journey."
url: "https://gordonyfg.github.io" # Your GitHub Pages URL
baseurl: "" # Leave empty for user/organization site
repository: "gordonyfg/gordonyfg.github.io" # Your repository
twitter_username: username
github_username: username
minimal_mistakes_skin: "dark" 
# Options: "air", "aqua", "contrast", "dark", "dirt", "neon", "mint", "plum", "sunrise"
search: true
codeenable_copy_code_button: true
```

#### Key Configurations:

- **`title`**: Sets the title of your site, which appears in the browser tab and various sections of the theme.
- **`description`**: A brief description that enhances SEO and appears in meta tags.
- **`url` & `baseurl`**: Define the base URL of your site. For GitHub Pages user/organization sites, `baseurl` is typically left empty.
- **`repository`**: Specifies the GitHub repository associated with the site, enabling features like edit links.
- **`twitter_username` & `github_username`**: Integrate your social profiles seamlessly into the site.
- **`minimal_mistakes_skin`**: Chooses a color scheme for the theme. I've selected `"dark"` for a sleek, modern look.
- **`search`**: Enables the built-in search functionality.
- **`codeenable_copy_code_button`**: Adds a "Copy" button to code snippets, enhancing user experience.

### 2. Build Settings

```yaml
markdown: kramdown
remote_theme: mmistakes/minimal-mistakes
permalink: /:categories/:title/
paginate: 5 # amount of posts to show
paginate_path: /page:num/
timezone: # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
```

#### Key Configurations:

- **`markdown`**: Specifies the Markdown processor; `kramdown` is a popular choice compatible with Jekyll.
- **`remote_theme`**: Indicates the theme to use. By pointing to `mmistakes/minimal-mistakes`, I leverage the Minimal Mistakes theme without manually installing it.
- **`permalink`**: Defines the URL structure for posts. This setup organizes posts by category, enhancing SEO and navigation.
- **`paginate` & `paginate_path`**: Control pagination, displaying five posts per page and setting the URL structure for paginated pages.

### 3. Plugins

```yaml
plugins:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jemoji
  - jekyll-include-cache
```

These plugins extend the functionality of my site:

- **`jekyll-paginate`**: Adds pagination support.
- **`jekyll-sitemap`**: Generates a sitemap for better SEO.
- **`jekyll-gist`**: Allows embedding GitHub Gists.
- **`jekyll-feed`**: Creates an Atom feed.
- **`jemoji`**: Supports emoji rendering.
- **`jekyll-include-cache`**: Optimizes includes for faster build times.

### 4. Author Information

```yaml
author:
  name: "Gordon Yeung"
  avatar: "/assets/images/your-avatar.jpg" # Path to your avatar image
  bio: "R&D Engineer & Embedded System Engineer"
  location: "British Columbia, Canada"
  links:
    - label: "Email"
      url: "mailto:gordon.yeung.toa@gmail.com"
      icon: "fas fa-envelope"
    - label: "GitHub"
      url: "https://github.com/gordonyfg"
      icon: "fab fa-github"
    - label: "LinkedIn"
      url: "https://www.linkedin.com/in/gordon-yeung-349b66133/"
      icon: "fab fa-linkedin"
```

#### Key Configurations:

- **`name` & `avatar`**: Personalize the site with your name and profile picture.
- **`bio` & `location`**: Provide a brief introduction and your geographical location.
- **`links`**: Connect to your various social profiles and contact methods, enhancing networking opportunities.

### 5. Footer Configuration

```yaml
footer:
  links:
    - label: "Twitter"
      icon: "fab fa-fw fa-twitter-square"
      url: "https://twitter.com/"
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/"
    - label: "Instagram"
      icon: "fab fa-fw fa-instagram"
      url: "https://instagram.com/"
```

The footer provides quick access to your social media profiles. Ensure you update the `url` fields with your actual social media links to make them functional.

### 6. Defaults and Archives

```yaml
defaults:
  # _posts
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: true
      share: true
      related: true
  # _pages
  - scope:
      path: "_pages"
      type: pages
    values:
      layout: single
      author_profile: true

category_archive:
  type: liquid
  path: /categories/
tag_archive:
  type: liquid
  path: /tags/
```

#### Key Configurations:

- **`defaults`**: Sets default front matter for posts and pages, ensuring consistency across your content. Features like author profiles, read time estimates, comments, sharing buttons, and related posts enhance user engagement.
- **`category_archive` & `tag_archive`**: Organize your content by categories and tags, making it easier for visitors to navigate topics of interest.

### 7. Comments Configuration

```yaml
comments:
  provider: "utterances"
  utterances:
    theme: "github-light" # "github-dark"
    issue_term: "pathname"
    label: "comment" # Optional - must be existing label.
```

I've integrated [Utterances](https://utteranc.es/) for comments, which leverages GitHub issues for a lightweight commenting system. This choice aligns well with GitHub Pages and ensures that comments are managed within your GitHub repository. The `theme` can be toggled between light and dark to match your site's aesthetic.

## Additional Customizations

While the above configurations cover the essentials, I've also made several other tweaks to tailor the site to my preferences:

- **Avatar and Bio Image**: Updated the `avatar` path to display a personal photo, adding a human touch to the site.
- **Custom Links**: Replaced generic social links with my actual GitHub and LinkedIn profiles, facilitating networking.
- **Dark Theme**: Opted for the `"dark"` skin in Minimal Mistakes to give the portfolio a modern and professional look.

## Getting Started with Your Own Configuration

If you're inspired to set up your own portfolio using Jekyll and Minimal Mistakes, here's a quick guide:

1. **Fork the Starter Theme**: Begin by forking the [Minimal Mistakes GitHub Pages Starter](https://github.com/mmistakes/mm-github-pages-starter) repository.
2. **Customize `_config.yml`**: Update the `_config.yml` with your personal information, social links, and preferred settings as demonstrated above.
3. **Add Your Content**: Populate the `_posts` and `_pages` directories with your projects, blog posts, and other relevant content.
4. **Deploy via GitHub Pages**: Push your changes to GitHub, and your site will be automatically built and deployed.

## Conclusion

Configuring a personal blog with Jekyll and Minimal Mistakes offers a powerful way to showcase your projects and share your journey. By customizing the `_config.yml`, you can tailor the site to reflect your personal brand and preferences. I hope this guide provides a helpful starting point for your own blogging adventures. Happy coding!

---

Feel free to reach out via [GitHub](https://github.com/gordonyfg) or [LinkedIn](https://www.linkedin.com/in/gordon-yeung-349b66133/) if you have any questions or suggestions!