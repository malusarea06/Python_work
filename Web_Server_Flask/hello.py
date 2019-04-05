from flask import Flask,jsonify,request


app = Flask(__name__)

#list of employee details
empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]


@app.route("/")
def hello():
	return "Hello World"


@app.route("/empDB/employes",methods=['GET'])
def getAllEmploye():
	return jsonify({'emps':empDB})	


@app.route("/empDB/employes/<empId>",methods=['GET'])
def getEmployeById(empId):
	usr = [emp for emp in empDB if (emp['id'] == empId)]
	return jsonify({'emp':usr})



@app.route("/empDB/employes/<empId>",methods=['PUT'])
def updateEmp(empId): 
	em = [emp for emp in empDB if(emp['id'] == empId)]
	if 'name' in request.json:
		em[0]['name'] = request.json['name']
	if 'title' in request.json:
		em[0]['title'] = request.json['title']
	return jsonify({'emp':em[0]})


@app.route('/empDB/employes',methods=['POST'])
def createEmp():
	dat = {'id':request.json['id']}

if __name__ == "__main__":
	app.run()



