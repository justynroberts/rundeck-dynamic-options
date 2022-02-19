# RunDeck Dynamic Options
Convert server based comma separated lists to local API serving options that can be consumed by Rundeck options.
Quick outline to solve a request.Feel free to use/modify.

**Overview**
Basic http flask server, scans location for csv files, and serves up as routes.

***Prerequisites:***
python3.x installed on Server. 
you will need to make sure flask is installed as a module (`pip install flask`), but you can follow conventions by running `pip install requirements.txt` also. 

Potentially this file could be installed elsewhere other than the server, but well, its only serving up `http`, so not recommended.

**Installation.** 
**git clone** this to a location on your rundeck server
Run application with `python3 rundeck-dynamic-options.py directory`
where `directory` is the location of your lists 

**Run application as a service**
Follow specific rules for your platform on running python as a service, but for example to run python file as a linux service on RHEL/CENTOS -

Subdirectory `options` contains csv files  with the extension .`list`. File name serves as route when the server starts
eg
http://localhost:3000/options/flowers 
would refer to flowers.list in the directory as defined on startup

Sample flowers.list:
   

     rose,orchid,daisy,dandelion

Use in Rundeck options by using the URL in the remote list option of any rundeck Job option


**Notes.**

 - Not really a whole lot of error checking. Please make sure you are writing clean, one line CSV files
 - Options can be nested, and generally support more complex scenarios, this is really just a simple use case.
 - Options can also contain 2 values, a label and an actual value - In this case Im just writing both the label and the value as the same.


Reference:
https://docs.rundeck.com/3.4.10/manual/job-options.html#option-model-provider
