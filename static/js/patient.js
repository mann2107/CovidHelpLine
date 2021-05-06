function getMyRequirements()
{

    $.ajax({
      type: "GET",
      url: "/listpatientrequirements",
      success: function (result) {

       // result = "[{'requirement_summary': 'Oxygen, 1',  'location': 'Jamalpur, India', 'posted': '24.54 minutes ago', 'patient_id': 'https:\\/\\/localhost:5005/pick?req_id=WxDHNUdF9y2hyUBLeSJadT'},{'requirement_summary': 'Covid Bed, 2', 'location': 'Jamalpur, India', 'posted': '24.54 minutes ago', 'patient_id': 'https:\\/\\/localhost:5005/pick?req_id=gogmLn7CPEj2s3LH9J4G4o'}]"

        console.log(result);

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

        $("#tblMyRequirement").html(str)

      }
    });

}
