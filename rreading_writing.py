#creating files,wroiting files
#/Users/aadi/Desktop
f = open("//Users//aadi//Desktop//data//first_writing.html","w")
f.write("<h1>Hello<h1>")
f.close()
ML = open("//Users//aadi//Desktop//data//first_writing.txt","w")
ML.write("Hey i will be best ML Engineer")
f.close()

#Reading files
reading = open("//Users//aadi//Desktop//data//first_writing.html","r")
print(reading.read())
f.close()