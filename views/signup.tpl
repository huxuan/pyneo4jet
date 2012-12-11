<p class="title">Register pyneo4jet!</p>
<div class="content">
    <form action="/?action=signup" method="POST">
        <div>
            Username:
            <br />
            <input type="text" name="username" value="{{get('username', '')}}"/>
        </div>
        <div>
            Password:
            <br />
            <input type="password" name="password" value=""/>
        </div>
        <div>
            Password Confirm:
            <br />
            <input type="password" name="password_confirm" value=""/>
        </div>
        <div>
            Invitation:
            <br />
            <input type="text" name="invitation" value=""/>
        </div>
        <div>
            <input type="submit" class="button" name="signup" value="Sign Up"/>
        </div>
    </form>
</div>
%if defined('msg'):
<p class="msg">{{msg}}</p>
%end
%rebase base title="Sign Up"
