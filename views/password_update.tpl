<form action="/{{user.username}}/?action=password" method="POST">
    old password: <input type="password" name="old_pw" value=""/>
    <br />
    new password: <input type="password" name="new_pw1" value=""/>
    <br />
    new password confirm: <input type="password" name="new_pw2" value=""/>
    <br />
    <input type="submit" name="update" value="Update"/>
</form>
% if defined('msg'):
    <div>{{msg}}</div>
% end
% rebase base title="Password Update", username=user.username
