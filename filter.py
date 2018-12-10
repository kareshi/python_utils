def downloadFinder(file):
    for line in file:
        if "Downloaded: http://ci-external" in line and "murex" in line:
             yield line

source = open('consoleText.txt','r')

def notInPrimary(file):
    for line in file:
        if not "Simple POM generated" in line and not "POM copied from JAR" in line:
             yield line


result = downloadFinder(source)

for line in result:
	print(line)