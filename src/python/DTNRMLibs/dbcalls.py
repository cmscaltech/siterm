#!/usr/bin/env python
"""
DB Backend SQL Calls to databses.

Copyright 2019 California Institute of Technology
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
Title 			: dtnrm
Author			: Justas Balcas
Email 			: justas.balcas (at) cern.ch
@Copyright		: Copyright (C) 2019 California Institute of Technology
Date			: 2019/05/01
"""
create_models = """CREATE TABLE models(id INTEGER PRIMARY KEY AUTOINCREMENT, uid text NOT NULL,
                                       insertdate INTEGER NOT NULL, fileloc text NOT NULL, content text NOT NULL)"""
create_deltas = """CREATE TABLE deltas(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       uid text NOT NULL,
                                       insertdate INTEGER NOT NULL,
                                       updatedate INTEGER NOT NULL,
                                       state text NOT NULL,
                                       deltat text NOT NULL,
                                       content text NOT NULL,
                                       modelid text NOT NULL,
                                       reduction text NOT NULL,
                                       addition text NOT NULL,
                                       reductionid text,
                                       modadd text,
                                       connectionid text NOT NULL)"""
create_delta_connections = """CREATE TABLE delta_connections(id INTEGER PRIMARY KEY AUTOINCREMENT, deltaid text NOT NULL,
                                                             connectionid text NOT NULL, state text NOT NULL)"""
create_states = """CREATE TABLE states(id INTEGER PRIMARY KEY AUTOINCREMENT, deltaid text NOT NULL,
                                     state text NOT NULL, insertdate INTEGER NOT NULL)"""
create_hoststates = """CREATE TABLE hoststates(id INTEGER PRIMARY KEY AUTOINCREMENT, deltaid text NOT NULL, state text NOT NULL,
                                             insertdate INTEGER NOT NULL, updatedate INTEGER NOT NULL, hostname text NOT NULL)"""
create_hoststateshistory = """CREATE TABLE hoststateshistory(id INTEGER PRIMARY KEY AUTOINCREMENT, deltaid text NOT NULL, state text NOT NULL,
                                                           insertdate INTEGER NOT NULL, hostname text NOT NULL)"""
create_parsed = "CREATE TABLE parsed(id INTEGER PRIMARY KEY AUTOINCREMENT, deltaid text NOT NULL, vals text NOT NULL, insertdate INTEGER NOT NULL)"
create_hosts = """CREATE TABLE hosts(id INTEGER PRIMARY KEY AUTOINCREMENT, ip text NOT NULL, hostname text NOT NULL,
                                   insertdate INTEGER NOT NULL, updatedate INTEGER NOT NULL, hostinfo text NOT NULL)"""
create_servicestates = """CREATE TABLE servicestates(id INTEGER PRIMARY KEY AUTOINCREMENT, hostname text NOT NULL, servicename text NOT NULL, servicestate text NOT NULL, updatedate INTEGER NUT NULL)"""


insert_models = "INSERT INTO models(uid, insertdate, fileloc, content) VALUES(:uid, :insertdate, :fileloc, :content)"
insert_deltas = """INSERT INTO deltas(uid, insertdate, updatedate, state, deltat, content, modelid, reduction, addition, reductionid, modadd, connectionid)
                   VALUES(:uid, :insertdate, :updatedate, :state, :deltat, :content, :modelid, :reduction, :addition, :reductionid, :modadd, :connectionid)"""
insert_delta_connections = """INSERT INTO delta_connections(deltaid, connectionid, state) VALUES(:deltaid, :connectionid, :state)"""
insert_states = "INSERT INTO states(deltaid, state, insertdate) VALUES(:deltaid, :state, :insertdate)"
insert_hoststates = "INSERT INTO hoststates(deltaid, state, insertdate, updatedate, hostname) VALUES(:deltaid, :state, :insertdate, :updatedate, :hostname)"
insert_hoststateshistory = "INSERT INTO hoststateshistory(deltaid, state, insertdate, hostname) VALUES(:deltaid, :state, :insertdate, :hostname)"
insert_parsed = "INSERT INTO parsed(deltaid, vals, insertdate) VALUES(:deltaid, :vals, :insertdate)"
insert_hosts = "INSERT INTO hosts(ip, hostname, insertdate, updatedate, hostinfo) VALUES(:ip, :hostname, :insertdate, :updatedate, :hostinfo)"
insert_servicestates = "INSERT INTO servicestates(hostname, servicename, servicestate, updatedate) VALUES(:hostname, :servicename, :servicestate, :updatedate)"

get_models = "SELECT id, uid, insertdate, fileloc, content FROM models"
get_deltas = "SELECT id, uid, insertdate, updatedate, state, deltat, content, modelid, reduction, addition, reductionid, modadd, connectionid FROM deltas"
get_delta_connections = "SELECT id, deltaid, connectionid, state FROM delta_connections"
get_states = "SELECT id, deltaid, state, insertdate FROM states"
get_hoststates = "SELECT id, deltaid, state, insertdate, updatedate, hostname FROM hoststates"
get_hoststateshistory = "SELECT id, deltaid, state, insertdate, hostname FROM hoststateshistory"
get_parsed = "SELECT id, deltaid, vals, insertdate FROM parsed"
get_hosts = "SELECT id, ip, hostname, insertdate, updatedate, hostinfo FROM hosts"
get_servicestates = "SELECT id, hostname, servicename, servicestate, updatedate FROM servicestates"

update_deltas = "UPDATE deltas SET updatedate = :updatedate, state = :state WHERE uid = :uid"
update_delta_connections = "UPDATE delta_connections SET state = :state WHERE connectionid = :connectionid AND deltaid = :deltaid"
update_deltasmod = "UPDATE deltas SET updatedate = :updatedate, modadd = :modadd WHERE uid = :uid"
update_hoststates = "UPDATE hoststates SET state = :state, updatedate = :updatedate WHERE id = :id"
update_hosts = "UPDATE hosts SET ip = :ip, hostname = :hostname, updatedate = :updatedate, hostinfo = :hostinfo WHERE id = :id"
update_servicestates = "UPDATE servicestates SET servicestate = :servicestate, updatedate = :updatedate WHERE hostname = :hostname AND servicename = :servicename"

delete_models = "DELETE FROM models"
delete_states = "DELETE FROM states"
delete_hoststates = "DELETE FROM hoststates"
delete_hosts = "DELETE FROM hosts"
