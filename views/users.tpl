% for user in users:
<div>
    <div>{{user.username}}</div>
    <div><img src='/avatar_{{user.username}}'/></div>
</div>
% end
% rebase base title=title, username=username
