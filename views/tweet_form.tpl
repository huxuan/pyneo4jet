% if defined('username') and username:
<form action="/{{username}}/?action=tweet" method="POST">
    <table>
        <tr>
            <div><textarea name="text" rows="5" cols="80" ></textarea></div>
        </tr>
        <tr>
            <td>
                <input type="submit" name="update" align="center" value="Update"/>
            </td>
        </tr>
    </table>
</form>
% end
