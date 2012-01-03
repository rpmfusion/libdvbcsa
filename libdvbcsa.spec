Name:           libdvbcsa
Version:        1.1.0
Release:        1%{?dist}
Summary:        DVB Common Scrambling Algorithm with encryption and decryption capabilities

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.videolan.org/developers/libdvbcsa.html
Source0:        http://download.videolan.org/pub/videolan/libdvbcsa/%{version}/libdvbcsa-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
libdvbcsa is a free and portable implementation of the DVB Common
Scrambling algorithm with decryption and encryption capabilities.

It comes in two flavors: a classical single packet implementation and
a faster parallel bitslice implementation.



%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static \
%ifarch %{ix86} x86_64
  --enable-sse2 --enable-uint64 \
%endif
%ifarch ppc ppc64
  --enable-altivec \
%endif


make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/dvbcsa/
%{_libdir}/*.so


%changelog
* Thu Jun 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Jan  5 2009 kwizart < kwizart at gmail.com > - 1.0.0-1
- Initial spec file

