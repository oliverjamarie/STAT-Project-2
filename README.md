# STAT-Project-2

Query.py is essentially used to make general queries about the data


Read.py parses through the Excel sheet and returns a 2 dimensional dictionnary. 
To get it 
  #1  "Import Read"
  #2  "data_set = Read.Reader().get_data()"
Each entry is organised by <b>[patient-id][attribute]</b> with attribute being the name of column from the spreadsheet.
You can see the attributes from lines #37 - #45 (example : 'sex', 'sbp' ...)

Example: To print the age all the men,
  for item in data_set:
    if (data_set[item]['sex'] == 1.0):
      println(data_set[item]['age'])
      
