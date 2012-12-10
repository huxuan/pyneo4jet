<form action="/{{user.username}}/?action=profile" method="POST" enctype="multipart/form-data">
    <table width="320" height="115" bgcolor="ACDAE5" border="0" align="left" cellpadding="0" cellspacing="0">
        <tr align="center" valign="middle">
            <td height="24" colspan="2">
                <font color="#505875"><strong>=== Profile Update ===</strong></font>
            </td>
        </tr>
        <tr>
            <td align="right" valign="middle">Name:</td>
            <td><input type="text" style="width:150px;height:22px" name="name" value="{{user.name}}"/></td>
        </tr>
        <tr>
            <td align="right" valign="middle">Gender:</td>
            <td>
                <select name="gender" style="width:150px;height:22px">
                    <option value=""></option>
                    % if user.gender == 'Male':
                    <option value="Male" selected="selected">Male</option>
                    <option value="Female">Female</option>
                    % else:
                    <option value="Male">Male</option>
                    <option value="Female" selected="selected">Female</option>
                    % end
                </select>
            </td>
        </tr>
        <tr>
            <td align="right" valign="middle">Hometown:</td>
            <td>
                <input type="text" style="width:150px;height:22px" name="hometown" value="{{user.hometown}}"/>
            </td>
        </tr>
        <tr>
            <td align="right" valign="middle">Avatar:</td>
            <td><input type="file" style="width:150px;height:22px" name="avatar"/></td>
        </tr>
        <tr align="center" valign="middle">
            <td height="27" colspan="2">
                <input type="submit" name="update" value="Update"/>
            </td>
        </tr>
    </table>
</form>
% if defined('msg'):
    <div>{{msg}}</div>
% end
% rebase base title="Profile Update", username=user.username
