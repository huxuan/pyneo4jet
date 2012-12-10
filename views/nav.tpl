<div class="nav">
    |<a style="margin-left: 30px;" style="font-size: 36px;" href="/"><STRONG>Home</STRONG></a></li>|
    % if defined('username') and username:
    <a style="font-size: 36px;" href="/{{username}}/"><STRONG>{{username}}</STRONG></a>|
    <a style="font-size: 36px;" href="/{{username}}/tweets/"><STRONG>Tweets</STRONG></a>|
    <a style="font-size: 36px;" href="/{{username}}/followers/"><STRONG>Followers</STRONG></a>|
    <a style="font-size: 36px;" href="/{{username}}/following/"><STRONG>Following</STRONG></a>|
    <a style="font-size: 36px;" href="/{{username}}/random/"><STRONG>Random</STRONG></a>|
    <a style="font-size: 36px;" href="/?action=signout"><STRONG>Sign Out</STRONG></a>|
    % else:
    <a style="font-size: 36px;" href="/?action=signup"><STRONG>Sign Up</STRONG></a>|
    % end
</div>
