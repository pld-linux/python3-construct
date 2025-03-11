%define		module	construct
Summary:	A powerful declarative symmetric parser/builder for binary data
Name:		python3-%{module}
Version:	2.10.68
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/construct/
Source0:	https://files.pythonhosted.org/packages/source/c/construct/%{module}-%{version}.tar.gz
# Source0-md5:	e426d3dd1566066e4ef1a03fe474dec0
URL:		https://pypi.org/project/construct/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Construct is a powerful declarative and symmetrical parser and builder
for binary data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, to build
objects into binary data.

The library provides both simple, atomic constructs (such as integers
of various sizes), as well as composite ones which allow you form
hierarchical and sequential structures of increasing complexity.
Construct features bit and byte granularity, easy debugging and
testing, an easy-to-extend subclass system, and lots of primitive
constructs to make your work easier.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%dir %{py3_sitescriptdir}/%{module}/lib
%{py3_sitescriptdir}/%{module}/lib/*.py
%{py3_sitescriptdir}/%{module}/lib/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
