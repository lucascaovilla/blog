$(document).ready(function(){  
     $('#login_button').click(function(){  
          var username = $('#username').val();  
          var password = $('#password').val();  
          if(username != '' && password != '')  
          {  
               $.ajax({  
                    url:"/action",  
                    method:"POST",  
                    data: {username:username, password:password},  
                    success:function(data)  
                    {  
                         if(data == 'No-data')  
                         {  
                              alert("Invalid Email Or Password!");  
                              }  
                              else 
                              {  
                              alert(data);
                              $('#loginModal').hide();  
                              location.reload();  
                         }  
                    }  
               });  
          }  
          else 
          {  
               alert("Both Fields are required");  
          }  
     });    
});  
