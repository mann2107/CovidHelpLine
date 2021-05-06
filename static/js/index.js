function redirectToRequirement()
{
    localStorage.setItem("mode", "requirement")
    if(false)//loggedin
        location.href="/requirement";
    else
    {
        location.href="/login";
    }

}

function redirectToVolunteer()
{
    localStorage.setItem("mode", "volunteer")
    if(true)//loggedin
        location.href="/volunteer";
    else
    {
        location.href="/login";
    }
}