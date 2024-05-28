# B1RDSPOT
This projects develops polish birds database for private usage.
For now it consits of two parts:
 - ETL_init - python sctipts that for following tasks:
	* web scrapping of bird data from polish faunistic comitee website
	* web scrapiing of english bird names from wikipedia
	* filling missing translations
	* initial transformations of data
	* loading data to stage tables
 - data structure - DDLs of objects in postgre database for imported data