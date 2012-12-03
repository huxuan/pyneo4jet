% for user in users:
<div>
    <div>{{user.username}}</div>
    <div><img src='{{user.avatar}}'/></div>
</div>
% end
% rebase base title=title, username=username
