<form action="/{{user.username}}/?action=profile" method="POST" enctype="multipart/form-data">
    username: <input type="text" name="username" value="{{get('username', '')}}"/>
    <br />
    avatar: <input type="file" name="avatar"/>
    <br />
    <input type="submit" name="update" value="Update"/>
</form>
% if defined('msg'):
    <div>{{msg}}</div>
% end
% rebase base title="Profile Update", username=user.username
