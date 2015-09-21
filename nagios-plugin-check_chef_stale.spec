%define		plugin	check_chef_stale
Summary:	Nagios plugin to check stale nodes in Chef
Name:		nagios-plugin-%{plugin}
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		Networking
Source0:	https://github.com/glensc/nagios-plugin-check_chef_stale/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	3352b9e1c767383590cee8e8a61be672
URL:		https://github.com/glensc/nagios-plugin-check_chef_stale
Requires:	nagios-common
Requires:	knife
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Alerting for stale nodes on Chef with Nagios.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin}.rb $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{plugin}.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
