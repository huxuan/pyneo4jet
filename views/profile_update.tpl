<form action="/{{user.username}}/?action=profile" method="POST" enctype="multipart/form-data">
    Name: <input type="text" name="name" value="{{user.name}}"/>
    <br />
    Gender:
    <select name="gender">
        <option value=""></option>
        % if user.gender == 'Male':
            <option value="Male" selected="selected">Male</option>
            <option value="Female">Female</option>
        % else:
            <option value="Male">Male</option>
            <option value="Female" selected="selected">Female</option>
        % end
    </select>
    <br />
    Hometown: <input type="text" name="hometown"/>
    <br />
    avatar: <input type="file" name="avatar"/>
    <br />
    <input type="submit" name="update" value="Update"/>
</form>
% if defined('msg'):
    <div>{{msg}}</div>
% end
% rebase base title="Profile Update", username=user.username
