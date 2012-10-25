puppet-push push based puppetry
===============================

What am I trying to solve?
--------------------------
* Puppet defaults to using a pull model, nodes pull their configs
* Implement Puppet where pulling is not an option (DMZ)

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



Install
=======
git install
-----------
Install git with apt, yum, whatever your flavor
```
yum install git
```

git clone
---------
```
git clone git://github.com/tomas-edwardsson/puppet-push.git /opt/puppet-push
```

configure
---------
edit /opt/puppet-push/bin/puppet-push - interesting stuff there
```
verbose=0
PATH=/opt/puppet-push/bin:/bin:/usr/bin
PUPPET_PUSH_BASE="/opt/puppet-push"
TARGET=$1
PUPPET_VAR_DIR="/var/lib/puppet"
REMOTE_SSH_USER=root
PUPPET_MODULE_DIR=/etc/puppet/modules/production
```

edit /opt/puppet-push/bin/extract-file-sources.py
```
puppet_push_path="/opt/puppet-push"
puppet_module_dir="/etc/puppet/modules/production"
```

Run
---
/opt/puppet-push/bin/puppet-push <nodename>


Disclaimer
==========
This is an ALPHA, I have only run it on a few nodes and it may break something.

License
=======
GPLv3


Author
======
Tomas Edwardsson <tommi@tommi.org>
Sponsored by the Icelandic National Hospital


