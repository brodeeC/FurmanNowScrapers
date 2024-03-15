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
    def insertInto(self, table, connection, commit=True):
        raise NotImplementedError("insertInto not implemented.")
        
class Selector(Queriable):
    '''
    Table is the name of the table that will be inserted with
    attrs is which attributes will be inserted
    conds is a list of conditionals. Each contititonal can be in
        one of three formats:
            1. [a, b] where the statement will be "a = b OR"
            2. [a, b, c] where b is an operateor and the 
                statement will be "a b c OR"
            3. [a, b, c, d]  where d is "AND" or "OR" and the
                query will be "a b c d"
    commit is whether or not the query should automatically be committeed to the 
    '''
    def _formulateSelect(table, attrs="All", conds=None):
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
    
    def _formulateClear(table, conds=None) -> Tuple[str, Tuple[str]]:
        delete = f"DELETE FROM `{table}`"
        if conds is None or len(conds) == 0:
            return delete
        delete += " WHERE"
        for cond in conds:
            delete += f" {cond[0]} {'=' if len(cond) <= 2 else cond[2]} %s {'OR' if len(cond) <= 3 else cond[3]}"
        atr = (e[1] for e in conds)
        
        return delete[:-2], tuple(atr)
            
        
    def _clearHelper(table, connection, conditions, commit):
        Clearable.query(connection, Clearable._formulateClear(table, conditions), commit)
                
    def clearFrom(self, table, connection, commit=True):
        raise NotImplementedError("clear not implemented.")