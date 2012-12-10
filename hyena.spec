Name:		hyena
License:	MIT
Group:		System/Libraries 
Version:	0.5
Release:	%mkrel 3
Summary:	Library for .NET applications
Url:		http://banshee-project.org/
Source:		http://ftp.acc.umu.se/pub/GNOME/sources/hyena/0.5/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM coolo@opensuse.org - broken Makefile syntax
Patch0:		fix-makefile.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	gtk-sharp2
BuildRequires:	mono-basic
BuildRequires:	mono-devel
BuildRequires:	mono-nunit
BuildRequires:	perl-XML-Parser
BuildRequires:	autoconf automake libtool make pkgconfig
BuildRequires:	gtk-sharp2-devel
Requires:	mono
Requires:	gtk-sharp2

%description
Hyena is a .NET library that powers Banshee and PDF Mod, among others.

%prep
%setup -q
%patch0 -p1

%build
%configure 
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# % find_lang % {name}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
# % doc AUTHORS NEWS README COPYING
%{_libdir}/%{name}
%{_libdir}/pkgconfig/*.pc

#% files lang -f % {name}.lang


%changelog
* Wed Dec 14 2011 Götz Waschk <waschk@mandriva.org> 0.5-3mdv2012.0
+ Revision: 740996
- rebuild for gtk+ packaging breakage

* Mon Oct 31 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.5-2
+ Revision: 708008
- rpmlint fixes
- require mono fix

* Mon Oct 31 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.5-1
+ Revision: 708005
- imported package hyena

