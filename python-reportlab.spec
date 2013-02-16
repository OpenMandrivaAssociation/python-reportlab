Summary:	ReportLab library to create PDF documents using Python
Name:		python-reportlab
Version:	2.5
Release:	%mkrel 4
URL:		http://www.reportlab.org/
# Upstream tarball with Odyssey text and non-free font files replaced
# Changes copied from Debian package - AdamW 2008/02
Source0:	http://www.reportlab.org/ftp/reportlab-%{version}.tar.gz
#Source1:	rl_accel-0.61-daily-unix.tgz
# From Debian, rediffed: changes source to use the free replacement 
# fonts - AdamW 2008/02
Patch0:		python-reportlab-2.1-fontclean.patch
Patch1:		reportlab-2.5-fix_build.patch
BuildRequires:	pkgconfig(freetype2)
License:	BSD
Group:		Publishing
%py_requires -d

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

%prep
%setup -q -n reportlab-%{version}
%patch1 -p1 -b .link
find . -type f | xargs perl -p -i -e 's@#!/bin/env python@#!/usr/bin/env python@'

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2
rm -rf %{buildroot}}%{py_platsitedir}/reportlab/fonts

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.txt README.txt
%{py_platsitedir}/*
