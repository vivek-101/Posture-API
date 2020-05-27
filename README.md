# Posture-API
This API highly emphases over dynamic scraping, plotting data and  bring out valuable insights. It gives the BMI, BMI_category, Posture analysis based on data collected through IoT device, recommend 3 exercise based on issues faced by user and create a Health Report.<br>

The input for this api will be structured as <br><br>

{<br>
  "hours": 8,<br>
	"issue":"digestion",<br>
	"height":1.63,<br>
	"weight":44.4<br>
}

and in response user will get<br><br>

{<br>
  "bmi": float,<br>
  "category": "string" --Underweight,healthy weight, overweight, Obese(1,2,3)<br>
  "excercise1": "name","image_link",[list of benefits],<br>
  "excercise2": "name","image_link",[list of benefits],<br>
  "excercise3": "name","image_link",[list of benefits],<br>
  "line graph": Base64 encoded png of daily sitting posture,<br>
  "pie chart": daily percentage of sitting (good/bad Posture),<br>
  "posture": Overall posture of User
}
