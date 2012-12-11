<div class="tweets">
    % for tweet in tweets:
    % if tweets.index(tweet) % 2 == 0:
    <div class="tweet even">
    % else:
    <div class="tweet odd">
    % end
        <div class="avatar">
            <a href="/{{tweet.username}}/">
                <img src="/avatar_{{tweet.username}}"/>
            </a>
        </div>
        <div class="tweet-side">
            <a href="/{{tweet.username}}/">
                <div class="name">{{tweet.username}}</div>
            </a>
            <div class="text">{{tweet.text}}</div>
            <div class="date">{{tweet.created_at}}</div>
        </div>
    </div>
    % end
</div>
