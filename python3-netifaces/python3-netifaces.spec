#
# spec file for package python3-netifaces
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the # file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python3-netifaces
Version:        0.10.5
Release:        1
Summary:        Portable network interface information.
License:        MIT
Group:          Development/Languages/Python
Url:            https://bitbucket.org/al45tair/netifaces/
Source0:         release_0_10_5.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:   python3-base
BuildRequires:   python3-base


%description
netifaces provides a (hopefully portable-ish) way for Python programmers to
get access to a list of the network interfaces on the local machine, and to
obtain the addresses of those network interfaces.

The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux
and Solaris.  On Windows, it is currently not able to retrieve IPv6
addresses, owing to shortcomings of the Windows API.

It should work on other UNIX-like systems provided they implement
either getifaddrs() or support the SIOCGIFxxx socket options, although the
data provided by the socket options is normally less complete.


%prep
%setup -q -n %{name}-%{version}

%build
tar zxvf release_0_10_5.tar.gz
mv al45tair-netifaces-* src
mv src/* .
CFLAGS="%{optflags}" python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}


%files
%defattr(-,root,root)
/usr/lib/python3.4/site-packages/netifaces-%{version}-py3.4.egg-info
/usr/lib/python3.4/site-packages/netifaces.cpython-34m.so

%changelog
