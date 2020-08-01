
firebase.auth().onAuthStateChanged(function(user) {
    if (user) {

        var userId = firebase.auth().currentUser.uid;
        // return firebase.database().ref('/users/' + userId).once('value').then(function(snapshot) {
        //   var username = (snapshot.val() && snapshot.val().username) || 'Anonymous';
        //   // ...consol
        //   console.log(username)
        // });

        var Usersref = firebase.database().ref("users/");

        Usersref.orderByChild("name").on("child_added", function(data) {
           if(data.val().userId==userId){ 
                uservalues = [data.val().regname,data.val().regnumber,data.val().emergency1,data.val().emergency2,data.val().emergency3];
                console.log(uservalues)
            }
        });


        
    $(document).ready(function(){

        var wlat,wlong,x;
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(getLocation);
        }
        else {
        console("not found");
        };
    
        function getLocation(position) {
            wlat = position.coords.latitude;
            wlong = position.coords.longitude;
            x = wlat+","+wlong
    
        }
        
  $("#help_me").click(function(){
      alert("help");

    
    y = user__information();
    console.log(y);

    
        
    $.post("https://ff3f8c36a9a1.ngrok.io/hello",
    {
        username :y[0],
        usercontact:y[1],
        emergency1 : y[2],
        emergency2 : y[3],
        emergency3 : y[4],
        location : wlat+","+wlong,

    },
    function(data,status){
      alert("Data: " + data + "\nStatus: " + status);
    });
      
      
 



  });
});





       
      

    } else {
      // No user is signed in.



        
    $(document).ready(function(){

        var wlat,wlong,x;
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(getLocation);
        }
        else {
        console("not found");
        };
    
        function getLocation(position) {
            wlat = position.coords.latitude;
            wlong = position.coords.longitude;
            x = wlat+","+wlong
    
        }
        
  $("#help_me").click(function(){
      alert("help");

    
 
        
    $.post("https://ff3f8c36a9a1.ngrok.io/hellowithoutsignin",
    {

        location : wlat+","+wlong,

    },
    function(data,status){
      alert("Data: " + data + "\nStatus: " + status);
    });
      
      
 



  });
});




      console.log("sign in")
    }
  });



      
      


function user__information()
{
    var userId = firebase.auth().currentUser.uid;
    // return firebase.database().ref('/users/' + userId).once('value').then(function(snapshot) {
    //   var username = (snapshot.val() && snapshot.val().username) || 'Anonymous';
    //   // ...consol
    //   console.log(username)
    // });

    var Usersref = firebase.database().ref("users/");

    Usersref.orderByChild("name").on("child_added", function(data) {
       if(data.val().userId==userId){ 
            uservalues = [data.val().regname,data.val().regnumber,data.val().emergency1,data.val().emergency2,data.val().emergency3];
            console.log(uservalues)
        }
    });
    return(uservalues)
}














function register_user_to_firebase(){
    console.log("register")


document.getElementById("sign-up-form").addEventListener('submit',function(e){
    e.preventDefault();
    var regnumber = document.getElementById("regnumber").value;
    var regname = document.getElementById("regname").value;
    var regmail = document.getElementById("regmail").value;
    var regstate = document.getElementById("regstate").value;
    var emergency1 = document.getElementById("emergency1").value;
    var emergency2 = document.getElementById("emergency2").value;
    var emergency3 = document.getElementById("emergency3").value;
    var regvol = document.getElementById("regvol").checked;
    var regpass = document.getElementById("regpass").value;


    firebase.auth().createUserWithEmailAndPassword(regmail, regpass)
    .then(function(response){
        alert("trying")
        firebase.database().ref('users').push({
            regnumber : regnumber,
            regname : regname,
            
            regstate : regstate ,
            regvol : regvol,
            emergency1 : emergency1,
            emergency2 : emergency2,
            emergency3 : emergency3,
            userId : firebase.auth().currentUser.uid,
            regmail : firebase.auth().currentUser.email})
    }).catch(function(error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log(errorMessage)
        // ...
      });

});

// window.location.replace('main.html')

}



function login_user()
{
    document.getElementById("sign-in-form").addEventListener('submit',function(e){
        e.preventDefault();
        
        var loginmail = document.getElementById("loginmail");
        
        var loginpassword = document.getElementById("loginpassword");


        firebase.auth().signInWithEmailAndPassword(loginmail.value,loginpassword.value)
        .catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            alert(errorMessage)
            // ...
          });
          alert("signed in")
    
    });
    
    // window.location.replace('main.html')
}


function help_me_user()
{




}