wwwlog = open("wwwlog.txt")
bytecolumn = (line.split()[-1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')
print ("Total %d" % sum(bytes))