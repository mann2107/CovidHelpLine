function showLogin()
{
    $("#divRegister").addClass("d-none")
    $("#divOTP").addClass("d-none")
    $("#divLogin").removeClass("d-none")

}


function showRegister()
{
    $("#divRegister").removeClass("d-none")
    $("#divOTP").addClass("d-none")
    $("#divLogin").addClass("d-none")

}

function showOTP()
{
    $("#divRegister").addClass("d-none")
    $("#divOTP").removeClass("d-none")
    $("#divLogin").addClass("d-none")

}


function submitLogin()
{
    if($("#mobile_login").val() == "" || $("#password").val() == "")
    {
        alert("Please enter required details.")
        return;
    }

    $.ajax({
      type: "POST",
      url: "/sign_in",
      data: {
        mobile: $("#mobile_login").val(),
        password: $("#password").val()
      },
      success: function (result) {
        if(result.status=="success")
        {
        if(localStorage.getItem("mode") != null)
            location.href="/" + localStorage.getItem("mode");
            }
            else
            {
            alert(result.msg)
            }
      }
    });
}

function submitRegister()
{
    if($("#mobile_register").val() == "" || $("#newpassword").val() == "" || $("#confirmpassword").val() == "")
    {
        alert("Please enter required details.")
        return;
    }

    if($("#newpassword").val() != $("#confirmpassword").val())
    {
        alert("New Password and confirm password should be same")
        return;
    }

    $.ajax({
      type: "POST",
      url: "/sign_up",
      data: {
        mobile: $("#mobile_register").val(),
        password: $("#newpassword").val()
      },
      success: function (result) {
        if(result.status=="success")
                showOTP()
                else
                {
                alert(result.msg)
                }
              }
            });
    }



function submitOTP()
{

    if($("#otp").val() == "")
    {
        alert("Please enter required details.")
        return;
    }

    $.ajax({
      type: "POST",
      url: "/verify_phone_otp",
      data: {
        mobile: $("#mobile_register").val(),
        otp: $("#otp").val()
      },
      success: function (result) {
      alert(result);
        if(result.status=="success"){
                if(localStorage.getItem("mode") != null)
                   location.href="/" + localStorage.getItem("mode");

        } else{
          alert(result.msg);
        }
}

    });
}

