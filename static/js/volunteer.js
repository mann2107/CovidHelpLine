function getGlobalRequirements()
{

    $.ajax({
      type: "GET",
      url: "/",
      success: function (result) {

        result = "[{'requirement_summary': 'Oxygen, 1', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'req_posted_at': '', 'status': 'Open', 'picked_by': 0, 'requirement_id': 'WxDHNUdF9y2hyUBLeSJadT', 'posted': '24.54 minutes ago', 'pick': ''}, {'requirement_summary': 'Covid Bed, 2', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'req_posted_at': '', 'status': 'Open', 'picked_by': 0, 'requirement_id': 'gogmLn7CPEj2s3LH9J4G4o', 'posted': '24.54 minutes ago', 'pick': ''}]"
        result = result.replace(/'/g, '"');
        console.log(result);
        console.log(JSON.parse(result))
        var str = "<tr class='bg-primary text-white '><td>Location</td><td>Patient Id</td><td>Posted</td><td>Requirement</td><td>Status</td><td>Pick</td></tr>"

        $.each(JSON.parse(result), function(index, obj){
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
      url: "/",
      success: function (result) {

        result = "[{'requirement_summary': 'Oxygen, 1',  'picked_at': '', 'status': 'Open', 'picked_by': ''},{'requirement_summary': 'Covid Bed, 2', 'picked_at': '', 'status': 'Open', 'picked_by': ''}]"
        result = result.replace(/'/g, '"');
        console.log(result);
        console.log(JSON.parse(result))
        var str = "<tr class='bg-primary text-white '><td>Picked At</td><td>Picked By</td><td>Requirement</td><td>Status</td></tr>"

        $.each(JSON.parse(result), function(index, obj){
            str+="<tr><td>"+obj.picked_at+
        "</td><td>"+obj.picked_by+
        "</td><td>"+obj.requirement_summary+
        "</td><td>"+obj.status+
        "</td></tr>"

        }
        )


        $("#tblVolunteerHelps").html(str)

      }
    });

}
