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
            <input type="text" name="username" value="{{get('username', '')}}"/>
        </div>
        <div>
            <input type="submit" class="button" name="signin" value="Sign In"/>
        </div>
    </form>
</div>
<table width="240" height="139"  border="0" align="center" cellpadding="0" cellspacing="0">
    <tr>
        <td height="139" align="center">
            <form action="/" method="POST">
                <table width="320" height="115" bgcolor="ACDAE5" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tr align="center" valign="middle">
                        <td height="24" colspan="2">
                            <font color="#505875"><strong>=== Sign In ===</strong></font>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" valign="middle">Username:</td>
                        <td><input type="text" style="width:150px;height:22px" name="username" value="{{get('username', '')}}"/></td>
                    </tr>
                    <tr>
                        <td align="right" valign="middle">Password:</td>
                        <td><input type="password" style="width:150px;height:22px" name="password" value=""/></td>
                    </tr>
                    <tr align="center" valign="middle">
                        <td height="27" colspan="2">
                            <input type="submit" name="signin" value="Sign In"/>
                        </td>
                    </tr>
                </table>
            </form>
        </td>
    </tr>
</table>
% if defined('msg'):
<p align="center" ><strong>{{msg}}</strong></p>
% end
% rebase base title="SignIn"
