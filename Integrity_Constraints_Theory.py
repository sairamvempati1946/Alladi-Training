'''
Integrity Constraints:
--------------------------------------------------------------------------------
Constraints means a rule to followed while creating a table in databases
----------------------------------------------------------------------------------
Following are constraints:
NOT NULL:ensure that a column can not be null value

UNIQUE:Ensure that all the value in a column are different

PRIMARY KEY:It identifies a column uniquely
             it combination of NOT NULL +UNIQUE

FOREIGN KEY:To make one table as parent and another table is child.in this situation child table will have common column
            which exits in parent table hence child table has the foreign key
            ex:person table:parent table
            order table:child table

CHECK:ensure that the values in a column satisfies certain conditions

DEFAULT:It sets the default value and when the user does not supply any value

CREATE INDEX:used to create n index on table to improve retrieval speed.
'''
