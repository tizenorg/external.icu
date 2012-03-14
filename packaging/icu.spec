Name:      icu
Version:   4.8.1
Release:   2.65
Summary:   International Components for Unicode
Group:     Development/Tools
License:   MIT
URL:       http://www.icu-project.org/
Source0:   http://download.icu-project.org/files/icu4c/4.8.1/icu4c-4_8_1-src.tgz
Patch0:    hack-atomics.diff
BuildRequires: doxygen, autoconf
Requires: lib%{name} = %{version}-%{release}

%description
Tools and utilities for developing with icu.

%package -n lib%{name}
Summary: International Components for Unicode - libraries
Group:   System/Libraries

%description -n lib%{name}
The International Components for Unicode (ICU) libraries provide
robust and full-featured Unicode services on a wide variety of
platforms. ICU supports the most current version of the Unicode
standard, and they provide support for supplementary Unicode
characters (needed for GB 18030 repertoire support).
As computing environments become more heterogeneous, software
portability becomes more important. ICU lets you produce the same
results across all the various platforms you support, without
sacrificing performance. It offers great flexibility to extend and
customize the supplied services.

%package  -n lib%{name}-devel
Summary:  Development files for International Components for Unicode
Group:    Development/Libraries
Requires: lib%{name} = %{version}-%{release}
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}-devel
Includes and definitions for developing with icu.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
autoconf
%configure --with-data-packaging=library --disable-samples --disable-renaming
#sed -i -- "s/-nodefaultlibs -nostdlib//" config/mh-linux
make # %{?_smp_mflags} # -j(X>1) may "break" man pages as of 3.2, b.f.u #2357

%install
rm -rf $RPM_BUILD_ROOT __docs
make install DESTDIR=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*
rm -rf $RPM_BUILD_ROOT/usr/share/man
rm -f $RPM_BUILD_ROOT/usr/share/icu/%{version}/license.html

%clean
rm -rf $RPM_BUILD_ROOT

%post -n lib%{name} -p /sbin/ldconfig

%postun -n lib%{name} -p /sbin/ldconfig

%files
%{_bindir}/derb
%{_bindir}/genbrk
%{_bindir}/gencfu
%{_bindir}/gencnval
%{_bindir}/genctd
%{_bindir}/genrb
%{_bindir}/makeconv
%{_bindir}/pkgdata
%{_bindir}/uconv
%{_bindir}/icuinfo
%{_sbindir}/*

%files -n lib%{name}
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%{_bindir}/icu-config
%{_includedir}/layout
%{_includedir}/unicode
%{_libdir}/*.so
%{_libdir}/pkgconfig/icu-*.pc
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/install-sh
%{_datadir}/%{name}/%{version}/mkinstalldirs
%{_datadir}/%{name}/%{version}/config

