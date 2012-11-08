import "nodes"

# Push style cannot push to server, use local file bucket
filebucket { local:
        server => false,
        path => "/var/lib/puppet/clientbucket",
}

File { backup => local }
Exec { path => "/usr/bin:/usr/sbin:/bin:/sbin" }

