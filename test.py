import subprocess
inventory_solr_url = "https://30800gc-stage2.cimm2.com/solr"
file_name = '202408-2100-1526_data.csv'
 
cmd = ["java",fr"-Durl={inventory_solr_url}","-Dtype=text/csv","-Dfiletypes=text/csv", "-jar", "post.jar",fr"{file_name}"]
proc = subprocess.run(cmd, capture_output=True, encoding="utf8")
eventid = '202408-2100-1526'
print("stdout: ", proc.stdout.rstrip())
print("stderr: ", proc.stderr.rstrip())
print("returncode: ", proc.returncode)
print("Publish to Solr Complete")
print("Delete old Document")
cmd = ["java",fr"-Durl={inventory_solr_url}","-Ddata=args","-Dcommit=yes", "-jar", "post.jar",f"<delete><query>-codeId:{eventid}</query></delete>"]
print(cmd)
proc = subprocess.run(cmd, capture_output=True, encoding="utf8")
print("stdout: ", proc.stdout.rstrip())
print("stderr: ", proc.stderr.rstrip())
print("returncode: ", proc.returncode)
print("Delete old Document Complete")
print("Delete zero QTy")
cmd = ["java",fr"-Durl={inventory_solr_url}","-Ddata=args","-Dcommit=yes", "-jar", "post.jar","<delete><query>qtyOnHand:0</query></delete>"]
proc = subprocess.run(cmd, capture_output=True, encoding="utf8")
print("stdout: ", proc.stdout.rstrip())
print("stderr: ", proc.stderr.rstrip())
print("returncode: ", proc.returncode)
print("Delete zero Complete")
print("Process Complete")
print("Update Last Updated Date")