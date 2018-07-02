CREATE TABLE samples.zooarch (
	id                   serial  NOT NULL ,
	sample_id            integer   ,
	element              varchar   ,
	portion              varchar   ,
	side                 varchar   ,
	sex                  varchar   ,
	taxonomic_desciption varchar   ,
	CONSTRAINT pk_zooarch_id PRIMARY KEY ( id )
 );

 CREATE TABLE samples.fusion (
 	fusion_id            serial  NOT NULL ,
 	sample_id            integer   ,
 	fusion               varchar   ,
 	CONSTRAINT pk_fusion_fusion_id PRIMARY KEY ( fusion_id )
  );

  CREATE TABLE samples.teeth (
  	teeth_id             serial  NOT NULL ,
  	sample_id            integer   ,
  	tooth_wear           varchar   ,
  	CONSTRAINT pk_teeth_teeth_id PRIMARY KEY ( teeth_id )
   );

























CREATE TABLE samples.faunal (
  sample_id            integer  NOT NULL ,
	area_easting         integer  NOT NULL ,
	area_northing        integer  NOT NULL ,
	context_number       integer  NOT NULL ,
	sample_number        integer  NOT NULL ,

Table A
	element              varchar(100)  NOT NULL ,
	portion              varchar(100)  NOT NULL ,
	side                 varchar(25)  NOT NULL ,
	sex                  varchar(25)  NOT NULL ,
	taxonomic_description varchar(100)  NOT NULL ,

Table B - A

  fusion               varchar(50)  NOT NULL ,

Table C - A
	tooth_wear           varchar(25)

Table D - B,C

  age_estimation       varchar(50)   ,

  [not used ?]status               varchar(30)   ,




To be investigated further!
	butchery_specific    varchar(200)  NOT NULL ,
	comments             varchar(150)   ,

	gnaw                 varchar(150)  NOT NULL ,
	comments [gnaw]      varchar(100)   ,

	taphonomy              varchar(50)  NOT NULL ,
	comments [taphonomy ]  varchar(150)   ,

	pathology              varchar(150)  NOT NULL ,
	comments [pathology ]  varchar(150)   ,

	burn                 varchar(50)  NOT NULL ,
	comments [burn ]     varchar(150)   ,









	collection_method    varchar(10)   ,
	mandible_with_teeth  bool  NOT NULL ,
	bt                   integer   ,
	ss                   integer   ,
	oc_tje               integer   ,
	ch                   integer   ,
	oa                   integer   ,
	equid                integer   ,
	cer                  integer   ,
	lp                   integer   ,
	meles                integer   ,
	pesc                 integer   ,
	brd                  integer   ,
	canis                integer   ,
	unio                 integer   ,
	cerastoderma         integer   ,
	landsnail            integer   ,
	shell_other          integer   ,
	rodent               integer   ,
	comments             varchar(500)   ,
	ursus                integer   ,
	big_feline_lynx_size integer   ,




CREATE TABLE samples.faunal (
  sample_id            integer  NOT NULL ,
	area_easting         integer  NOT NULL ,
	area_northing        integer  NOT NULL ,
	context_number       integer  NOT NULL ,
	sample_number        integer  NOT NULL ,

Table A
	element              varchar(100)  NOT NULL ,
	portion              varchar(100)  NOT NULL ,
	side                 varchar(25)  NOT NULL ,
	sex                  varchar(25)  NOT NULL ,
	taxonomic_description varchar(100)  NOT NULL ,

Table B - A

  fusion               varchar(50)  NOT NULL ,

Table C - A
	tooth_wear           varchar(25)

Table D - B,C

  age_estimation       varchar(50)   ,

  [not used ?]status               varchar(30)   ,




To be investigated further!
	butchery_specific    varchar(200)  NOT NULL ,
	comments             varchar(150)   ,

	gnaw                 varchar(150)  NOT NULL ,
	comments [gnaw]      varchar(100)   ,

	taphonomy              varchar(50)  NOT NULL ,
	comments [taphonomy ]  varchar(150)   ,

	pathology              varchar(150)  NOT NULL ,
	comments [pathology ]  varchar(150)   ,

	burn                 varchar(50)  NOT NULL ,
	comments [burn ]     varchar(150)   ,









	collection_method    varchar(10)   ,
	mandible_with_teeth  bool  NOT NULL ,
	bt                   integer   ,
	ss                   integer   ,
	oc_tje               integer   ,
	ch                   integer   ,
	oa                   integer   ,
	equid                integer   ,
	cer                  integer   ,
	lp                   integer   ,
	meles                integer   ,
	pesc                 integer   ,
	brd                  integer   ,
	canis                integer   ,
	unio                 integer   ,
	cerastoderma         integer   ,
	landsnail            integer   ,
	shell_other          integer   ,
	rodent               integer   ,
	comments             varchar(500)   ,
	ursus                integer   ,
	big_feline_lynx_size integer   ,
