#COVID-19 JHU.EDU CSSE Data Analytics
#v0.44 2020-03-15 3:44:46 PM
#Written by VTSTech (veritas@vts-tech.org)
#John Hopkins University CSSE Data
#
#git clone https://github.com/CSSEGISandData/COVID-19
#cd COVID-19
#wget https://gist.github.com/Veritas83/1f3b64135c3b565b9c5cebea926705ba/raw/bb0a002fcadd7889cdcd8f91c9c6aebe3d576875/VTSTech-COVID19.py

import os, sys, csv
from os import listdir
from os.path import isfile, join
from pathlib import Path

data_folder = Path("C:\\COVID\\data\\")

print (data_folder)

files = [f for f in listdir(data_folder) if isfile(join(data_folder, f))]
verbose=0
mode=""
report=""
cc="" #ISO 3166-1 Alpha-2
calc=""

def getcc(cc):
	if (cc.lower() == "af"):return "Afghanistan"
	elif (cc.lower() == "ax"):return "Aland"
	elif (cc.lower() == "al"):return "Albania"
	elif (cc.lower() == "dz"):return "Algeria"
	elif (cc.lower() == "as"):return "American Samoa"  
	elif (cc.lower() == "ad"):return "Andorra"
	elif (cc.lower() == "ao"):return "Angola" 
	elif (cc.lower() == "ai"):return "Anguilla"  
	elif (cc.lower() == "aq"):return "Antarctica"
	elif (cc.lower() == "ag"):return "Antigua and Barbuda"
	elif (cc.lower() == "ar"):return "Argentina" 
	elif (cc.lower() == "am"):return "Armenia"
	elif (cc.lower() == "aw"):return "Aruba"  
	elif (cc.lower() == "au"):return "Australia" 
	elif (cc.lower() == "at"):return "Austria"
	elif (cc.lower() == "az"):return "Azerbaijan"
	elif (cc.lower() == "bs"):return "Bahamas"
	elif (cc.lower() == "bh"):return "Bahrain"
	elif (cc.lower() == "bd"):return "Bangladesh"
	elif (cc.lower() == "bb"):return "Barbados"  
	elif (cc.lower() == "by"):return "Belarus"
	elif (cc.lower() == "be"):return "Belgium"
	elif (cc.lower() == "bz"):return "Belize" 
	elif (cc.lower() == "bj"):return "Benin"  
	elif (cc.lower() == "bm"):return "Bermuda"
	elif (cc.lower() == "bt"):return "Bhutan" 
	elif (cc.lower() == "bo"):return "Bolivia"  
	elif (cc.lower() == "bq"):return "Bonaire, Sint Eustatius and Saba"  
	elif (cc.lower() == "ba"):return "Bosnia and Herzegovina"
	elif (cc.lower() == "bw"):return "Botswana"  
	elif (cc.lower() == "bv"):return "Bouvet Island"
	elif (cc.lower() == "br"):return "Brazil" 
	elif (cc.lower() == "io"):return "British Indian Ocean Territory" 
	elif (cc.lower() == "bn"):return "Brunei Darussalam"  
	elif (cc.lower() == "bg"):return "Bulgaria"  
	elif (cc.lower() == "bf"):return "Burkina Faso" 
	elif (cc.lower() == "bi"):return "Burundi"
	elif (cc.lower() == "kh"):return "Cambodia"  
	elif (cc.lower() == "cm"):return "Cameroon"  
	elif (cc.lower() == "ca"):return "Canada" 
	elif (cc.lower() == "cv"):return "Cabo Verde"
	elif (cc.lower() == "ky"):return "Cayman Islands"  
	elif (cc.lower() == "cf"):return "Central African Republic" 
	elif (cc.lower() == "td"):return "Chad"
	elif (cc.lower() == "cl"):return "Chile"  
	elif (cc.lower() == "cn"):return "China"  
	elif (cc.lower() == "cx"):return "Christmas Island"
	elif (cc.lower() == "cc"):return "Cocos (Keeling) Islands"  
	elif (cc.lower() == "co"):return "Colombia"  
	elif (cc.lower() == "cs"):return "Cruise Ship"
	elif (cc.lower() == "km"):return "Comoros"
	elif (cc.lower() == "cg"):return "Congo (Kinshasa)"  
	elif (cc.lower() == "cd"):return "Congo (Democratic Republic of the)"
	elif (cc.lower() == "ck"):return "Cook Islands" 
	elif (cc.lower() == "cr"):return "Costa Rica"
	elif (cc.lower() == "ci"):return "Cote d'Ivoire"
	elif (cc.lower() == "hr"):return "Croatia"
	elif (cc.lower() == "cu"):return "Cuba"
	elif (cc.lower() == "cw"):return "Curacao"
	elif (cc.lower() == "cy"):return "Cyprus" 
	elif (cc.lower() == "cz"):return "Czech Republic"  
	elif (cc.lower() == "dk"):return "Denmark"
	elif (cc.lower() == "dj"):return "Djibouti"  
	elif (cc.lower() == "dm"):return "Dominica"  
	elif (cc.lower() == "do"):return "Dominican Republic" 
	elif (cc.lower() == "ec"):return "Ecuador"
	elif (cc.lower() == "eg"):return "Egypt"  
	elif (cc.lower() == "sv"):return "El Salvador"  
	elif (cc.lower() == "gq"):return "Equatorial Guinea"  
	elif (cc.lower() == "er"):return "Eritrea"
	elif (cc.lower() == "ee"):return "Estonia"
	elif (cc.lower() == "et"):return "Ethiopia"  
	elif (cc.lower() == "fk"):return "Falkland Islands (Malvinas)" 
	elif (cc.lower() == "fo"):return "Faroe Islands"
	elif (cc.lower() == "fj"):return "Fiji"
	elif (cc.lower() == "fi"):return "Finland"
	elif (cc.lower() == "fr"):return "France" 
	elif (cc.lower() == "gf"):return "French Guiana"
	elif (cc.lower() == "pf"):return "French Polynesia"
	elif (cc.lower() == "tf"):return "French Southern Territories" 
	elif (cc.lower() == "ga"):return "Gabon"  
	elif (cc.lower() == "gm"):return "Gambia" 
	elif (cc.lower() == "ge"):return "Georgia"
	elif (cc.lower() == "de"):return "Germany"
	elif (cc.lower() == "gh"):return "Ghana"  
	elif (cc.lower() == "gi"):return "Gibraltar" 
	elif (cc.lower() == "gr"):return "Greece" 
	elif (cc.lower() == "gl"):return "Greenland" 
	elif (cc.lower() == "gd"):return "Grenada"
	elif (cc.lower() == "gp"):return "Guadeloupe"
	elif (cc.lower() == "gu"):return "Guam"
	elif (cc.lower() == "gt"):return "Guatemala" 
	elif (cc.lower() == "gg"):return "Guernsey"  
	elif (cc.lower() == "gn"):return "Guinea" 
	elif (cc.lower() == "gw"):return "Guinea-Bissau"
	elif (cc.lower() == "gy"):return "Guyana" 
	elif (cc.lower() == "ht"):return "Haiti"  
	elif (cc.lower() == "hm"):return "Heard Island and McDonald Islands" 
	elif (cc.lower() == "va"):return "Holy See"  
	elif (cc.lower() == "hn"):return "Honduras"  
	elif (cc.lower() == "hk"):return "Hong Kong" 
	elif (cc.lower() == "hu"):return "Hungary"
	elif (cc.lower() == "is"):return "Iceland"
	elif (cc.lower() == "in"):return "India"  
	elif (cc.lower() == "id"):return "Indonesia" 
	elif (cc.lower() == "ir"):return "Iran"  
	elif (cc.lower() == "iq"):return "Iraq"
	elif (cc.lower() == "ie"):return "Ireland"
	elif (cc.lower() == "im"):return "Isle of Man"  
	elif (cc.lower() == "il"):return "Israel" 
	elif (cc.lower() == "it"):return "Italy"  
	elif (cc.lower() == "jm"):return "Jamaica"
	elif (cc.lower() == "jp"):return "Japan"  
	elif (cc.lower() == "je"):return "Jersey" 
	elif (cc.lower() == "jo"):return "Jordan" 
	elif (cc.lower() == "kz"):return "Kazakhstan"
	elif (cc.lower() == "ke"):return "Kenya"  
	elif (cc.lower() == "ki"):return "Kiribati"  
	elif (cc.lower() == "kp"):return "North Korea" 
	elif (cc.lower() == "kr"):return "South Korea"
	elif (cc.lower() == "kw"):return "Kuwait" 
	elif (cc.lower() == "kg"):return "Kyrgyzstan"
	elif (cc.lower() == "la"):return "Lao People's Democratic Republic"  
	elif (cc.lower() == "lv"):return "Latvia" 
	elif (cc.lower() == "lb"):return "Lebanon"
	elif (cc.lower() == "ls"):return "Lesotho"
	elif (cc.lower() == "lr"):return "Liberia"
	elif (cc.lower() == "ly"):return "Libya"  
	elif (cc.lower() == "li"):return "Liechtenstein"
	elif (cc.lower() == "lt"):return "Lithuania" 
	elif (cc.lower() == "lu"):return "Luxembourg"
	elif (cc.lower() == "mo"):return "Macao"  
	elif (cc.lower() == "mk"):return "North Macedonia"
	elif (cc.lower() == "mg"):return "Madagascar"
	elif (cc.lower() == "mw"):return "Malawi" 
	elif (cc.lower() == "my"):return "Malaysia"  
	elif (cc.lower() == "mv"):return "Maldives"  
	elif (cc.lower() == "ml"):return "Mali"
	elif (cc.lower() == "mt"):return "Malta"  
	elif (cc.lower() == "mh"):return "Marshall Islands"
	elif (cc.lower() == "mq"):return "Martinique"
	elif (cc.lower() == "mr"):return "Mauritania"
	elif (cc.lower() == "mu"):return "Mauritius" 
	elif (cc.lower() == "yt"):return "Mayotte"
	elif (cc.lower() == "mx"):return "Mexico" 
	elif (cc.lower() == "fm"):return "Micronesia"  
	elif (cc.lower() == "md"):return "Moldova" 
	elif (cc.lower() == "mc"):return "Monaco" 
	elif (cc.lower() == "mn"):return "Mongolia"  
	elif (cc.lower() == "me"):return "Montenegro"
	elif (cc.lower() == "ms"):return "Montserrat"
	elif (cc.lower() == "ma"):return "Morocco"
	elif (cc.lower() == "mz"):return "Mozambique"
	elif (cc.lower() == "mm"):return "Myanmar"
	elif (cc.lower() == "na"):return "Namibia"
	elif (cc.lower() == "nr"):return "Nauru"  
	elif (cc.lower() == "np"):return "Nepal"  
	elif (cc.lower() == "nl"):return "Netherlands"  
	elif (cc.lower() == "nc"):return "New Caledonia"
	elif (cc.lower() == "nz"):return "New Zealand"  
	elif (cc.lower() == "ni"):return "Nicaragua" 
	elif (cc.lower() == "ne"):return "Niger"  
	elif (cc.lower() == "ng"):return "Nigeria"
	elif (cc.lower() == "nu"):return "Niue"
	elif (cc.lower() == "nf"):return "Norfolk Island"  
	elif (cc.lower() == "mp"):return "Northern Mariana Islands" 
	elif (cc.lower() == "no"):return "Norway" 
	elif (cc.lower() == "om"):return "Oman"
	elif (cc.lower() == "pk"):return "Pakistan"  
	elif (cc.lower() == "pw"):return "Palau"  
	elif (cc.lower() == "ps"):return "occupied Palestinian territory"
	elif (cc.lower() == "pa"):return "Panama" 
	elif (cc.lower() == "pg"):return "Papua New Guinea"
	elif (cc.lower() == "py"):return "Paraguay"  
	elif (cc.lower() == "pe"):return "Peru"
	elif (cc.lower() == "ph"):return "Philippines"  
	elif (cc.lower() == "pn"):return "Pitcairn"  
	elif (cc.lower() == "pl"):return "Poland" 
	elif (cc.lower() == "pt"):return "Portugal"  
	elif (cc.lower() == "pr"):return "Puerto Rico"  
	elif (cc.lower() == "qa"):return "Qatar"  
	elif (cc.lower() == "re"):return "Reunion"
	elif (cc.lower() == "ro"):return "Romania"
	elif (cc.lower() == "ru"):return "Russian Federation" 
	elif (cc.lower() == "rw"):return "Rwanda" 
	elif (cc.lower() == "bl"):return "Saint Barthelemy"
	elif (cc.lower() == "sh"):return "Saint Helena, Ascension and Tristan da Cunha"  
	elif (cc.lower() == "kn"):return "Saint Kitts and Nevis" 
	elif (cc.lower() == "lc"):return "Saint Lucia"  
	elif (cc.lower() == "mf"):return "Saint Martin (French part)"  
	elif (cc.lower() == "pm"):return "Saint Pierre and Miquelon"
	elif (cc.lower() == "vc"):return "Saint Vincent and the Grenadines"  
	elif (cc.lower() == "ws"):return "Samoa"  
	elif (cc.lower() == "sm"):return "San Marino"
	elif (cc.lower() == "st"):return "Sao Tome and Principe" 
	elif (cc.lower() == "sa"):return "Saudi Arabia" 
	elif (cc.lower() == "sn"):return "Senegal"
	elif (cc.lower() == "rs"):return "Serbia" 
	elif (cc.lower() == "sc"):return "Seychelles"
	elif (cc.lower() == "sl"):return "Sierra Leone" 
	elif (cc.lower() == "sg"):return "Singapore" 
	elif (cc.lower() == "sx"):return "Sint Maarten (Dutch part)"
	elif (cc.lower() == "sk"):return "Slovakia"  
	elif (cc.lower() == "si"):return "Slovenia"  
	elif (cc.lower() == "sb"):return "Solomon Islands" 
	elif (cc.lower() == "so"):return "Somalia"
	elif (cc.lower() == "za"):return "South Africa" 
	elif (cc.lower() == "gs"):return "South Georgia and the South Sandwich Islands"  
	elif (cc.lower() == "ss"):return "South Sudan"  
	elif (cc.lower() == "es"):return "Spain"  
	elif (cc.lower() == "lk"):return "Sri Lanka" 
	elif (cc.lower() == "sd"):return "Sudan"  
	elif (cc.lower() == "sr"):return "Suriname"  
	elif (cc.lower() == "sj"):return "Svalbard and Jan Mayen"
	elif (cc.lower() == "sz"):return "Swaziland" 
	elif (cc.lower() == "se"):return "Sweden" 
	elif (cc.lower() == "ch"):return "Switzerland"  
	elif (cc.lower() == "sy"):return "Syrian Arab Republic"  
	elif (cc.lower() == "tw"):return "Taiwan, Province of China"
	elif (cc.lower() == "tj"):return "Tajikistan"
	elif (cc.lower() == "tz"):return "Tanzania, United Republic of"
	elif (cc.lower() == "th"):return "Thailand"  
	elif (cc.lower() == "tl"):return "Timor-Leste"  
	elif (cc.lower() == "tg"):return "Togo"
	elif (cc.lower() == "tk"):return "Tokelau"
	elif (cc.lower() == "to"):return "Tonga"  
	elif (cc.lower() == "tt"):return "Trinidad and Tobago"
	elif (cc.lower() == "tn"):return "Tunisia"
	elif (cc.lower() == "tr"):return "Turkey" 
	elif (cc.lower() == "tm"):return "Turkmenistan" 
	elif (cc.lower() == "tc"):return "Turks and Caicos Islands" 
	elif (cc.lower() == "tv"):return "Tuvalu" 
	elif (cc.lower() == "ug"):return "Uganda" 
	elif (cc.lower() == "ua"):return "Ukraine"
	elif (cc.lower() == "ae"):return "United Arab Emirates"  
	elif (cc.lower() == "gb"):return "United Kingdom"
	elif (cc.lower() == "us"):return "US" 
	elif (cc.lower() == "um"):return "United States Minor Outlying Islands" 
	elif (cc.lower() == "uy"):return "Uruguay"
	elif (cc.lower() == "uz"):return "Uzbekistan"
	elif (cc.lower() == "vu"):return "Vanuatu"
	elif (cc.lower() == "ve"):return "Venezuela (Bolivarian Republic of)"
	elif (cc.lower() == "vn"):return "Viet Nam"  
	elif (cc.lower() == "vg"):return "Virgin Islands (British)" 
	elif (cc.lower() == "vi"):return "Virgin Islands (U.S.)" 
	elif (cc.lower() == "wf"):return "Wallis and Futuna"  
	elif (cc.lower() == "eh"):return "Western Sahara"  
	elif (cc.lower() == "ye"):return "Yemen"  
	elif (cc.lower() == "zm"):return "Zambia" 
	elif (cc.lower() == "zw"):return "Zimbabwe"  
def getfn(msg):
	script_fn = msg.split("\\")
	for x in range(0,len(script_fn),1):
		if ("VTSTech-COVID19.py" in script_fn[x]):
			return script_fn[x]
		elif (".py" in script_fn[x]):
			return script_fn[x]
def banner():	
	print("COVID-19 JHU.EDU CSSE Data Analytics\nv0.44 Written by VTSTech (www.VTS-Tech.org)\nData Source: https://github.com/CSSEGISandData/COVID-19\n")
def usage():
	spc=" "
	print("Usage:",getfn(sys.argv[0]),"-l")
	print(spc*6,getfn(sys.argv[0]),"-d 03-14-2020")
	print(spc*6,getfn(sys.argv[0]),"-a -dav\n")
	print("-v",spc*17,"verbose mode\n-l",spc*17,"list daily reports available\n-d MM-DD-YYYY",spc*6,"use this daily report\n-a",spc*18,end='')
	print("use all available reports\n-c",spc*17,"filter by this country (ISO 3166-1 Alpha-2)\n-t",spc*17,"calculate total cases\n-td",end='')
	print(spc*17,"calculate total deaths\n-gdr",spc*15,"calculate global death rate (use with -c for national)\n-dav",spc*15,"calculate daily average new cases\n-dad",end='')
	print(spc*16,"calculate daily average new deaths\n-dnc",spc*15,"calculate daily new cases\n-dnd",spc*15,"calculate daily new deaths\n-dgf",spc*16,end='')
	print("calculate daily growth factor\n-din",spc*15,"find largest daily case increases")
def getreports():
	reports=""
	for x in range(0,len(files),1):
		if (".csv" in files[x]):
			reports=reports+"\n"+files[x]	
	return reports
def listreports():
	print("Daily Reports Available:\n")
	print(getreports())
def parsereports(calc):
	global mode
	global cc
	reports=getreports()
	i=0
	#print("DEBUG:", mode)
	if ("allreports" in mode):
		if (calc=="t") or (calc=="td") or (calc=="gdr"):
			for line in reports.split(".csv"):
				line=line+".csv"
				if (len(line)>4):
					tmp = parsereport(line.replace("\n",""),calc)
					if (tmp != 0 and tmp != None or verbose==1):print(tmp)
			if (calc=="t"):
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
				print("\nTotal Cases")
			elif (calc=="td"):
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
				print("\nTotal Deaths")
			elif (calc=="gdr"):
				if (len(cc)>=1):
					print("\nNational Death Rate")
					print("\nCountry Filter:", getcc(cc))
				else:
					print("\nGlobal Death Rate")
			print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.44 by VTSTech Complete.")
		elif (calc=="dav")or(calc=="dad")or(calc=="din")or(calc=="dnc")or(calc=="dgf")or(calc=="dnd"):
			if (calc=="dav"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				davg_cases=0
				for line in reports.split(".csv"):
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						new_cases=(c_cases - p_cases)
						#print(new_cases)
						davg_cases = (davg_cases+new_cases)/i
					t_days=i				
				if (len(cc)>=1):
					print("National Average Daily New Cases:",round(davg_cases,2))
					print("\nCountry Filter:", getcc(cc))
				else:
					print("Global Average Daily New Cases:",round(davg_cases,2))
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.44 by VTSTech Complete.")
			elif (calc=="dad"):
				p_deaths = 0
				c_deaths = 0
				n_deaths = []
				davg_deaths=0
				for line in reports.split(".csv"):
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_deaths = c_deaths
						c_deaths = parsereport(line.replace("\n",""),"td")
						new_deaths=(c_deaths - p_deaths)
						#print(new_deaths)
						davg_deaths = (davg_deaths+new_deaths)/i
					t_days=i
				if (len(cc)>=1):
					print("National Average Daily New Deaths:",round(davg_deaths,2))
					print("\nCountry Filter:", getcc(cc))
				else:
					print("Global Average Daily New Deaths:",round(davg_deaths,2))
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.44 by VTSTech Complete.")
			elif (calc=="dnc"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				davg_cases=0
				print("Daily New Cases:\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						#c_date = parsereport(line.replace("\n",""),"date")
						new_cases=(c_cases - p_cases)
						if (new_cases != 0 or verbose==1):print(c_date+" "+str(new_cases),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nCountry Filter:", getcc(cc))
					print("\nNational Daily New Cases")
				else:
					print("\n\nGlobal Daily New Cases\n")
				print("COVID-19 JHU.EDU CSSE Data Analytics v0.44 by VTSTech Complete.")
			elif (calc=="dnd"):
				p_deaths = 0
				c_deaths = 0
				n_deaths = []
				davg_deaths=0
				print("Daily New Deaths\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_deaths = c_deaths
						c_deaths = parsereport(line.replace("\n",""),"td")
						#c_date = parsereport(line.replace("\n",""),"date")
						new_deaths=(c_deaths - p_deaths)
						print(c_date+" "+str(new_deaths),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nCountry Filter:", getcc(cc))
					print("\nNational Daily New Deaths")
				else:
					print("\n\nGlobal Daily New Deaths\n")
				print("COVID-19 JHU.EDU CSSE Data Analytics v0.44 by VTSTech Complete.")
			elif (calc=="din"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				top_cases=0
				print("Largest Daily New Cases\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						#c_date = parsereport(line.replace("\n",""),"date")
						new_cases=(c_cases - p_cases)
						if (new_cases > top_cases) or (new_cases > 500):
							top_cases=new_cases
							print(c_date+" "+str(top_cases),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
				print("\n\nLargest Daily New Cases\nCOVID-19 JHU.EDU CSSE Data Analytics v0.44 by VTSTech Complete.")
			elif (calc=="dgf"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				davg_cases=0
				c_growth=0
				t_days=0
				print("Daily Growth Factor\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")					
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						#c_date = parsereport(line.replace("\n",""),"date")
						if (p_cases>0):c_growth=round((c_cases / p_cases),2)
						if (c_date=="") or (c_growth==0):
							t_days=t_days-1
						else:
							print(c_date+" "+str(c_growth),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nNational Daily Growth Factor")
					print("Country Filter:", getcc(cc))
				else:
					print("\n\nGlobal Daily Growth Factor")
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.44 by VTSTech Complete.")
	else:
		print("Error! This mode requires the -a parameter!")
def parsereport(report,calc):
	global mode
	global cc
	c_country=""
	c_prov=""
	c_cases=""
	c_deaths=""
	c_recov=""
	c_updated=""
	t_cases=0
	t_deaths=0
	gdr=0.0
	file_to_open = Path("C:\\COVID\\data\\" + report)
	if file_to_open.exists():
		f = open(file_to_open.absolute())
		cssereader = csv.reader(f, delimiter=',', quotechar='"')
		x=0
		for row in cssereader:
			if (x!=0):
				if (len(cc)>=1):
					if (getcc(cc) in row[1]):
						c_prov=row[0]
						c_country=row[1]
						c_updated=row[2]
						if (len(row[3])>0):
							c_cases=int(row[3])
							t_cases=int(t_cases+c_cases)
						if (len(row[4])>0):
							c_deaths=int(row[4])
							t_deaths=int(t_deaths+c_deaths)
						c_recov=row[5]
				else:
						c_prov=row[0]
						c_country=row[1]
						c_updated=row[2]
						if (len(row[3])>0):
							c_cases=int(row[3])
							t_cases=int(t_cases+c_cases)
						if (len(row[4])>0):
							c_deaths=int(row[4])
							t_deaths=int(t_deaths+c_deaths)
						c_recov=row[5]					
			x=x+1
		if (calc==""):
			print("Please select a metric to calculate: t, td, din, dav, dad, gdr")
		elif (calc=="t"):
			if (mode=="onereport"):print("Total Cases:",t_cases)
			return(t_cases)
		elif (calc=="td"):
			if (mode=="onereport"):print("Total Deaths:",t_deaths)
			return(t_deaths)
		elif (calc=="gdr"):
			if (t_deaths!=0) and (t_cases!=0):
				gdr=round(float(t_deaths/t_cases)*100,3)
				if (mode=="onereport"):print("Global Death Rate:",gdr,"%")
				#return(str(c_updated+" "+str(gdr)+"%"))
				c_date=str(report.split(".csv")[0])
				return(c_date+" "+str(gdr)+"%")
		elif (calc=="date"):
			return(str(row[2]))
		else:
			print ("Nothing for that calc")
		f.close()
	else:
		print("Error! Requsted file does not exist.")
	#print(report)
	
def main(mode,report,cc,calc):
	global totalargs
	if (mode == "listreports"):
		banner()
		listreports()
	elif(mode == "onereport"):
		banner()
		if (len(cc) >= 1):
			print("Country Filter:",getcc(cc))
		else:
			print("Country Filter: Global")
		print("Report:",report,"\n")
		parsereport(report,calc)
	elif(mode == "allreports"):
		banner()
		parsereports(calc)
	else:
		if (totalargs>=2):
			print("Requires either -l, -a or -d to be set")
###
totalargs = len(sys.argv)
for x in range(0,totalargs,1):
	if (totalargs >= 7):	
		banner()
		print("Too many arguments! Check command line.")
		usage()
		quit()
	elif (sys.argv[x] == "-v") or (totalargs==1 and "VTSTech-COVID19.py" in getfn(sys.argv[0])):
		verbose=1
		banner()
		usage()
	elif (sys.argv[x] == "-l"):
		mode="listreports"
	elif (sys.argv[x] == "-a"):
		mode="allreports"
	elif (sys.argv[x] == "-d"):
		mode="onereport"
		report=str(sys.argv[x+1]+".csv")
	elif (sys.argv[x] == "-t"):
		calc="t"
	elif (sys.argv[x] == "-td"):
		calc="td"
	elif (sys.argv[x] == "-gdr"):
		calc="gdr"
	elif (sys.argv[x] == "-dav"):
		calc="dav"
	elif (sys.argv[x] == "-dad"):
		calc="dad"
	elif (sys.argv[x] == "-din"):
		calc="din"
	elif (sys.argv[x] == "-dnc"):
		calc="dnc"
	elif (sys.argv[x] == "-dnd"):
		calc="dnd"
	elif (sys.argv[x] == "-dgf"):
		calc="dgf"
	elif (sys.argv[x] == "-c"):
		cc=sys.argv[x+1]
main(mode,report,cc,calc)
