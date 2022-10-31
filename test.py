from urllib.request import urlretrieve
import zipfile
import json

# python training didn't have api training, json, sorting
# pip install
# cover virtual environments

# pip3 install {pkg_name} --user

# Step One - download the file
url = "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2022.json.zip"
urlretrieve(url, "nvdcve-1.1-2022.json.zip")

# Step Two - extract the json
with zipfile.ZipFile("nvdcve-1.1-2022.json.zip", 'r') as zip_ref:
  zip_ref.extractall(".")

# Step Three - import json to variable
f = open('nvdcve-1.1-2022.json')
data = json.load(f)

# Step Four - loop over json
for cve in data["CVE_Items"]:
  #if (cve[description].contains("Java") and not cve[description].contains("JavaScript") then... print
  print(cve["cve"]["CVE_data_meta"]["ID"])

# Step Five - filter by vulnerability


# Step Six - create new json object with filtered results


# Step Seven - sort new json object by criteria B


# Step Eight - sort new json object by criteria A


# Step Nine - delete original zip and json off disk

# Step Last - write json to file
with open("newAwesomeProject.json", "w") as outfile:
  json.dumps(finalJsonVariable, outfile)



