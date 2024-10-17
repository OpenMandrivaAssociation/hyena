%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Library for .NET applications
Name:		hyena
Version:	0.5
Release:	5
License:	MIT
Group:		System/Libraries
Url:		https://banshee-project.org/
Source:		http://ftp.acc.umu.se/pub/GNOME/sources/hyena/0.5/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM coolo@opensuse.org - broken Makefile syntax
Patch0:		fix-makefile.diff
BuildRequires:	gtk-sharp2
BuildRequires:	mono-basic
BuildRequires:	mono-nunit
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(gapi-2.0)
Requires:	mono
Requires:	gtk-sharp2

%description
Hyena is a .NET library that powers Banshee and PDF Mod, among others.

%files
%{_libdir}/%{name}
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
make

%install
%makeinstall_std


