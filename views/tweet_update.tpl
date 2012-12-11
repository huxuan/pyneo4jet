% if defined('msg'):
    <div class="msg">{{msg}}</div>
% end
% rebase base title="Tweet Update", username=user.username, tweet_form=True
