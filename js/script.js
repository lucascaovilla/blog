function br() {
    document.write('<br>');
}

function print(text) {
    document.write(text);
}



function showPosts() {
    for(var i = 0; i < listPosts.length; i++) {
        
        const divPosts = document.getElementById('posts-list');
        
        var index = i + 1;

        var postTitle = listPosts[i][0];
        var postText = listPosts[i][1];
        var postInfo = listPosts[i][2];
        var postLink = listPosts[i][3];
        
        var divPostId = 'post-' + index;
        var divPostLink = 'post-' + index + '-link';
        var divTitleId = 'post-' + index + '-title';
        var divTextId = 'post-' + index + '-text';
        var divInfoId = 'post-' + index + '-info';
    
        
        divPosts.insertAdjacentHTML('beforeend', '<div class="post" id="' + divPostId + '">');
        var divPost = document.getElementById(divPostId);
        
        
        
        divPost.insertAdjacentHTML('beforeend', '<div id="' + divTitleId + '">');
        var divTitle = document.getElementById(divTitleId);
        divTitle.insertAdjacentHTML('beforeend', '<label>' + postTitle + '</label>');
            
        divPost.insertAdjacentHTML('beforeend', '<div id="' + divTextId + '">');
        var divText = document.getElementById(divTextId);
        divText.insertAdjacentHTML('beforeend', '<label>' + postText + '</label>');
            
        divPost.insertAdjacentHTML('beforeend', '<div id="' + divInfoId + '">');
        var divInfo = document.getElementById(divInfoId);
        divInfo.insertAdjacentHTML('beforeend', '<label>' + postInfo + '</label>');
        
        divPost.insertAdjacentHTML('beforeend', '<div id="' + divPostLink + '">');
        var divPostLink = document.getElementById(divPostLink);
        divPostLink.insertAdjacentHTML('beforeend', '<a href="' + postLink + '">Read More')

        divPosts.insertAdjacentHTML('beforeend', '<br>');
    }
}

var listPosts = [['post1', 'text1', 'info1', 'link1'], ['post2', 'text2', 'info2', 'link2'], ['post3', 'text3', 'info3', 'link3'], ['post1', 'text1', 'info1', 'link1'], ['post2', 'text2', 'info2', 'link2'], ['post3', 'text3', 'info3', 'link3'], ['post1', 'text1', 'info1', 'link1'], ['post2', 'text2', 'info2', 'link2'], ['post3', 'text3', 'info3', 'link3']];
    
showPosts();