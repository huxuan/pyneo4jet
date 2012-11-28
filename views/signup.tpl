<form action="/?method=signup" method="POST">
    username: <input type="text" name="username" value="{{get('username', '')}}"/>
    <br />
    password: <input type="text" name="password0" value=""/>
    <br />
    password confirm: <input type="text" name="password1" value=""/>
    <br />
    invitation: <input type="text" name="invitation" value=""/>
    <br />
    <input type="submit" name="signup" value="Sign Up"/>
</form>
%if defined('msg'):
    <div>{{msg}}</div>
%end
%rebase base title="Sign Up",username=get('username')
