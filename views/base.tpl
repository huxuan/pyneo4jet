<html>
<link rel="stylesheet" href="/style.css" />
<head>
    <title>{{get('title', '') and '%s | ' % title }}pyneo4jet</title>
</head>
<body>
    % include nav username=get('username')
    % setdefault('tweet_form', False)
    % if tweet_form:
        % include tweet_form username=get('username')
    % end
    % include
</body>
</html>
