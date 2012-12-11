<p class="title">Welcome to pyneo4jet!</p>
<div class="content">
    <form action="/" method="POST">
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
            <input type="submit" class="button" name="signin" value="Sign In"/>
        </div>
    </form>
</div>
% if defined('msg'):
<p class='msg'>{{msg}}</p>
% end
% rebase base title="SignIn"
