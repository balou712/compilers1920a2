import re

def f_callback(m):
	if m.group(0) == '&amp;':
		return '&'
	elif m.group(0) == '&gt;':
		return '>'
	elif m.group(0) == '&lt;':
		return '<'
	elif m.group(0) == '&nbsp;':
		return ' '

   

with open('testpage.txt','r',encoding='utf-8') as fp:
	text = fp.read()
        	
	rexp = re.compile('<title>(.+?)</title>')  #Εξαγωγή και εκτύπωση του τίτλου (οτιδήποτε βρίσκεται μεταξύ <title> και </title>)
	rexp2 = re.compile('<!--.*?-->',re.DOTALL)  #Απαλοιφή των σχολίων (οτιδήποτε βρίσκεται μεταξύ <!-- και -->)
	rexp3 = re.compile('<script(.*?)</script?|style=(.*?)')    #Απαλοιφή των <script> και <style> tags με όλο τους το περιεχόμενο
	rexp4 = re.compile('<a(.+?)</a>')  #Εξαγωγή και εκτύπωση του συνδέσμου (ιδιότητα href) από <a> tags και του κειμένου τους
	rexp5 = re.compile('<.+?>(.*?)</.+?>',re.DOTALL)  #Απαλοιφή όλων των tags από το κείμενο
	rexp6 = re.compile('(&amp|&gt|&lt|&nbsp);')   #Μετατροπή των ειδικών HTML entities που υπάρχουν στο κείμενο
	rexp7 = re.compile('\s+')   #Μετατροπή ακολουθιών συνεχόμενων χαρακτήρων whitespace σε ένα ακριβώς κενό

	print(re.findall(rexp,text))
        
	text=rexp2.sub(' ',text)
	text = rexp3.sub(" ",text)
 
	for m2 in rexp4.finditer(text):
		print(m2.group(1))

	text = rexp5.sub(' ',text)
	text = rexp6.sub(f_callback,text)
	text = rexp7.sub(' ',text)	

	print(text)
