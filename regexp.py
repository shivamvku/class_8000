data = '''[11:00 PM, 8/13/2018] +91 80084 10482: sonamthapa.dl@gmail.com
[11:19 PM, 8/13/2018] +1 (647) 877-5143: madhusrichandu@gmail.com
[11:23 PM, 8/13/2018] +971 58 973 2576: kanagalasravya@yahoo.com
[11:24 PM, 8/13/2018] +91 80198 64264: bachimanchiajay@gmail.com
[11:24 PM, 8/13/2018] +91 96001 09750: avinash1097.dl@gmail.com
[11:24 PM, 8/13/2018] +91 95022 93612: surendra.funny@gmail.com
[11:24 PM, 8/13/2018] +91 96520 21971: poojadncla2514@gmail.com
[11:25 PM, 8/13/2018] +91 99851 91436: nanda.pvnk@gmail.com
[11:25 PM, 8/13/2018] +91 96001 09750: Sir has arranged interview for python completed students this Saturday....
[11:25 PM, 8/13/2018] +91 96001 09750: So
[11:25 PM, 8/13/2018] +91 96001 09750: Be prepared for that
[11:41 PM, 8/13/2018] +91 81253 64265: surya.irukulla@gmail.com
[12:04 AM, 8/14/2018] +91 99511 58249: pavan24.dl@gmail.com
[12:14 AM, 8/14/2018] +91 75699 61518: saikiranreddy.dl@gmail.com
[6:21 AM, 8/14/2018] +91 97009 37058: satishparida111@gmail.com
[6:48 AM, 8/14/2018] +91 80193 96040: sharan.santosh.ss@gmail.com
[6:58 AM, 8/14/2018] +91 96667 55505: vineethchinthala0505@gmail.com
[7:02 AM, 8/14/2018] +91 90528 51769: avinash34.dl@gmail.com
suresh9406@gmail.com'''
import re
obj = re.compile(r'[\w\.]+@[\w\.]+')
mathc = obj.finditer(data)
# print(mathc)
# next(mathc)
for match in mathc:
        print(match)