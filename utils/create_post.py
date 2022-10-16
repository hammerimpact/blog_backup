from datetime import date, datetime
import os

# post root directory
post_path = "posts"

# "YYYY/MM/DD/HH/MM/SS" => "YYYYMMDDHHMMSS"
nowtime = datetime.utcnow()
directory_name = nowtime.strftime("%Y%m%d%H%M%S")

# file name
file_name = "index.md"

# create directory
os.mkdir("{}/{}".format(post_path, directory_name))

# create md file
f = open("{}/{}/{}".format(post_path, directory_name, file_name), "w")
f.write("(no_title)\n\n")
f.write("(no_tag)\n\n")