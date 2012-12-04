% if defined('username') and username:
<form action="/{{username}}/?action=tweet" method="POST">
    <textarea name="text"></textarea>
    <br />
    <input type="submit" name="update" value="Update"/>
</form>
% end
