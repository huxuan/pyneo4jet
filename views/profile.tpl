% if defined('user'):
    <div>Avatar:
        <a href="/{{user.username}}/">
            <img src="/avatar_{{user.username}}" width="35" height="30"/>
        </a>
    </div>
    <div>Name: {{user.name}}</div>
    <div>Gender: {{user.gender}}</div>
    <div>Hometown: {{user.hometown}}</div>
% end
% if user.username == owner.username:
<a href="/{{user.username}}/?action=profile">Update Profile</a>
<a href="/{{user.username}}/?action=password">Update Password</a>
% elif isfollow:
<form action="/{{user.username}}/?action=unfollow" method="POST">
    <input type="submit" value='unfollow'/>
</form>
% else:
<form action="/{{user.username}}/?action=follow" method="POST">
    <input type="submit" value='follow'/>
</form>
% end
% for tweet in tweets:
<div>
    <a href="/{{tweet.username}}/">
        <img src="/avatar_{{tweet.username}}" width="35" height="30"/>
        <strong>{{tweet.username}}: </strong>
    </a>
    <div><strong>{{tweet.text}}</strong></div>
    <div>{{tweet.created_at}}</div>
</div>
% end
% rebase base title=user.username, username=user.username
