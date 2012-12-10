<div><a href="/{{user.username}}/"><img src="/avatar_{{user.username}}" width="35" height="30"/></a>
<a href="/{{user.username}}/">{{user.username}}</a></div>
</br>
% if defined('user') and user.name:
<div>Name: {{user.name}}</div>
% end
% if defined('user') and user.gender:
<div>Gender: {{user.gender}}</div>
% end
% if defined('user') and user.hometown:
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
</br>
</br>
</br>
% for tweet in tweets:
<div>
		<a style="font-size: 18px;" href="/{{tweet.username}}/"><STRONG>{{tweet.username}}</STRONG></a>
    <div>{{tweet.text}}</div>
    <div>{{tweet.created_at}}</div>
</div>
% end
% rebase base title=user.username, username=user.username

