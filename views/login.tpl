<form action="/" method="POST">
    username: <input type="text" name="username" value="{{get('username', '')}}"/>
    <br />
    password: <input type="password" name="password" value=""/>
    <br />
    <input type="submit" name="login" value="login"/>
</form>
%if defined('msg'):
    <div>{{msg}}</div>
%end
%rebase base title="login",username=get('username')
