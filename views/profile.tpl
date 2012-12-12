<div class="content">
    <div class="profile">
        % if defined('user'):
        <div class="avatar">
            <a href="/{{user.username}}/">
                <img src="/avatar_{{user.username}}"/>
            </a>
        </div>
        <div class="profile-side">
            <div class="name">{{user.name}}</div>
            % if user.gender:
            <div class="gender">{{user.gender}}</div>
            % end
            % if user.hometown:
            <div class="hometown">{{user.hometown}}</div>
            % end
        </div>
        % end
        <div class="action">
            % if user.username == owner.username:
            <div class="update">
                [
                <a href="/{{user.username}}/?action=profile">Update Profile</a>
                |
                <a href="/{{user.username}}/?action=password">Update Password</a>
                ]
            </div>
            % elif isfollow:
            <form action="/{{user.username}}/?action=unfollow" method="POST">
                <input class="button" type="submit" value='unfollow'/>
            </form>
            % else:
            <form action="/{{user.username}}/?action=follow" method="POST">
                <input class="button" type="submit" value='follow'/>
            </form>
            % end
        </div>
    </div>
    % include tweets_list tweets=tweets
</div>
% rebase base title=user.username, username=user.username
