<div>{{user.username}}</div>
<div><img src={{user.avatar}} /></div>
% for tweet in tweets:
<div>
    <div>{{tweet.username}}</div>
    <div>{{tweet.text}}</div>
    <div>{{tweet.created_at}}</div>
</div>
% end
% rebase base title=user.username, username=user.username
