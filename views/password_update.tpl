<div class="password_update">
	<p class="title">Change Your Password</p>
	<div class="content">
	    <form action="/{{user.username}}/?action=password" method="POST">
	        <div>
	            Old Password:
	            <br />
	            <input type="password" name="old_pw" value=""/>
	        </div>
	        <div>
	            New Password:
	            <br />
	            <input type="password" name="new_pw1" value=""/>
	        </div>
	        <div>
	            New Password Confirm:
	            <br />
	            <input type="password" name="new_pw2" value=""/>
	        </div>
	        <div>
	            <input type="submit" name="update" value="Update"/>
	        </div>
	    </form>
	</div>
	% if defined('msg'):
	    <p class="msg">{{msg}}</p>
	% end
</div>
% rebase base title="Password Update", username=user.username
