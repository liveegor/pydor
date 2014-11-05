#!/usr/bin/python
# -*- coding: utf-8 -*-



# Connection data
server = 'orclsrv'
SID = 'study'
login = 'autopark'
password = '0000'



# Queries
SQL_GetDisps = 'select disp_id, disp_name from dispatcher'

SQL_GetGms 	 = 'select gm_id, gm_name from GARAGE_MANAGER'

SQL_GetBreaks    = ''' select break_numb, bus_number, break_date, break_what 
from break 
where gm_id = %d '''

SQL_GetBreaks_2  = "select \
break_numb, gm_id, bus_number, break_date, break_descr,\
break_what, break_costs, break_spare_parts, break_works \
from break \
where break_numb = %d"

SQL_InsertBreak  = "insert into break\n \
(break_numb, gm_id, bus_number, break_date, break_descr,\
break_what, break_costs, break_spare_parts, break_works)\n \
values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"

SQL_GetBuses = 'select bus_number from bus'

SQL_UpdateBreak  = "update break \
set gm_id = '%s', bus_number = '%s', break_date = '%s', \
 break_descr = '%s', break_what = '%s', break_costs = '%s', \
 break_spare_parts = '%s', break_works = '%s' \
 where break_numb = '%s'"

SQL_GetRuns  = ["select r.run_id, d.driv_name, r.route_numb, r.run_date \
from run r, driver d  \
where r.driv_id = d.driv_id \
and r.bus_number = d.bus_number \
and r.disp_id = %d ", \
\
"select r.run_id, d.driv_name, r.route_numb, r.run_date \
from run r, driver d  \
where r.driv_id = d.driv_id \
and r.bus_number != d.bus_number \
and r.disp_id = %d "]

SQL_DeleteRun = 'delete from run \
where run_id = %d'

SQL_DeleteBreak = 'delete from break \
where break_numb = %d'

SQL_GetWorkers = ["select d.disp_id, d.disp_name, d.disp_salary, count(*) \
from dispatcher d, run r \
where d.disp_id = r.disp_id \
group by d.disp_id, d.disp_name, d.disp_salary ", \
\
"select g.gm_id, g.gm_name, g.gm_salary, count (*) \
from garage_manager g, break b \
where g.gm_id = b.gm_id \
group by g.gm_id, g.gm_name, g.gm_salary "]

SQL_Report = "select month, count(*) from \
(select to_char(run.run_date, 'MM') as month, route.route_dist as distance \
from run, route \
where to_char(run.run_date, 'YYYY') = to_char(sysdate, 'YYYY') and \
run.route_numb = route.route_numb) \
group by month"

SQL_Report_2 = "select month, sum(distance) from \
(select to_char(run.run_date, 'MM') as month, route.route_dist as distance \
from run, route \
where to_char(run.run_date, 'YYYY') = to_char(sysdate, 'YYYY') and \
run.route_numb = route.route_numb and \
run.bus_number = '%s' ) \
group by month"

SQL_GetRoutes = 'select route_numb from route'

SQL_GetDrivers = 'select driv_name, driv_id from driver'

SQL_GetRuns_2 = '''select bus_number, route_numb, driv_id, run_date 
from run 
where run_id = %d '''

SQL_InsertRun = ''' insert into run 
(run_id, disp_id, bus_number, run_date, route_numb, driv_id) 
values ('%d', '%d', '%s', '%s', '%s', '%d' ) '''

SQL_UpdateRun = ''' update run 
set disp_id = '%d', bus_number = '%s', 
run_date = '%s', route_numb = '%s', driv_id = '%d' 
where run_id = '%d' '''

# Call if this is main module
# (not included)
if __name__ == '__main__':

    import sys
    import prettytable


    # Russian support for client
    import os
    os.environ['NLS_LANG'] = 'Russian.AL32UTF8'


    # Good module import
    try:
        import cx_Oracle
    except ImportError, info:
        print "Import Error:", info
        sys.exit()
    if cx_Oracle.version < '3.0':
        print "Very old version of cx_Oracle :", cx_Oracle.version
        sys.exit()


    # Connect to database
    try:
        db = cx_Oracle.connect (login, password, server + '/' + SID)
        cursor = db.cursor()

        quere = SQL_Report
        # quere = "select to_char(sysdate, 'YYYY') from dual"

        cursor.execute(quere)
        db.commit()

        pt = prettytable.from_db_cursor(cursor)
        print pt.get_string()


        db.close()

    except cx_Oracle.Error, error:
        print str(error).decode('utf8')