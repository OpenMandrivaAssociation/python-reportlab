%define ver 1_19

Summary: ReportLab library to create PDF documents using Python
Name: python-reportlab
Version: 2.0
Release: %mkrel 1
URL: http://www.reportlab.org/
Source0: http://www.reportlab.org/ftp/ReportLab_%{ver}.tar.bz2
License: BSD
Group: Publishing
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: python-devel

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
%setup -q -n reportlab-%ver
find . -type f | xargs perl -p -i -e 's@#!/bin/env python@#!/usr/bin/env python@'

%build
cd reportlab
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
cd reportlab
python setup.py install --root=$RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT%_libdir/python*
tar c reportlab | tar x -C site-packages
rm -rf reportlab

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc reportlab/docs
%{py_platsitedir}/*



