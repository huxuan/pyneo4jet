<div class="users">
    % for user in users:
    % if users.index(user) % 2 == 0:
    <div class="user even">
    % else:
    <div class="user odd">
    % end
        <div class="avatar">
            <a href="/{{user.username}}/">
                <img src="/avatar_{{user.username}}"/>
            </a>
        </div>
        <div class="user-side">
            <a href="/{{user.username}}/">
                <div class="name">{{user.username}}</div>
            </a>
        </div>
    </div>
    % end
</div>
% rebase base title=title, username=username
