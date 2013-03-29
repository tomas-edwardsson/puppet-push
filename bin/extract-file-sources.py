#!/usr/bin/python

# Copyright (C) 2012  Tomas Edwardsson

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import simplejson as json
import sys
import os
import pipes

puppet_push_path = "/var/lib/puppet-push"
puppet_module_dir = os.environ["PUPPET_MODULE_DIR"]

def main():
    if len(sys.argv) != 2:
        usage()
    target = sys.argv[1]

    catalog = parse_json('%s/pending/%s.cat' % (puppet_push_path, target))
    r = get_file_sources(catalog)

    for source in r:
        (module, path) = source.split('/', 1)
        if os.path.exists("%s/%s/files/%s" % (puppet_module_dir, module, path)) is False:
            # This happens alot with variable expansion, not warning
            #sys.stderr.write("Warning: file referenced in module %s missing '%s/files/%s'\n" % (module, module, path))
            continue
        sys.stdout.write(pipes.quote("%s/files/%s" % (module, path)) + " ")
    print

def usage():
    sys.stderr.write("Usage %s <hostname>\n" % (sys.argv[0]))
    sys.exit(1)

def get_file_sources(cat):
    """
    Parses the catalog dict and returns file resources based on the following
    conditions:

    * resource type is File
    * resource has parameter 'source'
    * resource does not set recurse
    * resource source starts with puppet:///
    
    This function makes the following assumptions:
        sourceselect => first
        recurse => false

    Returns array of puppet source strings:
    ['puppet:///module/file', '/local/fs/path']
    """


    resources = filter(lambda r: r['type'] == 'File' and r['parameters'].has_key('source'), cat['data']['resources'])

    sources = []
    for r in resources:
        if r['parameters'].has_key('recurse') and r['parameters']['recurse'] != 'false':
            raise Exception('Fatal: File resource %s defined in %s uses recursion, not supported' % ('a','a')) # TODO
        if type(r['parameters']['source']) is list:
            for source in r['parameters']['source']:
                if source.startswith('puppet:///'):
                    sources.append(source[10:])
        else:
            source = r['parameters']['source']
            if source.startswith('puppet:///'):
                sources.append(source[10:])
    return sources

        

def parse_json(file):
    fh = open(file, "r")

    return json.load(fh)


if __name__ == "__main__":
    main()

# vim: ts=4 sts=4 expandtab shiftwidth=4 smarttab autoindent
