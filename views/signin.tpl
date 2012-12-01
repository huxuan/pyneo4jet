<form action="/" method="POST">
    username: <input type="text" name="username" value="{{get('username', '')}}"/>
    <br />
    password: <input type="password" name="password" value=""/>
    <br />
    <input type="submit" name="signin" value="Sign In"/>
</form>
% if defined('msg'):
    <div>{{msg}}</div>
% end
% rebase base title="SignIn"
