<div class="nav">
    <a href="/">Home</a></li>
    % if defined(username):
    |<a href="/{{username}}/">{{username}}</a>
    |<a href="/{{username}}/tweets/">Tweets</a>
    |<a href="/{{username}}/followers/">Followers</a>
    |<a href="/{{username}}/following/">Following</a>
    % end
</div>
