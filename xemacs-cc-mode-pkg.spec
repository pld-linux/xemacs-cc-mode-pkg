Summary:	C, C++ and Java language support
Summary(pl):	Tryby dla C, C++ i Javy
Name:		xemacs-cc-mode-pkg
%define 	srcname	cc-mode
Version:	1.17
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		xemacs-cc-mode-pkg-info.patch
URL:		http://www.xemacs.org/
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	xemacs-sumo

%description
CC Mode is a GNU Emacs mode for editing files containing C, C++,
Objective-C, Java, CORBA IDL, and Pike code. It provides syntax-based
indentation and has several handy commands and some minor modes to
%{__make} the editing easier. Note that CC Mode does _not_ provide
font-locking; there are other Emacs packages for that.

%description -l pl 
CC mode to Emacsowy tryb przeznaczony od edycji program� w j�zyku C i
innych j�zykach o podobnej sk�adni: C++, Objective-C, CORBA IDL, Pike.
(Dla Javy stworzono osobny pakiet: "jde").

%prep
%setup -q -c
%patch0 -p1

%build
(cd man/cc-mode; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	lisp/cc-mode/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/cc-mode/ChangeLog.gz
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
