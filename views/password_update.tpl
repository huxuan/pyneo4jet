<style type="text/css">p.pos_abs{position:absolute;left:80px;top:400px}</style>

			<form action="/{{user.username}}/?action=password" method="POST">
					<table width="320" height="115" bgcolor="ACDAE5" border="0" align="left" cellpadding="0" cellspacing="0">
							<tr align="center" valign="middle">            
									<td height="24" colspan="2">
											<font color="#505875"><STRONG>=== Password Update ===</STRONG></font> 
									</td>          
							</tr>
							<tr>
									<td align="right" valign="middle">Old Password:
			            </td>            
			            <td>
			            	<input type="password" style="width:150px;height:22px" name="old_pw" value=""/>
			    				</td>
			        </tr>          
			        <tr>            
			        	  <td align="right" valign="middle">New Password:
			        	  </td>            
			            <td>
			              <input type="password" style="width:150px;height:22px" name="new_pw1" value=""/>
			    			 </td>          
			       </tr>
			       <tr>            
			        	  <td align="right" valign="middle">New Password Confirm: 
			        	  </td>            
			            <td>
			              <input type="password" style="width:150px;height:22px" name="new_pw2" value=""/>
			    			 </td>          
			       </tr>
			       <tr align="center" valign="middle">            
			            <td height="27" colspan="2">
			    					<input type="submit" name="update" value="Update"/>
			    				</td>          
				     </tr> 
				 </table>
			</form>
% if defined('msg'):
		<p align="left" class="pos_abs"><STRONG>{{msg}}</STRONG></p>
% end
% rebase base title="Password Update", username=user.username
