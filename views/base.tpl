<html>
    <link rel="stylesheet" href="/style.css" />
    <head>
        <title>{{get('title', '') and '%s | ' % title }}pyneo4jet</title>
    </head>
    <body>
        % include nav username=get('username')
        <div class="content_base clearfix" style="overflow:hidden">
            <div class="conL" style="height: auto; ">
                <div class="conL-inner">
                % setdefault('tweet_form', False)
                % if tweet_form:
                    % include tweet_form username=get('username')
                % end
                % include
                </div>
            </div>
        </div>
    </body>
</html>
