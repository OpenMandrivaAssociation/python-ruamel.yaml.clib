Name:		python-ruamel.yaml.clib
Version:	0.2.12
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml.clib/ruamel.yaml.clib-%{version}.tar.gz
Summary:	C version of reader, parser and emitter for ruamel.yaml derived from libyaml
URL:		https://pypi.org/project/ruamel.yaml.clib/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildSystem:	python

%description
C version of reader, parser and emitter for ruamel.yaml derived from libyaml

%files
%{py_platsitedir}/*.so
%{py_platsitedir}/ruamel.yaml.clib-%{version}.dist-info
