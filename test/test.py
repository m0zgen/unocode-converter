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
  # for directory in directories:
  #   print os.path.join(root, directory)
  for filename in filenames:
    # print os.path.join(root,filename)
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

# for root, dirs, files in os.walk(path):
#     for file in files:
#       if file.endswith(newExtension):
#         os.remove(os.path.join(root,file))


    # for file_ in files:
    #     if file_.endswith(newExtension):
    #         shutil.copy(os.path.join(root, file_), os.path.join(convertDir, file_))



# cleanSource='find ./slack_export -name "*.convert" -exec rm -rf {} \\;'
# cleanDest='find ./slack_export -name "*.json" -exec rm -rf {} \\;'
# os.system(cleanSource)
# os.system(cleanDest)
# bash working command find . -name "*.convert" -exec rename .convert .json {} \;
#
