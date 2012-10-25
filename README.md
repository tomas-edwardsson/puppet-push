puppet-push push based puppetry
===============================

What am I trying to solve?
--------------------------
* Where pulling is not an option (DMZ)

What does it need?
------------------
* SSH key access to the target node as root
* puppet installed on the remote node


What does it do?
----------------
* Generates facts on target node and fetches
* Compiles the catalog on the master
* Pushes files from the File[] resource and replaces puppet:/// paths
* Modifies catalog to replace the File[] source statements
* Pushes catalog to target node
* Applies catalog


License
=======
GPLv3


Author
======
Tomas Edwardsson <tommi@ok.is>
Sponsored by the Icelandic National Hospital
