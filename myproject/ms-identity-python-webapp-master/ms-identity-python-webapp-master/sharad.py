import boto3

def ec2( name, r):
 

  EC2_RESOURCE = boto3.resource('ec2', region_name=r)
  instances = EC2_RESOURCE.instances.all()
  a = None
  b = None
  c = None
  tr = ''

  for instance in instances:
          if instance.tags == None:
            a = "none"
            b = "none"
            c = "none"
            d = instance.id
            e = instance.state["Name"]
            f = instance.instance_type
            #fun(a,b,c,d,e,f)
            tr += "<tr><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td></tr>".format( b, a, c, d, e, f)
          else:
             for tag in instance.tags:
                 if tag['Key'] == 'owner':
                   a = tag['Value']
                 if tag['Key'] == 'Name':
                   b = tag['Value']
                 if tag['Key'] == 'Project_name':
                   c = tag['Value']
             d = instance.id
             e = instance.state["Name"]
             f = instance.instance_type
             #fun(a,b,c,d,e,f)
             tr += "<tr><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td><td valign='top'>{}</td></tr>".format( b, a, c, d, e, f )

  body = '<body>'
  header = '<h1 align="center">AWS EC2 </h1>'
  table = '<table border=1 align="center" id="myTable"><tr><th>InstanceName</th><th>OwnerName</th><th>ProjectName</th><th>InstanceId</th><th>InstanceState</th><th>InstanceType</th></tr>'
  end = "</table>"
  search='<center><input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for Instance names.."></center><br>'
  back ='<center><input type="button" value="Go back!" onclick="history.back()"></center>'
  abc = '<form action="/bill.html" method="post" ><div><center><button>Billing</button></center></center></div></form>'
  bcd = ' <script>function myFunction() {var input, filter, table, tr, td, i, txtValue;input = document.getElementById("myInput");filter = input.value.toUpperCase();table = document.getElementById("myTable");tr = table.getElementsByTagName("tr");for (i = 0; i < tr.length; i++) {td = tr[i].getElementsByTagName("td")[0];if (td) {txtValue = td.textContent || td.innerText;if (txtValue.toUpperCase().indexOf(filter) > -1) {tr[i].style.display = "";} else {tr[i].style.display = "none";}}}}</script>'
  Func = open("./templates/table.html","w")
  Func.write(header+body+search+table+tr+end+back+abc+bcd)
  Func.close()
