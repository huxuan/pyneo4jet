<form action="/?method=signup" method="POST">
    username: <input type="text" name="username" value="{{get('username', '')}}"/>
    <br />
    password: <input type="password" name="password" value=""/>
    <br />
    invitation: <input type="text" name="invitation" value=""/>
    <br />
    <input type="submit" name="signup" value="Sign Up"/>
</form>
%if defined('msg'):
    <div>{{msg}}</div>
%end
%rebase base title="Sign Up",username=get('username')
