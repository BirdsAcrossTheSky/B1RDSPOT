Importing data requires having python installed on your device. 
Also before running script you need to download python packages included in requirements.txt file.
To do so run the command:
	*pip install -r requirements*
In order to tun python script use command :
	*python <scriptname.py>*
in the location of script.

Scripts should be executed in following order:
	1. *EXTRACT/species_data_import.py*
	2. *EXTRACT/list_annex_transform.py*
	3. *EXTRACT/legend_tranform.py*
and after object in database are created:
	4. *data_staging.py*
	