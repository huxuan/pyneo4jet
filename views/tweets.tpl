% for tweet in tweets:
<div>
    <a href="/{{tweet.username}}/"><img src="/avatar_{{tweet.username}}" width="35" height="30"/>
        <a style="font-size: 18px;" href="/{{tweet.username}}/">
        <strong>{{tweet.username}}: </strong>
    </a>
    <div><strong>{{tweet.text}}</strong></div>
    <div>{{tweet.created_at}}</div>
</div>
% end
% rebase base title=title, username=username
