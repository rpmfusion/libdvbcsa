Name:           libdvbcsa
Version:        1.1.0
Release:        11%{?dist}
Summary:        DVB Common Scrambling Algorithm with encryption and decryption capabilities

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.videolan.org/developers/libdvbcsa.html
Source0:        https://download.videolan.org/pub/videolan/libdvbcsa/%{version}/libdvbcsa-%{version}.tar.gz
BuildRequires:  gcc

%description
libdvbcsa is a free and portable implementation of the DVB Common
Scrambling algorithm with decryption and encryption capabilities.

It comes in two flavors: a classical single packet implementation and
a faster parallel bitslice implementation.



%package        devel
Summary:        Development files for %{name}
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


%ldconfig_scriptlets


%files
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/dvbcsa/
%{_libdir}/*.so


%changelog
* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-5
- Use https on download

* Sat Mar 25 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-4
- Disable altivec to fix build

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-2
- Spec file clean-up

* Thu Jun 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Jan  5 2009 kwizart < kwizart at gmail.com > - 1.0.0-1
- Initial spec file

