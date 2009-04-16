Name:           bsgit
BuildRequires:  python-devel
License:        GPL v2 or later
Group:          Productivity/Text/Utilities
AutoReqProv:    on
Version:        0
Release:        0
Summary:        Import packages from the build service into git
Source:         bsgit-%version.tar.gz
Requires:       git-core osc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%description
This is a first version of a git frontend for the build service.  Right now,
all it does is import packages from the build service into branches in a git
repository.  Changes in git cannot be exported back to the build service so far.

%prep
%setup

%build
CFLAGS="%{optflags}" \
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root %{buildroot}
mv %buildroot%_prefix/bin/bsgit.py %buildroot%_prefix/bin/bsgit

%files
%defattr(-,root,root)
/usr/bin/bsgit
%python_sitelib/*

%changelog
