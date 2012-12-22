% if defined('ownername') and ownername:
<form action="/{{ownername}}/?action=tweet" method="POST">
    <div class="recommendTopic clearfix">
        <div id="textAdContainer" class="recommendTopic-topic"></div>
    </div>
    <div class="statusUpdate">
        <div id="publishBox" class="publishBox disabled" data-nest="false">
            <div class="publishBox-bd">
                <div class="publishBox-textareaBox">
                    <textarea name="text" class="publishBox-textarea"></textarea>
                </div>
            </div>
            <input type="submit" class="button" name="update" value="Tweet!"/>
        </div>
    </div>
</form>
% end
