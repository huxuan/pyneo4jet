<div class="nav">
    |<a style="font-size: 36px;" href="/"><strong>Home</strong></a></li>|
    % if defined('username') and username:
    <a style="font-size: 36px;" href="/{{username}}/"><strong>{{username}}</strong></a>|
    <a style="font-size: 36px;" href="/{{username}}/tweets/"><strong>Tweets</strong></a>|
    <a style="font-size: 36px;" href="/{{username}}/followers/"><strong>Followers</strong></a>|
    <a style="font-size: 36px;" href="/{{username}}/following/"><strong>Following</strong></a>|
    <a style="font-size: 36px;" href="/{{username}}/random/"><strong>Random</strong></a>|
    <a style="font-size: 36px;" href="/?action=signout"><strong>Sign Out</strong></a>|
    % else:
    <a style="font-size: 36px;" href="/?action=signup"><strong>Sign Up</strong></a>|
    % end
</div>
