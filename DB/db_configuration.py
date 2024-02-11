import subprocess

#create db
script_to_run = "create_db.py"
subprocess.run(["python3", script_to_run])

#create tables
script_to_run = "create_initial_tables.py"
subprocess.run(["python3", script_to_run])

#create infos
script_to_run = "create_initial_information.py"
subprocess.run(["python3", script_to_run])