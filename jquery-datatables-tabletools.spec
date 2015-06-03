%define		plugin	tabletools
Summary:	DataTables tabletools plugin
Name:		jquery-datatables-%{plugin}
Version:	2.2.4
Release:	1
License:	MIT
Group:		Applications/WWW
# Source0Download: https://datatables.net/download/index#TableTools
Source0:	http://datatables.net/releases/TableTools-%{version}.zip
# Source0-md5:	fbabe57a9c1e0fc8ccd5f37e83333bc4
URL:		https://datatables.net/extensions/tabletools/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jquery-datatables >= 1.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/datatables/%{plugin}

%description
TableTools is a plug-in for the DataTables HTML table enhancer, which
adds a highly customisable button toolbar to a DataTable.

%package demo
Summary:	Demo for jQuery DataTables tabletools plugin
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.datatables %{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery DataTables tabletools plugin.

%prep
%setup -qn TableTools-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/{js,css}

cp -p js/dataTables.tableTools.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{plugin}-%{version}.min.js
cp -p js/dataTables.tableTools.js $RPM_BUILD_ROOT%{_appdir}/js/%{plugin}-%{version}.src.js

ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{plugin}.min.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/js/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/js/%{plugin}.js

cp -p css/dataTables.tableTools.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}-%{version}.min.css
cp -p css/dataTables.tableTools.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}-%{version}.src.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}.min.css
ln -s %{plugin}-%{version}.src.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}.src.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}.css

cp -a images $RPM_BUILD_ROOT%{_appdir}
cp -a swf $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
