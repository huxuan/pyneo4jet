<div class="nav">
    <a href="/">Home</a></li>
    <span class="pipe">·</span>
    % if defined('username') and username:
    <a href="/{{username}}/">{{username}}</a>
    <span class="pipe">·</span>
    <a href="/{{username}}/tweets/">Tweets</a>
    <span class="pipe">·</span>
    <a href="/{{username}}/followers/">Followers</a>
    <span class="pipe">·</span>
    <a href="/{{username}}/following/">Following</a>
    <span class="pipe">·</span>
    <a href="/{{username}}/random/">Random</a>
    <span class="pipe">·</span>
    <a href="/?action=signout">Sign Out</a>
    % else:
    <a href="/?action=signup">Sign Up</a>
    % end
</div>
