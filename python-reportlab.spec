%global module reportlab
%global mod %(m=%{module}; echo ${m:0:1})

%global cmapdir %(echo `rpm -qls ghostscript-common | grep CMap | awk '{print $2}'`)

Summary:	ReportLab library to create PDF documents using Python
Name:		python-%{module}
Version:	3.6.11
Release:	1
License:	BSD and GPLv2+
Group:		Publishing
URL:		https://www.reportlab.com/opensource/
Source0:	https://pypi.io/packages/source/%{mod}/%{module}/%{module}-%{version}.tar.gz
#Source1:	rl_accel-0.61-daily-unix.tgz
#Patch0:		reportlab-3.5.23-no-Lusrlib.patch
BuildRequires:	fontpackages-devel
BuildRequires:	ghostscript
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	font(dejavusans)

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
%license LICENSE.txt
%doc README.txt CHANGES.md
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}-py%{python3_version}.egg-info

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n reportlab-%{version}

# remove bundled libs
rm -rf src/rl_addons/renderPM/libart_lgpl

# clean up hashbangs from libraries
find src -name '*.py' | xargs sed -i -e '/^#!\//d'

# patch the CMap path by adding Fedora ghostscript path before the match
#sed -i '/\~\/\.local\/share\/fonts\/CMap/i''\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ '\'%{cmapdir}\''\,' src/reportlab/rl_settings.py

# drop bundled egg-info
rm -rf src/reportlab.egg-info/

%build
CFLAGS="%{build_cflags} -Isrc/rl_addons/renderPM `pkg-config --cflags libart-2.0`" \
%__python3 setup.py build -- --use-system-libart --no-download-t1-files

%install
CFLAGS="%{build_cflags} -Isrc/rl_addons/renderPM `pkg-config --cflags libart-2.0`" \
%{__python} setup.py  install -O1 --skip-build --root %{buildroot} --use-system-libart --no-download-t1-files

#rm -rf %{buildroot}}%{py2_platsitedir}/reportlab/fonts

# Unbundled fonts
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Regular") %{buildroot}%{python3_sitearch}/reportlab/fonts/Vera.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold Oblique") %{buildroot}%{python3_sitearch}/reportlab/fonts/VeraBI.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold") %{buildroot}%{python3_sitearch}/reportlab/fonts/VeraBd.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Condensed Oblique") %{buildroot}%{python3_sitearch}/reportlab/fonts/VeraIt.ttf

# remove license
rm -f %{buildroot}%{python3_sitearch}/reportlab/fonts/bitstream-vera-license.txt

# add resources
cp -a demos %{buildroot}%{python3_sitearch}/reportlab/
cp -a tools %{buildroot}%{python3_sitearch}/reportlab/
