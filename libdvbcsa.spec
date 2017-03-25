Name:           libdvbcsa
Version:        1.1.0
Release:        3%{?dist}
Summary:        DVB Common Scrambling Algorithm with encryption and decryption capabilities

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.videolan.org/developers/libdvbcsa.html
Source0:        http://download.videolan.org/pub/videolan/libdvbcsa/%{version}/libdvbcsa-%{version}.tar.gz


%description
libdvbcsa is a free and portable implementation of the DVB Common
Scrambling algorithm with decryption and encryption capabilities.

It comes in two flavors: a classical single packet implementation and
a faster parallel bitslice implementation.



%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{_isa} = %{version}-%{release}

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


%make_build


%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/dvbcsa/
%{_libdir}/*.so


%changelog
* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-2
- Spec file clean-up

* Thu Jun 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Jan  5 2009 kwizart < kwizart at gmail.com > - 1.0.0-1
- Initial spec file

