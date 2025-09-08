cve = "cpe:2.3:a:phoenixcontact-software:multiprog:5.0:*:*:*:*:*:*:*"

cve = cve.split(":") 
part = cve[2]
vendor = cve[3]
product = cve[4]
version = cve[5]
print(part, vendor, product, version)