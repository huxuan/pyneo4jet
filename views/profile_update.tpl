<form action="/{{user.username}}?action=profile" method="POST">
    username: <input type="text" name="username" value="{{get('username', '')}}"/>
    <br />
    <input type="submit" name="update" value="Update"/>
</form>
% if defined('msg'):
    <div>{{msg}}</div>
% end
% rebase base title="Profile Update", username=user.username
