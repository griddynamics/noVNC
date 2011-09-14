%global with_doc 0

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:             openstack-noVNC
Version:	  2011.3
Release:	  0.20110914.1.3%{?dist}
Summary:          OpenStack Nova VNC console service 

Group:            Applications/System
License:          LGPL v3 with exceptions
Vendor:           Grid Dynamics Consulting Services, Inc.
URL:              https://github.com/openstack/noVNC
Source0:          %{name}-%{version}.tar.gz 
Source1:          openstack-nova-vncproxy.init 

BuildRoot:        %{_tmppath}/noVNC-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:        noarch

%description
noVNC is a VNC client written  using HTML5 (Web Sockets, Canvas) with encryption (wss://) support.


%prep

%build

%install
install -p -D -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/openstack-nova-vncproxy
# Add noVNC console
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/noVNC
tar zxf %{SOURCE0} -C %{buildroot}%{_sharedstatedir}/nova/noVNC


%clean
rm -rf %{buildroot}

%files 
%{_bindir}/nova-vncproxy
%{_initrddir}/openstack-nova-vncproxy
%{_sharedstatedir}/nova/noVNC
#%doc %{_sharedstatedir}/nova/noVNC/LICENSE.txt
#%doc %{_sharedstatedir}/nova/noVNC/README.md


%changelog
* Wed Sep 14 2011 Pavel Shkitin <pshkitin@griddynamics.com>
- Imported sources from upstream at commit 7873bed

