Summary:	ReportLab library to create PDF documents using Python
Name:		python-reportlab
Version:	3.3.0
Release:	1
License:	BSD
Group:		Publishing
Url:		http://www.reportlab.org/
# Upstream tarball with Odyssey text and non-free font files replaced
# Changes copied from Debian package - AdamW 2008/02
Source0:	http://www.reportlab.org/ftp/reportlab-%{version}.tar.gz
#Source1:	rl_accel-0.61-daily-unix.tgz
BuildRequires:	pkgconfig(freetype2)
BuildRequires:  pkgconfig(python2)
BuildRequires:	pkgconfig(python3)

%description
ReportLab is a library that lets you directly create documents in
Adobe's Portable Document Format (PDF) using the Python programming
language.

ReportLab library creates PDF based on graphics commands without
intervening steps. It's therefore extremely fast, and flexible (since
you're using a full-blown programming language).

Sample use cases are:

  * Dynamic PDF generation on the web
  * High-volume corporate reporting and database publishing
  * As embeddable print engine for other applications, including a
    'report language' so that users can customize their own reports.
  * As 'build system' for complex documents with charts, tables and text
    such as management accounts, statistical reports and scientific papers
  * from XML to PDF in one step

%package -n python2-reportlab
Summary:        ReportLab library to create PDF documents using Python
Group:		Publishing

%description -n python2-reportlab
ReportLab is a library that lets you directly create documents in
Adobe's Portable Document Format (PDF) using the Python programming
language.

ReportLab library creates PDF based on graphics commands without
intervening steps. It's therefore extremely fast, and flexible (since
you're using a full-blown programming language).

Sample use cases are:

  * Dynamic PDF generation on the web
  * High-volume corporate reporting and database publishing
  * As embeddable print engine for other applications, including a
    'report language' so that users can customize their own reports.
  * As 'build system' for complex documents with charts, tables and text
    such as management accounts, statistical reports and scientific papers
  * from XML to PDF in one step

%prep
%setup -qn reportlab-%{version}
%apply_patches
find . -type f | xargs perl -p -i -e 's@#!/bin/env python@#!/usr/bin/env python@'
cd ..
cp -a reportlab-%{version} %py3dir

%build
%{__python2} setup.py build build_ext -lm

pushd %py3dir
%{__python3} setup.py build build_ext -lm
popd

%install
%{__python2} setup.py install --root=%{buildroot} --compile --optimize=2 
rm -rf %{buildroot}}%{py2_platsitedir}/reportlab/fonts

pushd %py3dir
%{__python3} setup.py install --root=%{buildroot} --compile --optimize=2
rm -rf %{buildroot}}%{py3_platsitedir}/reportlab/fonts
popd

%files
%doc LICENSE.txt README.txt
%{py3_platsitedir}/*

%files -n python2-reportlab
%doc LICENSE.txt README.txt
%{py2_platsitedir}/*

