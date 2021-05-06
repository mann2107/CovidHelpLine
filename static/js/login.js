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
      url: "/",
      data: {
        mobile: $("#mobile_login").val(),
        password: $("#password").val()
      },
      success: function () {

        if(localStorage.getItem("mode") != null)
            location.href="/" + localStorage.getItem("mode");
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
showOTP()
    $.ajax({
      type: "POST",
      url: "/",
      data: {
        mobile: $("#mobile_register").val(),
        password: $("#newpassword").val()
      },
      success: function () {

        showOTP()
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
      url: "/",
      data: {
        mobile: $("#mobile_register").val(),
        otp: $("#otp").val()
      },
      success: function () {

        if(localStorage.getItem("mode") != null)
            location.href="/" + localStorage.getItem("mode");
      }
    });
}
