# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 23:10:02 2024

@author: Michael Peeler
"""

from abc import ABC, abstractmethod
from typing import Tuple
import traceback

class Queriable():
    def query(connection, query, commit = True):
        with connection.cursor() as cursor:
            try:
                cursor.execute(*query)
                if commit:
                    connection.commit()
            except:
                traceback.print_exc()
                connection.rollback()
                
    def cursorQuery(cursor, query):
        try:
            cursor.execute(*query)
        except:
            traceback.print_exc()

class Insertable(ABC, Queriable):
    # Takes as input a table name and list of table field attribute names : attribute value pairs,
    # and a dictionary using those keys, and formulates an insert statement to insert the
    # values of the dictionary into the corresponding attribute fields of the provided table.
    # Returns a string statement and a tuple with all entries that can be unpacked in
    # cursor.execute to run an insert statement 
    # (e.g. cursor.execute(*formulateInsert(table, attrs, dct))). 
    def _formulateInsert(table, attrs):
        insert =  f"INSERT INTO `{table}` ("
        vals = "VALUES ("
        for e in attrs:
            insert += f"{str(e[0])},"
            vals += "%s,"
        atr = (e[1] for e in attrs)
            
        # Removes last comma, adds closing parenthese 
        return insert[:-1] + ") " + vals[:-1] + ")", tuple(atr)
    
    def _insertIntoHelper(table, connection, attrs, commit):
        Insertable.query(connection, Insertable._formulateInsert(table, attrs), commit)
        
    @abstractmethod
    def insertInto(table, connection, commit=True):
        raise NotImplementedError("insertInto not implemented.")
        
class Selector(Queriable):
    def _formulateSelect(table, attrs="All", conds=None, commit=True):
        fieldsSelected = ""
        if isinstance(attrs, list):
            fieldsSelected = ", ".join(attrs)
        elif isinstance(attrs, str) and attrs == "All":
            fieldsSelected = "*"
        
        select = f"SELECT {fieldsSelected} FROM {table} "
        if conds is None or len(conds) == 0:
            return select, ()

        select += "WHERE "
        for c in conds:
            select += " ".join(["",
                                c[0], 
                                "=" if len(c) <= 2 else c[2],
                                "%s", 
                                "OR" if len(c) <= 3 else c[3]])
        select = select[:-2]
        
        return select, tuple(e[1] for e in conds)

class Clearable(ABC, Queriable):
    
    def _formulateClear(table, conds=None) -> Tuple[str, Tuple[str, str]]:
        delete = f"DELETE FROM `{table}`"
        if conds is None or len(conds) == 0:
            return delete
        delete += " WHERE"
        for cond in conds:
            delete += f" {cond[0]} {'=' if len(cond) <= 2 else cond[2]} %s OR"
        atr = (e[1] for e in conds)
        
        return delete[:-2], tuple(atr)
            
        
    def _clearHelper(table, connection, conditions, commit):
        Clearable.query(connection, Clearable._formulateClear(table, conditions), commit)
                
    def clearFrom(table, connection, commit=True):
        raise NotImplementedError("clear not implemented.")