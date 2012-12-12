<table width="440" height="512"  border="0" align="center" cellpadding="0" cellspacing="0">
    <tr align="center" valign="middle">
        <td height="154" colspan="2">
            <h1 class="title" >Register pyneo4jet!</h1>
        </td>
    </tr>
    <tr>
        <td height="139" align="center">
            <form action="/?action=signup" method="POST">
                <table width="320" height="215" bgcolor="ACDAE5" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tr align="center" valign="middle">
                        <td height="24" colspan="2">
                            <font color="#505875"><STRONG>=== Register ===</STRONG></font>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" valign="middle">
                            Username:
                        </td>
                        <td>
                            <input type="text" style="width:150px;height:22px" name="username" value="{{get('username', '')}}"/>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" valign="middle">
                            Password:
                        </td>
                        <td>
                            <input type="password" style="width:150px;height:22px" name="password" value=""/>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" valign="middle">
                            Password Confirm:
                        </td>
                        <td>
                            <input type="password" style="width:150px;height:22px" name="password_confirm" value=""/>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" valign="middle">
                            Invitation:
                        </td>
                        <td>
                            <input type="text" style="width:150px;height:22px" name="invitation" value=""/>
                        </td>
                    </tr>
                    <tr align="center" valign="middle">
                        <td height="27" colspan="2">
                            <input type="submit" name="signup" value="Sign Up"/>
                        </td>
                    </tr>
                </table>
            </form>
            %if defined('msg'):
                <p class="msg">{{msg}}</p>
            %end
        </td>
    </tr>
</table>
%rebase base title="Sign Up"
