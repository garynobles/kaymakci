ALTER TABLE samples.icon DROP CONSTRAINT fk_icon_container
ALTER TABLE samples.icon DROP CONSTRAINT fk_icon_store
ALTER TABLE samples.icon DROP CONSTRAINT fk_icon_location
ALTER TABLE samples.container ADD icon_id integer 
ALTER TABLE samples."location" ADD icon_id integer 
ALTER TABLE samples.store ADD icon_id integer 
ALTER TABLE samples.icon DROP COLUMN container_id
ALTER TABLE samples.icon DROP COLUMN location_id
ALTER TABLE samples.icon DROP COLUMN store_id
ALTER TABLE samples.icon DROP COLUMN url
ALTER TABLE samples.icon ADD icon_desc varchar 

CREATE INDEX idx_store_icon_id ON samples.store ( icon_id ) 
ALTER TABLE samples.store ADD CONSTRAINT fk_store_icon FOREIGN KEY ( icon_id ) REFERENCES samples.icon( id ) 

CREATE INDEX idx_location_icon_id ON samples."location" ( icon_id ) 
ALTER TABLE samples."location" ADD CONSTRAINT fk_location_icon FOREIGN KEY ( icon_id ) REFERENCES samples.icon( id ) 

CREATE INDEX idx_container_icon_id ON samples.container ( icon_id ) 
ALTER TABLE samples.container ADD CONSTRAINT fk_container_icon FOREIGN KEY ( icon_id ) REFERENCES samples.icon( id ) 

