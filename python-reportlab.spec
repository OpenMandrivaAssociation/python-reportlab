Summary:	ReportLab library to create PDF documents using Python
Name:		python-reportlab
Version:	2.6
Release:	4
License:	BSD
Group:		Publishing
Url:		http://www.reportlab.org/
# Upstream tarball with Odyssey text and non-free font files replaced
# Changes copied from Debian package - AdamW 2008/02
Source0:	http://www.reportlab.org/ftp/reportlab-%{version}.tar.gz
#Source1:	rl_accel-0.61-daily-unix.tgz
# From Debian, rediffed: changes source to use the free replacement 
# fonts - AdamW 2008/02
Patch1:		reportlab-2.5-fix_build.patch
BuildRequires:	pkgconfig(freetype2)
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
%setup -qn reportlab-%{version}
%apply_patches
find . -type f | xargs perl -p -i -e 's@#!/bin/env python@#!/usr/bin/env python@'

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --compile --optimize=2
rm -rf %{buildroot}}%{py_platsitedir}/reportlab/fonts

%files
%doc LICENSE.txt README.txt
%{py_platsitedir}/*

