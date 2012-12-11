% if defined('username') and username:
<form action="/{{username}}/?action=tweet" method="POST">
    <textarea name="text" class="text" size="20"></textarea>
    <input type="submit" class="button" name="update" value="Tweet!"/>
</form>
% end
