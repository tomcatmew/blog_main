AUTHOR = 'tomcat'
SITENAME = 'personal blog'
SITEURL = 'https://tomcatmew.github.io/blog_main'

PATH = "content"

TIMEZONE = 'Japan'

DEFAULT_LANG = 'English'

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

import yaml
from pathlib import Path

def get_comments(article_slug):
    comments_path = Path(f'content/data/comments/')
    comments = []

    if comments_path.exists():
        for comment_file in comments_path.glob(f'{article_slug}-*.md'):
            with comment_file.open('r') as f:
                comment = yaml.safe_load(f)
                comments.append(comment)

    return comments

JINJA_FILTERS = {
    'get_comments': get_comments,
}
