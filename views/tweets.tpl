% for tweet in tweets:
<div>
    <a href="/{{tweet.username}}/"><img src="/avatar_{{tweet.username}}" width="35" height="30"/>
		<a style="font-size: 18px;" href="/{{tweet.username}}/"><STRONG>{{tweet.username}}: </STRONG></a>
		<div><STRONG>{{tweet.text}}</STRONG></div>
		<div>{{tweet.created_at}}</div>
		</br>
		</br>
</div>
% end
% rebase base title=title, username=username
