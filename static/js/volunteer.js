function getGlobalRequirements()
{

    $.ajax({
      type: "GET",
      url: "/listglobalrequirements",
      success: function (result) {

        //result = result.replace(/'/g, '"');
        console.log(result);

        var str = "<tr class='bg-primary text-white '><td>Location</td><td>Patient Id</td><td>Posted</td><td>Requirement</td><td>Status</td><td>Pick</td></tr>"

        $.each(result, function(index, obj){
        str+="<tr><td>"+obj.location+
        "</td><td>"+obj.patient_id+
        "</td><td>"+obj.posted+
        "</td><td>"+obj.requirement_summary+
        "</td><td>"+obj.status+
        "</td><td><a href='"+obj.pick+
        "'>Pick</a></td></tr>"

        }
        )
        $("#tblGlobalRequirement").html(str)

      }
    });

}

function getMyHelps()
{

    $.ajax({
      type: "GET",
      url: "/listuserhelps",
      success: function (result) {

        //result = "[{'requirement_summary': 'Oxygen, 1',  'picked_at': '', 'status': 'Open', 'picked_by': ''},{'requirement_summary': 'Covid Bed, 2', 'picked_at': '', 'status': 'Open', 'picked_by': ''}]"
        //result = result.replace(/'/g, '"');
        console.log(result);
        //console.log(JSON.parse(result))
        var str = "<tr class='bg-primary text-white '><td>Location</td><td>Patient Id</td><td>Posted</td><td>Requirement</td><td>Status</td></tr>"

        $.each(result, function(index, obj){
        str+="<tr><td>"+obj.location+
        "</td><td>"+obj.patient_id+
        "</td><td>"+obj.posted+
        "</td><td>"+obj.requirement_summary+
        "</td><td>";

        $.each(obj.volunteers, function(i, vol){
            str+=vol;

            if(i<obj.volunteers.length-1)
            {
            str+=", ";
            }
        })



        str += "</td></tr>";

        }
        )


        $("#tblVolunteerHelps").html(str)

      }
    });

}
