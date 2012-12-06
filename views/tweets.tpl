% for tweet in tweets:
<div>
    <div>{{tweet.username}}</div>
    <div>{{tweet.text}}</div>
    <div>{{tweet.created_at}}</div>
</div>
% end
% rebase base title=title, username=username
