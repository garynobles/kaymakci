ALTER TABLE samples.container DROP CONSTRAINT fk_container_icon
ALTER TABLE samples."location" DROP CONSTRAINT fk_location_icon
ALTER TABLE samples.store DROP CONSTRAINT fk_store_icon
ALTER TABLE samples.icon DROP COLUMN id
ALTER TABLE samples.icon ADD icon_id serial NOT NULL 
ALTER TABLE samples.icon ADD CONSTRAINT pk_icon_icon_id PRIMARY KEY ( icon_id ) 

ALTER TABLE samples.container ADD CONSTRAINT fk_container_icon FOREIGN KEY ( icon_id ) REFERENCES samples.icon( icon_id ) 
ALTER TABLE samples.store ADD CONSTRAINT fk_store_icon FOREIGN KEY ( icon_id ) REFERENCES samples.icon( icon_id ) 
ALTER TABLE samples."location" ADD CONSTRAINT fk_location_icon FOREIGN KEY ( icon_id ) REFERENCES samples.icon( icon_id ) 





