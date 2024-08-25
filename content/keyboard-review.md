Title: My First Review
Date: 2010-12-03 10:20
Category: Review

Following is a review of my favorite mechanical keyboard.

## Comments

{% for comment in article.slug | get_comments %}
<div class="comment">
    <p><strong>{{ comment.author }}</strong> said on {{ comment.date }}:</p>
    <p>{{ comment.body }}</p>
</div>
{% endfor %}

<form action="https://github.com/tomcatmew/blog_main/issues" method="POST">
    <input type="hidden" name="title" value="Comment on {{ title }}">
    <input type="hidden" name="labels" value="comment">
    
    <p>
        <label for="name">Name:</label>
        <input type="text" id="name" name="body[name]" required>
    </p>
    <p>
        <label for="email">Email:</label>
        <input type="email" id="email" name="body[email]" required>
    </p>
    <p>
        <label for="comment">Comment:</label>
        <textarea id="comment" name="body[comment]" required></textarea>
    </p>
    <p>
        <button type="submit">Submit Comment</button>
    </p>
</form>