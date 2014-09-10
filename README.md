puppet-push push based puppetry
===============================

What am I trying to solve?
--------------------------
* Puppet defaults to using a pull model, nodes pull their configs
* Implement Puppet where pulling is not an option (DMZ)

What does it need?
------------------
* SSH key access to the target node as root
* puppet and rsync installed on the remote node and local node
* puppet version 2.7.0 or newer
* Alternate site.pp (site-push.pp)


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
git clone git://github.com/tomas-edwardsson/puppet-push.git
```

build rpm or install
--------------------
```
make rpm
```
and install that, or
```
make install
```

configure
---------
edit /etc/puppet-push.conf
```
PUPPET_VAR_DIR="/var/lib/puppet"
PUPPET_MODULE_DIR=/etc/puppet/modules/production
REMOTE_SSH_USER=root

VERBOSE=0
```

Filebucket configuration
------------------------
If you are using a filebucket server for the pull based hosts you will need to override it for the push based hosts.

An alternative site.pp file is provided which can be set in puppet-push.conf but if you can conditionally set the
filebucket and file backup parameters in the manifests for the push based nodes it's possible to skip a special site.pp file.

Containing:
```
filebucket { local:
        server => false,
        path => "/var/lib/puppet/clientbucket",
}

File { backup => local }
```

Run
---
```
puppet-push <nodename>
```


Disclaimer
==========
This is an ALPHA, I have only run it on a few nodes and it may break something.

License
=======
GPLv3


Authors
======
Pall Valmundsson <pall.valmundsson@gmail.com>

Tomas Edwardsson <tommi@tommi.org>

Sponsored by the Icelandic National Hospital


