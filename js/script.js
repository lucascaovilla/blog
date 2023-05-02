function br() {
    document.write('<br>');
}

function print(text) {
    document.write(text);
}



function showPosts() {
    for(var i = 0; i < listPosts.length; i++) {
        
        const mainDiv = document.getElementById('main-div');
        
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
    
        
        mainDiv.insertAdjacentHTML('beforeend', '<div class="post" id="' + divPostId + '">');
        var divPost = document.getElementById(divPostId);
        
        
        
        divPost.insertAdjacentHTML('beforeend', '<div class="post-title" id="' + divTitleId + '">');
        var divTitle = document.getElementById(divTitleId);
        divTitle.insertAdjacentHTML('beforeend', '<label>' + postTitle + '</label>');
            
        divPost.insertAdjacentHTML('beforeend', '<div class="post-text" id="' + divTextId + '">');
        var divText = document.getElementById(divTextId);
        divText.insertAdjacentHTML('beforeend', '<label>' + postText + '</label>');
            
        divPost.insertAdjacentHTML('beforeend', '<div class="post-info" id="' + divInfoId + '">');
        var divInfo = document.getElementById(divInfoId);
        divInfo.insertAdjacentHTML('beforeend', '<label>' + postInfo + '</label>');
        
        divPost.insertAdjacentHTML('beforeend', '<div class="post-link" id="' + divPostLink + '">');
        var divPostLink = document.getElementById(divPostLink);
        divPostLink.insertAdjacentHTML('beforeend', '<a href="' + postLink + '">Read More')

        mainDiv.insertAdjacentHTML('beforeend', '<br>');
    }
}

function showProjects() {
    for(var i = 0; i < listProjects.length; i++) {
        
        const mainDiv = document.getElementById('main-div');
        
        var index = i + 1;

        var projectTitle = listProjects[i][0];
        var projectDescription = listProjects[i][1];
        var projectLink = listProjects[i][2];
        
        var divProjectId = 'project-' + index;
        var divProjectLink = 'project-' + index + '-link';
        var divTitleId = 'project-' + index + '-title';
        var divDescriptionId = 'project-' + index + '-Description';
    
        
        mainDiv.insertAdjacentHTML('beforeend', '<div class="project" id="' + divProjectId + '">');
        var divProject = document.getElementById(divProjectId);
        
        
        
        divProject.insertAdjacentHTML('beforeend', '<div class="project-title" id="' + divTitleId + '">');
        var divTitle = document.getElementById(divTitleId);
        divTitle.insertAdjacentHTML('beforeend', '<label>' + projectTitle + '</label>');
            
        divProject.insertAdjacentHTML('beforeend', '<div class="project-Description" id="' + divDescriptionId + '">');
        var divDescription = document.getElementById(divDescriptionId);
        divDescription.insertAdjacentHTML('beforeend', '<label>' + projectDescription + '</label>');
            
        divProject.insertAdjacentHTML('beforeend', '<div class="project-link" id="' + divProjectLink + '">');
        var divProjectLink = document.getElementById(divProjectLink);
        divProjectLink.insertAdjacentHTML('beforeend', '<a href="' + projectLink + '">Read More')

        mainDiv.insertAdjacentHTML('beforeend', '<br>');
    }
}

function showAbout() {
        
    const mainDiv = document.getElementById('main-div');
    
    mainDiv.insertAdjacentHTML('beforeend', '<div class="about-me" id="about-me">');
    var divAboutMe = document.getElementById("about-me");
    
    var selfHistory = listAbout[0];
    var selfInterests = listAbout[1];
    var selfKnowledge = listAbout[2];
    
    divAboutMe.insertAdjacentHTML('beforeend', '<div class="self-history" id="self-history">');
    var divSelfHistory = document.getElementById("self-history");
    divSelfHistory.insertAdjacentHTML('beforeend', '<label>' + selfHistory + '</label>');
        
    divAboutMe.insertAdjacentHTML('beforeend', '<div class="self-interests" id="self-interests">');
    var divSelfInterests = document.getElementById("self-interests");
    divSelfInterests.insertAdjacentHTML('beforeend', '<label>' + selfInterests + '</label>');

    divAboutMe.insertAdjacentHTML('beforeend', '<div class="self-picture" id="self-picture">');
    var divSelfPicture = document.getElementById("self-picture");
    divSelfPicture.insertAdjacentHTML('beforeend', '<img src="Imagem0082.jpg">');

    divAboutMe.insertAdjacentHTML('beforeend', '<div class="self-info" id="self-info">');
    var divSelfInfo = document.getElementById("self-info");
    divSelfInfo.insertAdjacentHTML('beforeend', '<label>Name</label>');
    divSelfInfo.insertAdjacentHTML('beforeend', '<label>Age</label>');
        
    divAboutMe.insertAdjacentHTML('beforeend', '<div class="self-knowledge" id="self-knowledge">');
    var divSelfKnowledge = document.getElementById("self-knowledge");
    divSelfKnowledge.insertAdjacentHTML('beforeend', '<label>' + selfKnowledge + '</label>');
}

function showCreateAccount() {
        
    const mainDiv = document.getElementById('main-div');
    
    mainDiv.insertAdjacentHTML('beforeend', '<div class="create-account" id="create-account">');
    var divCreateAccount = document.getElementById("create-account");
    
    divCreateAccount.insertAdjacentHTML('beforeend', '<form class="create-account-form" id="create-account-form" action="?index=posts">');
    var formCreateAccount = document.getElementById("create-account-form");
    
    formCreateAccount.insertAdjacentHTML('beforeend', '<div class="input-name" id="input-name">');
    var divInputName = document.getElementById("input-name");
    divInputName.insertAdjacentHTML('beforeend', '<label>Insira seu nome:</label>');
    divInputName.insertAdjacentHTML('beforeend', '<input required></input>');
    
    formCreateAccount.insertAdjacentHTML('beforeend', '<div class="input-email" id="input-email">');
    var divInputEmail = document.getElementById("input-email");
    divInputEmail.insertAdjacentHTML('beforeend', '<label>Insira seu email:</label>');
    divInputEmail.insertAdjacentHTML('beforeend', '<input required></input>');

    formCreateAccount.insertAdjacentHTML('beforeend', '<div class="input-birthday" id="input-birthday">');
    var divInputBirthday = document.getElementById("input-birthday");
    divInputBirthday.insertAdjacentHTML('beforeend', '<label>Insira sua data de nascimento:</label>');
    divInputBirthday.insertAdjacentHTML('beforeend', '<input type="date" required></input>');

    formCreateAccount.insertAdjacentHTML('beforeend', '<div class="input-position" id="input-position">');
    var divInputPosition = document.getElementById("input-position");
    divInputPosition.insertAdjacentHTML('beforeend', '<label>Insira seu cargo:</label>');
    divInputPosition.insertAdjacentHTML('beforeend', '<input required></input>');

        
    formCreateAccount.insertAdjacentHTML('beforeend', '<div class="input-interests" id="input-interests">');
    var divInputInterests = document.getElementById("input-interests");
    divInputInterests.insertAdjacentHTML('beforeend', '<label>Informe 3 interesses seus:</label>');
    divInputInterests.insertAdjacentHTML('beforeend', '<input id="first-interest" required></input>');
    divInputInterests.insertAdjacentHTML('beforeend', '<input id="second-interest" required></input>');
    divInputInterests.insertAdjacentHTML('beforeend', '<input id="third-interest" required></input>');

    formCreateAccount.insertAdjacentHTML('beforeend', '<div class="input-password" id="input-password">');
    var divInputPassword = document.getElementById("input-password");
    divInputPassword.insertAdjacentHTML('beforeend', '<label>Digite uma senha:</label>');
    divInputPassword.insertAdjacentHTML('beforeend', '<input id="first-entry-password" required></input>');
    divInputPassword.insertAdjacentHTML('beforeend', '<br>');
    divInputPassword.insertAdjacentHTML('beforeend', '<label>Repita a senha:</label>');
    divInputPassword.insertAdjacentHTML('beforeend', '<input id="second-entry-password" required></input>');
    divInputPassword.insertAdjacentHTML('beforeend', '<br>');
    divInputPassword.insertAdjacentHTML('beforeend', '<label>A senha deve ter no mínimo 8 dígitos.</label>');

    formCreateAccount.insertAdjacentHTML('beforeend', '<div class="create-account-button" id="create-account-button">');
    var divCreateAccountButton = document.getElementById("create-account-button");
    divCreateAccountButton.insertAdjacentHTML('beforeend', '<button>Criar conta</button>');

}

function showLogin() {
        
    const mainDiv = document.getElementById('main-div');
    
    mainDiv.insertAdjacentHTML('beforeend', '<div class="login" id="login">');
    var divLogin = document.getElementById("login");
    
    divLogin.insertAdjacentHTML('beforeend', '<form class="login-form" id="login-form" action="?index=posts">');
    var formLogin = document.getElementById("login-form");
    
    formLogin.insertAdjacentHTML('beforeend', '<div class="input-email" id="input-email">');
    var divInputEmail = document.getElementById("input-email");
    divInputEmail.insertAdjacentHTML('beforeend', '<label>Insira seu email:</label>');
    divInputEmail.insertAdjacentHTML('beforeend', '<input required></input>');

    formLogin.insertAdjacentHTML('beforeend', '<div class="input-password" id="input-password">');
    var divInputPassword = document.getElementById("input-password");
    divInputPassword.insertAdjacentHTML('beforeend', '<label>Senha:</label>');
    divInputPassword.insertAdjacentHTML('beforeend', '<input id="password" required></input>');

    formLogin.insertAdjacentHTML('beforeend', '<div class="login-button" id="login-button">');
    var divLoginButton = document.getElementById("login-button");
    divLoginButton.insertAdjacentHTML('beforeend', '<button>Login</button>');

}

function showContacts() {
        
    const mainDiv = document.getElementById('main-div');
    
    mainDiv.insertAdjacentHTML('beforeend', '<div class="contacts" id="contacts">');
    var divContacts = document.getElementById("contacts");

    divContacts.insertAdjacentHTML('beforeend', '<h4 class="text-uppercase mb-4">Contacts, Portfolio and Social Media</h4>');
    divContacts.insertAdjacentHTML('beforeend', '<a href="https://lucasgrisac@gmail.com">gmail</a>');
    divContacts.insertAdjacentHTML('beforeend', '<a href="https://github.com/lucascaovilla">github</a>');
    divContacts.insertAdjacentHTML('beforeend', '<a href="https://www.linkedin.com/in/lucasgcaovilla/">linkedin</a>');
}




var listPosts = [['post1', 'text1', 'info1', 'link1'], ['post2', 'text2', 'info2', 'link2'], ['post3', 'text3', 'info3', 'link3']];
var listProjects = [['project1', 'description1', 'link1'], ['project2', 'description2', 'link2'], ['project3', 'description3', 'link3']];
var listAbout = ["about me", "my interests", "my techs"];

function urlParam() {
    let paramString = window.location.href.split('?')[1];
    let queryString = new URLSearchParams(paramString);
    
    var param = "";

    for (let pair of queryString.entries()) {
       param = pair[1];
    }
    return param
}

console.log(urlParam())


const paramDict = {'posts': showPosts, 'projects': showProjects, 'about': showAbout, 'create-account': showCreateAccount, 'login': showLogin, 'contacts': showContacts};

function renderParam(param) {
    return paramDict[param]()
}

renderParam(urlParam());