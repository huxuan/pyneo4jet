<div class="nav">
    |<a href="/">Home</a></li>|
    % if defined('username') and username:
    <a href="/{{username}}/">{{username}}</a>|
    <a href="/{{username}}/tweets/">Tweets</a>|
    <a href="/{{username}}/followers/">Followers</a>|
    <a href="/{{username}}/following/">Following</a>|
    <a href="/?action=signout">Sign Out</a>|
    % else:
    <a href="/?action=signup">Sign Up</a>|
    % end
</div>
