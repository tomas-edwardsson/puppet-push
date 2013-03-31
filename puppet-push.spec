Name:		puppet-push
Version:	0.1
Release:	1%{?dist}
Summary:	Pushes puppet catalog to targets that can not connect to the puppet master.

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/tomas-edwardsson/puppet-push
Source0:	%{name}-%{version}.tar.gz

Requires:	puppet >= 2.7.0
Requires:	python
Requires:	openssh-clients
Requires:	rsync
Requires:	coreutils >= 8.0
Requires:	python-simplejson

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Puppet defaults to using a pull model, nodes pull their configs. puppet-push
generates the nodes catalog an pushes it to it via ssh.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 bin/puppet-push ${RPM_BUILD_ROOT}%{_bindir}/puppet-push
install -D -m 755 bin/extract-file-sources.py ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/extract-file-sources.py
install -D -m 755 etc/puppet-push.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/puppet-push.conf
mkdir -p ${RPM_BUILD_ROOT}%{_sharedstatedir}/puppet-push

%files
%defattr(-,root,root,-)
%doc LICENSE README.md etc/site-push.pp-example
%{_bindir}/puppet-push
%config(noreplace) %{_sysconfdir}/puppet-push.conf
%dir %{_sharedstatedir}/puppet-push

%{_libexecdir}/%{name}/extract-file-sources.py
%if 0%{?rhel} >= 6
%{_libexecdir}/%{name}/extract-file-sources.pyc
%{_libexecdir}/%{name}/extract-file-sources.pyo
%endif
%if 0%{?fedora} >= 16
%{_libexecdir}/%{name}/extract-file-sources.pyc
%{_libexecdir}/%{name}/extract-file-sources.pyo
%endif

%changelog

