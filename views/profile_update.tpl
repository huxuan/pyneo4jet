<div class="profile_update">
    <p class="title">Update Profile</p>
    <div class="content">
        <form action="/{{user.username}}/?action=profile" method="POST" enctype="multipart/form-data">
        <div>
            Name:
            <br />
            <input type="text" name="name" value="{{user.name}}"/>
        </div>
        <div>
            Gender:
            <br />
            <select name="gender">
                <option value=""></option>
                % if user.gender == 'Male':
                <option value="Male" selected="selected">Male</option>
                % else:
                <option value="Male">Male</option>
                % end
                % if user.gender == 'Female':
                <option value="Female" selected="selected">Female</option>
                % else:
                <option value="Female">Female</option>
                % end
            </select>
        </div>
        <div>
            Hometown:
            <br />
            <input type="text" name="hometown" value="{{user.hometown}}"/>
        </div>
        <div>
            Avatar:
            <br />
            <input type="file" name="avatar"/>
        </div>
        <div>
            <input type="submit" class="button" name="update" value="Update"/>
        </div>
    </div>
    % if defined('msg'):
        <div class="msg">{{msg}}</div>
    % end
</div>
% rebase base title="Profile Update", username=user.username
