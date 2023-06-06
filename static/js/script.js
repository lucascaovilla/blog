$(document).ready(function(){  
     $('#login-button').click(function(){  
          var username = $('#login-username').val();  
          var password = $('#login-password').val();  
          if(username != '' && password != '') {  
               $.ajax({  
                    url:"/login",  
                    method:"POST",  
                    data: {username:username, password:password},  
                    success:function(data) {
                         if(data == 'No-data') {  
                              alert("Invalid Username or Password!");  
                         } else {  
                              alert(data);
                              $('#loginModal').hide();  
                              location.reload();  
                         }  
                    }  
               });  
          } else {  
               alert("Both Fields are required");  
          }  
     });    
});


$(document).ready(function(){  
     $('#create-account-button').click(function(){  
          var username = $('#create-account-username').val();  
          var email = $('#create-account-email').val();  
          var password = $('#create-account-password').val();
          var confPassw = $('#create-account-confirm-password').val();
          if(password !== confPassw) {
               alert("The passwords must be the same.")
          } else {
               if(username != '' && email != '' && password != '') {  
                    $.ajax({  
                         url:"/create-account",  
                         method:"POST",  
                         data: {username:username, email:email, password:password},  
                         success:function(data) {
                              if(data == 'No-data') {  
                                   alert("This Email already have an account!");  
                              } else {  
                                   alert(data);
                                   $('#createAccountModal').hide();  
                                   location.reload();  
                              }  
                         }  
                    });  
               } else {  
                    alert("All Fields are required");  
               }  
          }
          });    
     });