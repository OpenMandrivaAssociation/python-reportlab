Summary:	ReportLab library to create PDF documents using Python
Name:		python-reportlab
Version:	4.4.6
Release:	1
License:	BSD and GPLv2+
Group:		Publishing
URL:		https://www.reportlab.com/opensource/
Source0:	https://pypi.io/packages/source/r/reportlab/reportlab-%{version}.tar.gz
#Source1:	rl_accel-0.61-daily-unix.tgz
#Patch0:		reportlab-3.5.23-no-Lusrlib.patch
#BuildRequires:	fontpackages-devel
#BuildRequires:	ghostscript
#BuildRequires:	pkgconfig(freetype2)
#BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildRequires:	font(dejavusans)
BuildArch:      noarch

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

%files
%license LICENSE
%doc README.txt CHANGES.md
%{py_puresitedir}/reportlab
%{py_puresitedir}/reportlab-%{version}*-info

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n reportlab-%{version}

# clean up hashbangs from libraries
find src -name '*.py' | xargs sed -i -e '/^#!\//d'

# drop bundled egg-info
rm -rf src/reportlab.egg-info/

%build
%py_build -- --no-download-t1-files

%install
%py_install

# Unbundled fonts
#rm -rf %{buildroot}%{py_puresitedir}/reportlab/fonts
install -dpm 0755 %{buildroot}%{py_puresitedir}/reportlab/fonts
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Regular") %{buildroot}%{py_puresitedir}/reportlab/fonts/Vera.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold Oblique") %{buildroot}%{py_puresitedir}/reportlab/fonts/VeraBI.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold") %{buildroot}%{py_puresitedir}/reportlab/fonts/VeraBd.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Condensed Oblique") %{buildroot}%{py_puresitedir}/reportlab/fonts/VeraIt.ttf
rm -f %{buildroot}%{python3_sitearch}/reportlab/fonts/bitstream-vera-license.txt

# add resources
cp -a demos %{buildroot}%{py_puresitedir}/reportlab/
cp -a tools %{buildroot}%{py_puresitedir}/reportlab/

