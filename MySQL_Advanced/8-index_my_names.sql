-- creates an index on the first character of the 'name' column

CREATE INDEX idx_name_first ON names (name(1));
