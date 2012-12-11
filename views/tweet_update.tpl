% if defined('tweet_msg'):
    <div>{{tweet_msg}}</div>
% end
% rebase base title="Tweet Update", username=user.username, tweet_form=True
