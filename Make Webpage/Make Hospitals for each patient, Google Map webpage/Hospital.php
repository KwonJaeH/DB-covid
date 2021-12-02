<?php
	require_once 'dbconfig.php';
?>

<html>
	<head>
		<title>PHP COVID</title>
	</head>

	<style>
		table {
			width : 100%;
			border : 1px solid #444444;
			border-collapse : collapse;
		}
		th,td{
			border : 1px solid #444444;
		}
	</style>

	<body>
        <h3>Hospital_id 를 입력하세요. </h3>
        <form method="get" action="./Hospital.php">
            <input type="number" name="id" value="1" min="1" max="43">
            <input type="submit" value="확인">
        </form>


        <p><h3> 
		<?php
              if(isset($_GET['id'])){
                $id = $_GET["id"];

                $sql = "select name from HOSPITAL where hospital_id = '$id'";
                $result = mysqli_query($con,$sql);
                $data = mysqli_fetch_assoc($result);
                echo $data['name']." 에 입원한 환자 ";

                $sql = "select count(*) as num from PATIENT_INFO where hospital_id = '$id'";
                $result = mysqli_query($con,$sql);
                $data = mysqli_fetch_assoc($result);
                echo $data['num']." 명";

                $sql2 = "select * from PATIENT_INFO where hospital_id = '$id'";
            }else{
                $sql = "select count(*) as cnt from PATIENT_INFO";
                $result = mysqli_query($con,$sql);
                $data = mysqli_fetch_assoc($result);
                echo "환자 ".$data['cnt']." 명 ";

                $sql2 = "select * from PATIENT_INFO";
            }
            
		?>
		</h3></p>
        
		<table class = "table table_striped">
			<tr>
				<th>Patient_ID</th>
				<th>Sex</th>
				<th>Age</th>
				<th>Country</th>
				<th>Province</th>
				<th>City</th>
				<th>Infection_case</th>
				<th>Infected_by</th>
				<th>contact_number</th>
				<th>symptom_onset_date</th>
				<th>confirmed_date</th>
				<th>released_date</th>
				<th>decreased_date</th>
				<th>state</th>
                <th>Hospital_id</th>
			</tr>
            
			<?php
				$result = mysqli_query($con,$sql2);
				while($row = mysqli_fetch_assoc($result)){
					print"<tr>";
					foreach($row as $key => $val){
                        if($key == 'Hospital_id'){
                            echo "<td> <a href=./Hospital_Map.php?hospital_id=",urlencode($val),">" . $val . "</a></td>";
                        }else{
						    print"<td>" . $val . "</td>";
                        }
					}
					print"</tr>";
				}
			?>

		</table>
	</body>

</html>