# Converter Cyrillic unicode to utf-f
# Created by Yevgeniy Goncharov, https://sys-adm.in
#

import json
import os, shutil, sys, codecs

# Custom path
# path = "/path/to/dir/slack_export"

# current foler (script destination)
path = os.getcwd() + "/slack_export"
# Json file list
files = []

# Converted files & Folders
newExtension = ".convert"
convertDir=os.getcwd() + "/converted-json"

# create directory if doesn't exist
if not os.path.exists(convertDir):
    os.mkdir(convertDir)

# Find all filest
for root, directories, filenames in os.walk(path):
  for filename in filenames:
    files.append(os.path.join(root,filename))

# Filter by json and convert to utf-8
for f in files:
  if f.endswith(".json"):
    input_j = file(f, "r")
    output_j = codecs.open(f + newExtension, "w", encoding="utf-8")
    jdata = json.loads(input_j.read().decode("utf-8-sig"))
    json.dump(jdata, output_j, indent=4, sort_keys=True, ensure_ascii=False)
    print(f)


# Move converted files to new folder
for root, dirs, files in os.walk(path):
    for dirName in dirs:
      s = os.path.join(root, dirName)
      d = os.path.join(convertDir, dirName)
      if os.path.exists(d):
        continue
        shutil.rmtree(d)
      shutil.copytree(s, d)
      print(dirName)
