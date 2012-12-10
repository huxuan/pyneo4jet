<div><a href="/{{user.username}}/"><img src="/avatar_{{user.username}}" width="35" height="30"/></a>
<a href="/{{user.username}}/">{{user.username}}</a></div>
<div>Name: {{user.name}}</div>
<div>Gender: {{user.gender}}</div>
<div>Hometown: {{user.hometown}}</div>
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
		<a style="font-size: 18px;" href="/{{tweet.username}}/"><STRONG>{{tweet.username}}</STRONG></a>
    <div>{{tweet.text}}</div>
    <div>{{tweet.created_at}}</div>
</div>
% end
% rebase base title=user.username, username=user.username

